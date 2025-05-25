# 🐘 Apache Hadoop &mdash; 🧮 Exemplo contapalabras

![Logo Apache Hadoop](images/hadoop/Hadoop_logo_new.svg#derecha "Logo Apache Hadoop")

Imos empregar o **.jar** de exemplo para demostrar a operación de mapreduce contando palabras sobre un arquivo presente no HDFS.

Este arquivo **.jar** de exemplo podémolo executar directamente en Apache Hadoop:

- `/opt/cloudera/parcels/CDH-6.1.1-1.cdh6.1.1.p0.875250/jars/hadoop-mapreduce-examples-3.0.0-cdh6.1.1.jar`

**Preparando o contorno**

1. Creamos un arquivo coa lista da compra:

    ``` bash title="$HOME/lista_compra.txt"
    echo "Ovos, leite, pan, pan, ovos, aceite, sal, ovos, leite, carne, peixe, fariña, pan raiao, ovos, leite fariña." > lista_compra.txt
    ``` 

2. Creamos o directorio `compras` no **HDFS** e subimos o arquivo ese directorio:
    ```
    hdfs dfs -mkdir compras
    hdfs dfs -put lista_compra.txt compras/
    ```

3. Comprobamos que temos subido correctamente o arquivo:
    ```
    hdfs dfs -ls compras
    ```

4. Executamos o comando `yarn jar` con estes parámetros:
    ```
    yarn jar \
        /opt/cloudera/parcels/CDH-6.1.1-1.cdh6.1.1.p0.875250/jars/hadoop-mapreduce-examples-3.0.0-cdh6.1.1.jar \
        wordcount compras resumo_compras
    ```

Debería terse creado en `resumo_contas` o conteo de palabras dos arquivos que estivesen dentro do directorio `compras`.