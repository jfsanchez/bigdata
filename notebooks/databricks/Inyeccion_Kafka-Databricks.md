
# Inyección desde Kafka a Databricks

### Guardamos la información en un topic de kafka

Añadimos estas dos líneas para definir el `bootstrap_servers` y el `topic_name` en un script de python que utilizaremos como el producer de Kafka.
```python
bootstrap_servers = ['<servidor-kafka:puerto>'] 
topic_name = '<nombre-del-topic>'
```
### Leer datos desde Apache Kafka

Establecemos una conexión con el clúster de Kafka alojado en AWS. Definimos el servidor, el puerto y el tópico al que nos queremos suscribir. En el `startingOffsets` se puede indicar si queremos toda la información desde el principio "earliest" o solo la de la última ejecución "latest".
```python
df = (spark.readStream
  .format("kafka")
  .option("kafka.bootstrap.servers", "<servidor-kafka:puerto>")
  .option("subscribe", "<nombre-del-topic>")
  .option("startingOffsets", "latest")
  .load())
```
###  Pasar de Binario a String

Kafka manda el contenido del mensaje (la columna `value`) en formato **binario**. Para que la información se pueda leer, realizamos un `CAST` a formato **String** . Con esto podremos ver el contenido en su formato original.
```python
df_transformed = df.selectExpr("CAST(value AS STRING)")
```

### Transformación de JSON a un dataframe

Extraemos los campos del JSON guardado en la columna `value`.Después definimos un esquema y usamos la función `from_json`.
```python
from pyspark.sql.functions import from_json, col

schema = "columna1 tipo_de_dato, columna2 tipo_de_dato, columna3 tipo_de_dato"

df_transf = (df_transformed
    .withColumn("jsonData", from_json(col("value"), schema))
    .select("jsonData.*"))
```
### Escritura en una tabla Delta Lake

Guardamos el DataFrame ya transformado (`df_transf`) en formato **Delta**. Usamos el modo **append** y configuramos el **checkpoint** para garantizar que, si el sistema falla, no se pierdan datos ni se dupliquen.
```python
(df_transf.writeStream
  .format("delta")
  .outputMode("append")
  .option("checkpointLocation", "<ruta-checkpoint>")
  .toTable("eiab1.miesquema.data_kafka")
    .awaitTermination())
```

### Visualización de la tabla

```sql
SELECT * FROM mi_tabla_delta
```
