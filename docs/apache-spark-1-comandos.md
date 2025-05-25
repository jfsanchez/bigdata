# ⚝ Apache Spark &mdash; 🔲 Comandos

![Logo Apache Spark](images/spark/Apache_Spark_logo.svg#derecha "Logo Apache Spark")

## Enviar traballos: spark-submit

Contorno CESGA:

``` bash
spark-submit --driver-memory 4g --executor-memory 2g --num-executors 4 programa.py
```

Contorno propio:

``` bash
spark-submit --deploy-mode cluster programa.py
```

Exemplo de código para definir a variable `sc` (**sparkContext**)

``` python title="programa.py"

from pyspark.sql import SparkSession
from pyspark import SparkContext

if __name__ == '__main__':
    spark = SparkSession \
        .builder \
        .appName('My Application') \
        .getOrCreate()
    sc = spark.sparkContext
    # ...
    # Aquí vai o código do teu programa
    # ..
    spark.stop()
```

## YARN &mdash; Yet Another Resource Negotiator

Mirar os logs:
``` bash
yarn logs -applicationId [APPID]
```

Ver tódolos nodos

``` bash
yarn node -list -all
```

Finalizar unha aplicación

``` bash
yarn application -kill APP_ID
```


## jps