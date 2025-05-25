# 🐘 Apache Hadoop &mdash; 🧾 Instalación

![Logo Apache Hadoop](images/hadoop/Hadoop_logo_new.svg#derecha "Logo Apache Hadoop")

Instalación de Apache Hadoop empregando ClusterShell

## Requisitos previos

Estas probas foron feitas nunha contorna baixo *Rocky Linux 8.5 v2* no CESGA, no seu *OpenStack*.

## Grupo de seguridade

Teremos que abrir os seguintes portos (ollo, deberíamolos abrir só entre eles e para nos, posto que deixar abertos os portos é un importante risco de seguridade):

**Xerais**:

 - SSH: 22 (TCP).

**Apache Hadoop**:

 - HADOOP_HDFS: 9000 (TCP)
 - HADDOP_MASTER_WEB: 9870 (TCP)
 - HADOOP_SECONDARY_NAMENODE_WEB 9864 (TCP) (admin)
 - HADOOP_SECONDARY_NAMENODE_WEB 9868 (TCP)

**Apache Spark**:

 - SPARK_MAIN: 9001 (TCP)
 - INFO_MASTER_SPARK: 8080 (TCP)
 - INFO_WORKERS_SPARK: 8081 (TCP)
 - INFO_WORKERS_SPARK_WEB: 4040 (TCP)
 - OUTROS: 7707 (TCP)


## Instalación de ClusterShell

Debemos instalar [ClusterShell](https://clustershell.readthedocs.io/en/latest/) no nodo master ou no equipo onde fagamos a instalación. **ClusterShell** é un programa que permite enviar á vez comandos a varias máquinas.

Executemos os comandos dende o noso equipo local ou dende o nodo master, podemos incluir o nodo master para conectarnos contra el mesmo e executar tamén nel os comandos.

### Instalación dende Rocky Linux ou distro baseada en Redhat

``` bash
sudo yum --enablerepo=extras -y install epel-release
```

``` bash
sudo yum install -y clustershell
```

### Instalación dende Linux Mint ou distro baseada en Ubuntu/Debian

``` bash
sudo apt-get install clustershell
```

## Conexión aos servidores por nome

Deberemos configurar o arquivo `/etc/hosts` cos nomes dos servidores:

~~~~ title="/etc/hosts"
X.Y.Z.T1 hadoop1 hadoop1.local
X.Y.Z.T2 hadoop2 hadoop2.local
X.Y.Z.T3 hadoop3 hadoop3.local
...
[X.Y.Z.Tn hadoopN hadoopN.local]
~~~~

Cada un destes servidores debe ter como mínimo 4 GB de RAM (8 é o mínimo recomendable máis imos aplicar restriccións na configuración).

Debemos ter creado un usuario chamado `cesgaxuser`, co que executaremos tódolos comandos. Este usuario existe por defecto nas máquinas virtuais novas creadas no OpenStack do CESGA.

Dende o nodo **master** (*hadoop1*) debemos poder conectar por SSH ao resto de nodos: *hadoop2*, *hadoop3* ... *hadoopN* (ter copiada a parte pública da chave SSH no `.ssh/authorized_keys`). Podemos xerar e meter unha chave nova no master (empregando `ssh-keygen`) ou ben copiar a chave que nos xenere o OpenStack (arquivo .pem coa chave RSA).

Se copiamos a chave RSA xerada polo OpenStack durante a creación da máquina, podemos copiala mediante scp:

Neste exemplo imaxinamos que este arquivo, gardado no directorio onde nos atopemos, chámase: `ficheiro-chave-ssh.pem`

- Copiamos o arquivo (ollo, hai que repetir o arquivo, unha vez para pasalo como chave a empregar e outra para copialo):

    ``` bash
    scp -i ficheiro-chave-ssh.pem \
      ficheiro-chave-ssh.pem cesgaxuser@hadoop1:/home/cesgaxuser/
    ```

Se nos devolve un erro coma este:

````
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0755 for 'ficheiro-chave-ssh.pem' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "ficheiro-chave-ssh.pem": bad permissions
````

Deberemos dar permisos adecuados (só podemos ler a chave nos):

``` bash
chmod 0600 ficheiro-chave-ssh.pem
```

- Conectamos co master:

    ``` bash
    ssh -i ficheiro-chave-ssh.pem cesgaxuser@hadoop1
    ```

- Dentro do master, forzaremos a creación da estrutura `.ssh` no directorio `$HOME`:

    ``` bash
    ssh localhost
    ```

Preguntaranos se queremos conectar co servidor, xa que é a primeira vez e non coñece a chave:

```
[cesgaxuser@hadoop1 ~]$ ssh localhost
The authenticity of host 'localhost (::1)' can't be established.
ECDSA key fingerprint is SHA256:5aeqrZspd4Wev7IrUFH/KS8OXORpa614OEWXRHUG+yE.
Are you sure you want to continue connecting (yes/no/[fingerprint])? 
```

Contestamos `yes` e damos a enter para que se cree a estrutura `.ssh`.

Agora toca mover a chave privada ao directorio por defecto:

``` bash
mv ficheiro-chave-ssh.pem .ssh/id_rsa
```

E dar os permisos adecuados:

``` bash
chmod 0600 .ssh/id_rsa
```

Finalmente, xeraremos a parte pública da nosa chave privada:

``` bash
ssh-keygen -y -f .ssh/id_rsa > .ssh/id_rsa.pub
```

Copiaremos as chaves do nodo master ao resto de nodos por comodidade, de xeito que poderemos enviar un comando a tódolos nodos dende calquera. Esto pode supor un risco de seguridade, mais poderemos borrar se queremos a chave privada do resto de nodos. De tódolos xeitos, tendo en conta que a configuración é a mesma en tódolos nodos e que están conectados, que logre acceder a un, moi probablemente poida acceder a todos.

No `.ssh/known_hosts` de *hadoop1*, *hadoop2* ... *hadoopN* precisamos os fingerprints de todos os servidores. Para facelo:

- Descargamos os fingerprints dos servidores (con tódalas IPs e nomes):

    ``` bash
    for servidor in $(cat /etc/hosts|grep hadoop); do \
      ssh-keyscan -H $servidor; done >> /home/cesgaxuser/.ssh/known_hosts
    ```

Se mudásemos a liña que lista os hosts por esta: `$(cat /etc/hosts|grep hadoop|awk '{print $1}'`, poderíamos asociar as chaves só os enderezos IP.

- Copiamos a configuración a tódolos nodos:

    ``` bash
    clush -l cesgaxuser -bw hadoop[2-4] \
      --copy /home/cesgaxuser/.ssh \
      --dest /home/cesgaxuser/
    ```

### Actualización de paquetes

Antes de seguir, é moi conveniente actualizar o sistema para evitar erros de seguridade. Deste xeito probamos que podemos conectar con tódolos nodos.

```
clush -l cesgaxuser -bw hadoop[1-4] sudo dnf update -y
```

(**opcional, máis recomendable**) E por comodidade, instalamos `nano` un editor moi simple e máis amigable que `vi` e tamén `net-tools` por se precisamos ver certas configuracións de rede para diagnosticar erros.

``` bash
clush -l cesgaxuser -bw hadoop[1-4] sudo dnf install -y nano net-tools
```


### Instalación de Java OpenJDK Correto de Amazon

En tódolos equipos debemos ter instalada a máquina virtual de Java OpenJDK versión Corrreto de Amazon a través de repositorio. 

Tes as instruccións máis detalladas e con explicacións en: [Java/Amazon Corretto/OpenJDK](amazon-corretto-java-0-instalacion.md)

Engadimos o respositorio:

``` bash
clush -l cesgaxuser -bw hadoop[1-4] \
  sudo curl -L -o /etc/yum.repos.d/corretto.repo \
  https://yum.corretto.aws/corretto.repo
```

Instalamos o paquete:

``` bash
clush -l cesgaxuser -bw hadoop[1-4] \
  sudo dnf install -y java-11-amazon-corretto-devel`
```


## Configuración do **nodo master**
Debemos conectarnos por SSH ao nodo master:

``` bash
ssh cesgaxuser@hadoop1
```

### Configuración de JAVA_HOME en tódolos servidores

Editaremos o arquivo `/home/cesgaxuser/.bashrc` para configurar as variables de contorna necesarias.

``` bash
nano .bashrc
```

Metemos esta liña ao final:

``` bash title=".bashrc"
export JAVA_HOME='/usr/lib/jvm/java-11-amazon-corretto/'
```

Esto configura a variable de contorna `JAVA_HOME`. Non debería ser necesario ao estar instalada a máquina dende un repositorio automatizado, pero é unha boa práctica para que o resto de scripts non dean fallos ou avisos.

Pechamos a sesión (Ctrl+D) e volvemos entrar (ou executamos `. ./bashrc` ou `source .bashrc` para recargar as variables de entorno).

Copiamos este arquivo ao resto de nodos, empregaremos *clustershell* para simplificar o proceso:

``` bash
clush -l cesgaxuser -bw hadoop[2-4] --copy .bashrc --dest /home/cesgaxuser/
```


### Descargando e instalando Apache Hadoop en tódolos nodos

No nodo master, **descargamos** *Apache Hadoop* da web oficial:

```
curl https://dlcdn.apache.org/hadoop/common/hadoop-3.2.4/hadoop-3.2.4.tar.gz \
  --output hadoop-3.2.4.tar.gz
```

E **copiámolo** ao resto de nodos:

``` bash
clush -l cesgaxuser -bw hadoop[2-4] \
  --copy hadoop-3.2.4.tar.gz --dest /home/cesgaxuser/
```

**Descomprimimos** en tódolos nodos:

``` bash
clush -l cesgaxuser -bw hadoop[1-4] 
  tar -xzf hadoop-3.2.4.tar.gz
```

### Configurando as variables de contorna específicas de **Apache Hadoop**

Metemos no `.bashrc` ao final as seguintes novas variables da contorna:

``` bash title=".bashrc"
export HADOOP_HOME='/home/cesgaxuser/hadoop-3.2.4'
export PATH=${PATH}:${HADOOP_HOME}/bin:${HADOOP_HOME}/sbin
```

E copiamos o arquivo ao resto de nodos para aplicar a mesma configuración:

``` bash
clush -l cesgaxuser -bw hadoop[2-4] \
  --copy .bashrc --dest /home/cesgaxuser/
```

Pechamos a sesión (Ctrl+D) e volvemos entrar (ou executamos `. ./bashrc` ou `source .bashrc` para recargar as variables de entorno).

Para comprobar se funciona a instalación básica e as variables de contorna, podemos escribir o comando:

```
hdfs
```

E debería devolvernos a axuda do comando.

### Configurando Apache Hadoop

Editamos os arquivos de configuración seguintes e os deixamos así:

``` xml title="hadoop-3.2.4/etc/hadoop/core-site.xml"
    <configuration>
        <property>
            <name>fs.default.name</name>
            <value>hdfs://hadoop1:9000</value>
        </property>
    </configuration>
```

``` xml title="hadoop-3.2.4/etc/hadoop/hdfs-site.xml"
    <configuration>
        <property>
            <name>dfs.namenode.name.dir</name>
            <value>/home/cesgaxuser/data/nameNode</value>
        </property>

        <property>
            <name>dfs.datanode.data.dir</name>
            <value>/home/cesgaxuser/data/dataNode</value>
        </property>

        <property>
            <name>dfs.replication</name>
            <value>1</value>
        </property>
    </configuration>
```

``` xml title="hadoop-3.2.4/etc/hadoop/mapred-site.xml"
    <configuration>
        <property>
            <name>mapreduce.framework.name</name>
            <value>yarn</value>
        </property>
        <property>
            <name>yarn.app.mapreduce.am.env</name>
            <value>HADOOP_MAPRED_HOME=$HADOOP_HOME</value>
        </property>
        <property>
            <name>mapreduce.map.env</name>
            <value>HADOOP_MAPRED_HOME=$HADOOP_HOME</value>
        </property>
        <property>
            <name>mapreduce.reduce.env</name>
            <value>HADOOP_MAPRED_HOME=$HADOOP_HOME</value>
        </property>
    
    <!-- Límite de uso de RAM (non poñer se temos alomenos 8GB por servidor -->

    <property>
        <name>yarn.app.mapreduce.am.resource.mb</name>
        <value>512</value>
    </property>

    <property>
        <name>mapreduce.map.memory.mb</name>
        <value>256</value>
    </property>

    <property>
        <name>mapreduce.reduce.memory.mb</name>
        <value>256</value>
    </property>

    </configuration>
```

No seguinte arquivo lembra substituir XXX.XXX.XXX.XXX pola IP do nodo master ou mellor polo host: **hadoop1**:

``` xml title="hadoop-3.2.4/etc/hadoop/yarn-site.xml"
    <configuration>
        <property>
            <name>yarn.acl.enable</name>
            <value>0</value>
        </property>

        <property>
            <name>yarn.resourcemanager.hostname</name>
            <value>XXX.XXX.XXX.XXX</value>
        </property>

        <property>
            <name>yarn.nodemanager.aux-services</name>
            <value>mapreduce_shuffle</value>
        </property>

        <!-- Límite de uso de RAM (non poñer se temos +8GB por servidor -->
        <property>
            <name>yarn.nodemanager.resource.memory-mb</name>
            <value>1536</value>
        </property>
        
        <property>
            <name>yarn.scheduler.maximum-allocation-mb</name>
            <value>1536</value>
        </property>
    
        <property>
            <name>yarn.scheduler.minimum-allocation-mb</name>
            <value>128</value>
        </property>
    
        <property>
            <name>yarn.nodemanager.vmem-check-enabled</name>
            <value>false</value>
        </property>

    </configuration>
```

E tamén metemos os nodos que queiramos que fagan de workers no arquivo:

``` title="hadoop-3.2.4/etc/hadoop/workers"
hadoop1
hadoop2
hadoop3
hadoop4
```

Agora precisamos crear os directorios que almacenarán os datos:

``` bash
mkdir -p /home/cesgaxuser/data/nameNode
mkdir -p /home/cesgaxuser/data/dataNode
```


Con esto teríamos configurado **yarn** en *hadoop1* (master).

### Configuración do resto de nodos

Podemos copiar simplemente a configuración ao resto de nodos:

``` bash
clush -l cesgaxuser -bw hadoop[2-4] \
  --copy hadoop-3.2.4/etc/hadoop/workers \
  hadoop-3.2.4/etc/hadoop/yarn-site.xml \
  hadoop-3.2.4/etc/hadoop/mapred-site.xml \
  hadoop-3.2.4/etc/hadoop/hdfs-site.xml \
  hadoop-3.2.4/etc/hadoop/core-site.xml \
  --dest /home/cesgaxuser/hadoop-3.2.4/etc/hadoop
```

### Formatear o HDFS:

Dende *hadoop1* (o nodo master) executamos:

``` bash
hdfs namenode -format
```

E finalmente dende o master iniciamos todo o sistema (esto conecta por SSH aos nodos e executa os comandos necesarios para que se poñan a traballar):

``` bash
start-dfs.sh
start-yarn.sh
```

### Arrancando Apache Hadoop ao inicio con cron

Se queremos lanzar o proceso de Apache Hadoop dende cron (por exemplo para facer uso da opción `@reboot`) deberemos cambiar por si acaso o arquivo: `hadoop-3.2.4/etc/hadoop/hadoop-env.sh` e mudar as seguintes variables, para non depender do .bashrc do usuario:


``` bash title="hadoop-3.2.4/etc/hadoop/hadoop-env.sh"
    export JAVA_HOME='/usr/lib/jvm/java-11-amazon-corretto/'
    export HADOOP_HOME='/home/cesgaxuser/hadoop-3.2.4'
    export HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop
    #HADOOP_OPTS=
```

Unha vez cambiemos o arquivo, copiarémolo ao resto de nodos, por coherencia e por manter igual a configuración en tódolos sitios.

``` bash
clush -l cesgaxuser -bw hadoop[2-4] \
  --copy hadoop-3.2.4/etc/hadoop/hadoop-env.sh \
  --dest /home/cesgaxuser/hadoop-3.2.4/etc/hadoop
```

Finalmente editaremos o cron do nodo master para indicarlle que arranque Hadoop cando iniciemos a máquina:

(**importante**: *Se non queres empregar vi, establece a variable `EDITOR=nano` se o tes instalado*)

 ``` bash
 crontab -e
 ```

E metemos no arquivo o seguinte contido:

```
@reboot /home/cesgaxuser/hadoop-3.2.4/sbin/start-dfs.sh
@reboot /home/cesgaxuser/hadoop-3.2.4/sbin/start-yarn.sh
```

Por último reiniciamos tódolos nodos:

```
clush -l cesgaxuser -bw hadoop[1-4] sudo reboot
```

### Comprobando que funciona

Para obter información do HDFS, podemos empregar o comando:

``` bash
hdfs dfsadmin -report
```

Queda iniciar yarn.

## Bibliografía

Podes atopar máis información:

 - <https://www.linode.com/docs/guides/how-to-install-and-set-up-hadoop-cluster/>
 - <https://sparkbyexamples.com/spark/spark-setup-on-hadoop-yarn/>
 - <https://www.linode.com/docs/guides/install-configure-run-spark-on-top-of-hadoop-yarn-cluster/>
 - <https://www.tutorialspoint.com/es/hadoop/hadoop_multi_node_cluster.htm>
 - <https://hadoop.apache.org/docs/r3.0.0/hadoop-project-dist/hadoop-hdfs/hdfs-default.xml>

## Copyright

© 2023 - Jose Sánchez

Se atopas erros, agradecerei que me envíes un email/mensaxe co aviso ou as correccións.
