# Prueba con Databricks
## Creación del notebook
#### Código
El código pertenece al notebook de “spark-databricks”, pero ligeramente modificado para la correcta implementación de un job con un trigger.


```
dbutils.widgets.text("event_file_path", "")

spark.sql(f"CREATE CATALOG IF NOT EXISTS catalogo")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS catalogo.esquema")
spark.sql(f"USE CATALOG catalogo")
spark.sql(f"USE esquema")
spark.sql(f"CREATE VOLUME IF NOT EXISTS volumen")
from pyspark.sql import functions as F


base = (spark.range(1, 1000)
    .withColumnRenamed('id', 'order_id')
    .withColumn('customer_id', (F.col('order_id') % 120 + 1).cast('int'))
    .withColumn('fecha', F.date_add(F.to_date(F.lit('2025-10-01')), (F.col('order_id') % 60).cast('int')))
    .withColumn('country', F.when((F.col('order_id') % 4)==0, 'ES')
                        .when((F.col('order_id') % 4)==1, 'PT')
                        .when((F.col('order_id') % 4)==2, 'FR')
                        .otherwise('DE'))
    .withColumn('channel', F.when((F.col('order_id') % 3)==0, 'web')
                        .when((F.col('order_id') % 3)==1, 'store')
                        .otherwise('partner'))
    )
lines = (base
        .withColumn('line_id', F.explode(F.array([F.lit(1), F.lit(2)])))
        .withColumn('sku', F.concat(F.lit('SKU-'), F.lpad((F.col('order_id') % 80 + 1).cast('string'), 3, '0')))
        .withColumn('qty', (F.col('line_id') + (F.col('order_id') % 4) + 1).cast('int'))
        .withColumn('importe', (F.round((F.col('qty') * (F.col('order_id') % 50 + 10)) * 1.15, 2)).cast('double'))
        .withColumn('archivo_origen', F.lit(dbutils.widgets.get("event_file_path"))))


lines.write.mode("append").saveAsTable("test_schema")
```


## Creación del job
Creamos el job como tipo Notebook, y añadimos el path del notebook que acabamos de crear.
![Creación del job]("imágenes_databricks\documentacion_trigger_filearrival-1.png")


## Creación del trigger
En el menú de la derecha, vamos a la opción de Schedules and Triggers, y clicamos en Add Trigger.
![Creación del trigger]("imágenes_databricks\documentacion_trigger_filearrival-2.png")




En Trigger type elegimos File arrival.
![Trigger type]("imágenes_databricks\documentacion_trigger_filearrival-3.png")




Y en Storage location añadimos la ruta al volumen.
![Storage location]("imágenes_databricks\documentacion_trigger_filearrival-4.png")

Comprobación del funcionamiento
Subimos un archivo de prueba al volumen.
![Subimos archivo]("imágenes_databricks\documentacion_trigger_filearrival-5.png")




Y esperamos a que se ejecute el trigger del job.
![Ejecución]("imágenes_databricks\documentacion_trigger_filearrival-6.png")




Finalmente comprobamos que se ha creado una tabla nueva con la información del notebook.
![Creación de la tabla]("imágenes_databricks\documentacion_trigger_filearrival-7.png")