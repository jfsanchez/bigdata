# 🐘 Apache Hadoop &mdash; 🔲 Comandos

![Logo Apache Hadoop](images/hadoop/Hadoop_logo_new.svg#derecha "Logo Apache Hadoop")

[Apache Hadoop](https://hadoop.apache.org), é un [framework](https://es.wikipedia.org/wiki/Framework) que permite o procesamento distribuido de grande volume de datos sobre [clústeres de computadoras](https://es.wikipedia.org/wiki/Cl%C3%BAster_de_computadoras) empregando modelos sinxelos de programación.

O **HDFS** ou **H**adoop **D**istributed **F**ile **S**ystem é un sistema de arquivos distribuído empregado por Apache Hadoop que espalla os datos polos distintos discos dos servidores que forman o clúster de Hadoop.

- Os arquivos grandes divídense en bloques (**blocks**) por defecto de 128 MiB.

- De cada bloque hai varias copias, o número exacto establéceo o factor de replicación (**replication factor**) por defecto 3.

## Onde están os meus datos?

A primeira pregunta que debemos facernos é: Onde están os meus datos?

- No **$HOME** do teu usuario -> */home/subdirs-opcionais/usuario*.
- No **HOME** do servidor de HADOOP -> */user/usuario*.

A variable $HOME normalmente fai referencia ao teu cartafol persoal. Este adoita estar en **/home/usuario** ou en **/home/algo/mais/usuario**. Estes son os arquivos aos que accedes normalmente.

O HOME de Hadoop normalmente estará en: **/user/usuario** e para acceder a él debes empregar o comando hdfs ou ben API ou programas que se relacionen con Hadoop. A URL de acceso ao arquivo ten o formato: *hdfs://nameservice1/user/usuario/arquivo*.

## Interactuando co sistema de arquivos

O programa **hdfs** danos unha interfaz e operacións útiles para acceder ao HDFS de Hadoop. Os comandos seguen unha sintaxe de tipo:

``` bash
hdfs dfs -COMANDO # (1)!
```

1.  dfs: Indica que a operación é de arquivos sobre o sistema de arquivos.

Os comandos habituais son:

### Ver arquivos e directorios

Ver arquivos no noso HOME de HDFS. Imos ver ademáis as distintas rutas: relativas, absolutas e completas.

``` bash
hdfs dfs -ls
```

Ver arquivos que hai en "directorio" que é un directorio que está no noso HOME de HDFS:

``` bash
hdfs dfs -ls directorio
```

O mesmo que o anterior pero empregando unha ruta absoluta:

``` bash
hdfs dfs -ls /user/usuario/directorio
```

O mesmo que o anterior pero empregando a ruta absoluta e completa do HDFS:

``` bash
hdfs dfs -ls hdfs://nameservice1/user/usuario/directorio
```

### Transferindo datos entre o HDFS e o almacenamento local

🔼 **Subir**/Enviar o ARQUIVO_LOCAL que está no noso $HOME ("o noso disco duro") a un directorio de HDFS chamado "DIRECTORIO_HDFS":

``` bash
hdfs dfs -put ARQUIVO_LOCAL DIRECTORIO_HDFS
```

🔽 **Baixar**/Descargar/Recibir do HDFS ("clúster de Hadoop") o arquivo ao noso almacenamento local ("disco duro"):

``` bash
hdfs dfs -get arquivo-do-hdfs.txt
```

**Amosar** un **arquivo** do HDFS por consola **en modo texto**. Ademáis admite o formato **ZIP** e **TextRecordInputStream**:

``` bash
hdfs dfs -text arquivo.zip
hdfs dfs -text arquivo.txt
```

**Amosar un arquivo do HDFS** por consola, danos igual o formato no que estea:

``` bash
hdfs dfs -cat arquivo-calquera.xyz
```

**Ver o inicio do arquivo** (cabeceira) empregando pipes:

``` bash
hdfs dfs -cat arquivo-moi-grande.csv|head
```

Amosar a cola (o final) do arquivo. Útil para comprobar se está ben recibido e o formato.

``` bash
hdfs dfs -tail arquivo-longo.csv
```

**Copiar** un arquivo dentro do HDFS (de HDFS a HDFS)

``` bash
hdfs dfs -cp ARQUIVO_ORIXE ARQUIVO_DESTINO
```

**Mover** un arquivo dentro do HDFS (de HDFS a HDFS)

``` bash
hdfs dfs -mv ARQUIVO_ORIXE ARQUIVO_DESTINO
```
**Borrar** un arquivo do HDFS

``` bash
hdfs dfs -rm arquivo.txt
```

Resultado:

```
25/02/08 16:39:19 INFO fs.TrashPolicyDefault: Moved: 'hdfs://nameservice1/user/usuario/arquivo.txt' to trash at: hdfs://nameservice1/user/usuario/.Trash/Current/user/usuario/arquivo.txt
```

**Borrar** un arquivo do HDFS **evitando a papeleira** (skipTrash):

``` bash
hdfs dfs -rm -skipTrash arquivo.txt
```

Resultado:
```
Deleted arquivo.txt
```

### Mudando de usuario, grupo e permisos

Seguindo a [máscara de permisos UGO](https://es.wikipedia.org/wiki/Umask) podemos mudar os permisos dun arquivo ou dun directorio de forma recursiva (-R):

``` bash
hdfs dfs -chmod 765 ficheiro
```

``` bash
hdfs dfs -chmod -R 755 meudir
```

Tamén podemos mudar o propietario e o grupo do ficheiro (tamén admite -R para directorios):

``` bash
hdfs dfs -chown hadoop:hadoop ficheiro123.txt
```

Ou mudar solo o grupo:

``` bash
hdfs dfs -chgrp hadoop ficheiro321.txt
```

### É cuestión de espazo

Medir o espazo consumido non sempre é directo. Se preguntamos canto oucpa un arquivo:

``` bash
dfs dfs -du -h -s 100MB.zip
```

Veremos dous tamaños: Tamaño do arquivo e o espazo en disco consumido.

```
100 M  300 M  100MB.zip
```

O tamaño en disco consumido pódese calcular como o resultado de multiplicar o tamaño do arquivo polo factor de replicación. Pode haber diferencias debidas ao tamaño de bloque, sobre todo con tamaños de bloque grandes.

Consultar o espazo libre dispoñible:

``` bash
hdfs dfs -df -h
```


### Outros comandos útiles (probar):

Engadir (concatenar) o contido de `ventas-diarias-hoxe-LOCAL.txt` que está no **almacenamento local** (disco duro local ou $HOME) ao arquivo do **HDFS** `ventas-HDFS.txt`

``` bash
hdfs dfs -appendToFile ventas-diarias-hoxe-LOCAL.txt ventas-HDFS.txt
```

Descargar a local ao arquivo `ventas-local.txt` o resultado da concatenación dos arquivos do HDFS: `ventas-HDFS-part1.txt` e `ventas-HDFS-part2.txt`.

``` bash
hdfs dfs -getmerge -nl ventas-HDFS-part1.txt ventas-HDFS-part2.txt ventas-local.txt
```

Xerar un checksum dos datos para comprobar se están ben (emprégase MD5, non está pensado para modificacións maliciosas dos datos, senón para cambios accidentais)

``` bash
hdfs dfs -checksum ventas-HDFS.txt
```

Mudar o factor de replicación dun arquivo ou dun directorio:

``` bash
hadoop fs -setrep -w 3 100MB.zip
hadoop fs -setrep -w 3 -R /user/usuario/directorio
```

Cómo se comproba que mudou. Dúas maneiras:

Con ls, o número antes de **usuario** é o factor de replicación:

```
-rw-r--r--   **4** usuario grupo  104857600 2025-01-29 22:00 100MB.zip
```

Con du mirando que sube o espacio ocupado en disco:

``` bash
hdfs dfs -du -h -s 100MB.zip
```

Vemos que:

```
100 M  400 M  100MB.zip
```

## Arquivos de configuración

### hdfs-site.xml. Tamaño de bloque

Cada arquivo divídese en bloques (mínimo 1 bloque por arquivo) de por defecto 128 MiB.

``` xml
<property>
<name>dfs.block.size</name>
<value>134217728</value>
<property>
```


### hdfs-site.xml. Factor de replicación

O número de copias de cada bloque, por defecto 3.

``` xml
<property>
<name>dfs.replication</name>
<value>3</value>
</property>
```


## Máis información

- <https://bigdata.cesga.es/tutorials/hdfs.html>

Se empregas os recursos do [CESGA](https://www.cesga.es/), lembra que dende a casa debes conectarte á VPN antes de conectarte por SSH ao servidor hadoop.cesga.es.