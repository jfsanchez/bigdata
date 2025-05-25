# 🧾 MySQL / MariaDB
 
 ![Logo MariaDB](images/mysql-server-docker/mariadb-logo.svg#derecha "Logo MariaDB")

 - Baseado nas imaxes oficiais:
     - MySQL: <https://hub.docker.com/_/mysql>
     - MariaDB: <https://hub.docker.com/_/mariadb>

### Instalación

É recomendable crear previamente un volume cun nome para ter localizado onde temos os datos e que non se borre se executamos un `docker volume prune`.

Tamén imos crear un directorio compartido, deste xeito resultará máis fácil importar as bases de datos de proba sen ter que instalar outro cliente ou ter problemas por non estar no directorio correcto durante a importación.

``` bash
docker volume create bbddvol
mkdir -p $HOME/bd
```

Agora creamos o contedor. O volume estará asociado ao directorio coa base de datos:

⚠️ Emprega o botón copiar da dereita para que non fallen os saltos de liñas e caracteres especiais nas diferentes terminais.

=== "MySQL"

    ``` bash
    docker run -p 9906:3306 --name bbdd \
      -v bbddvol:/var/lib/mysql \
      -v $HOME/bd:/bd \
      -e MYSQL_RANDOM_ROOT_PASSWORD=1 \
      -e MYSQL_DATABASE=basededatos \
      -e MYSQL_USER=usuario \
      -e MYSQL_PASSWORD=ContrasinalMariano123. \
      --restart unless-stopped \
      -d mysql:8
    ```

=== "MariaDB"

    ``` bash
    docker run -p 9906:3306 --name bbdd \
      -v bbddvol:/var/lib/mysql \
      -v $HOME/bd:/bd \
      -e MARIADB_RANDOM_ROOT_PASSWORD=1 \
      -e MARIADB_DATABASE=basededatos \
      -e MARIADB_USER=usuario \
      -e MARIADB_PASSWORD=ContrasinalMariano123. \
      --restart unless-stopped \
      -d mariadb:latest
    ```

**Aclaracións**:

- `-p 9906:3306` redirixe o porto `9906` do anfitrión ao porto `3306` do contedor.
- `--env` ou `-e` serven para definir variables de entorno (configuración) presentes na imaxe.
- `-v` permite asociar (montar) un directorio local a un directorio de dentro do contedor. Poderíamos asociado un directorio local `/home/user/mysqldatos` ao contedor en `/var/lib/mysql` co parámetro: `-v /home/user/mysqldatos:/var/lib/mysql`. Tamén poderíamos mapear un volume anterior con: `-v ID_DO_VOLUME:/var/lib/mysql`.
- `--restart unless-stopped` Recupera no reinicio o estado do contedor (volve arrancalo) salvo que se parase explícitamente.
- `-d` Executa o contedor en modo dettached (devolve o control á consola tras a súa execución).

⚠️⚠️⚠️ **NON ESQUEZAS APUNTAR O CONTRASINAL DE ROOT**:

Para saber o contrasinal de root asignado aleatoriamente debemos buscar nos logs unha liña que conteña: `"[Note] [Entrypoint]: GENERATED ROOT PASSWORD:"`. Tras executar o contedor, dalle 20 segundos para que arranque de todo e executa:

``` bash
docker logs bbdd
```
Tamén precisaremos o enderezo IP do contedor, pódelo averiguar con:

``` bash
docker inspect bbdd
```

E buscar a liña "IPAddress": "XXX.XXX.XXX.XXX" dentro de **"NetworkSettings"** (as X son números).

Apunta nun arquivo o enderezo IP e o contrasinal de root. Vas necesitalo varias veces!

Se estás executando unha instancia ou máquina, tamén é conveniente que averigues e apuntes o seu enderezo IP.

Por último comprobamos que teñamos correctamente asociado o volume de datos ao noso contedor:

``` bash
docker ps -a --no-trunc --format "{{.Names}}: {{.Mounts}}"
```

### Recuperar instancia de MySQL co seu volume 

Se queremos recuperar unha instancia borrada, sempre e cando non borrásemos o seu volume de datos, anterior (non fai falta especificar usuarios ou contrasinais):

=== "MySQL"

    ``` bash
    docker run -p 9906:3306 --name bbdd \
      -v bbddvol:/var/lib/mysql \
      -v $HOME/bd:/bd \
      --restart unless-stopped \
      -d mysql:8
    ```

=== "MariaDB"

    ``` bash
    docker run -p 9906:3306 --name bbdd \
      -v bbddvol:/var/lib/mysql \
      -v $HOME/bd:/bd \
      --restart unless-stopped \
      -d mariadb:latest
    ```

### (CLI) Conexión directa co cliente

=== "Conectar co cliente do docker (MySQL)"

    ``` bash
    docker exec -it bbdd mysql -uusuario -pContrasinalMariano123.
    ```

    - Podemos engadir `-hX.X.X.X` para conectar con outro equipo.

=== "Conectar cun cliente doutro host (MySQL)"

    ``` bash
    mysql -hX.X.X.X -P9906 -uusuario -pContrasinalMariano123.
    ```

    - `X.X.X.X` é a IP do servidor ao que queremos conectar.

=== "Conectar co cliente do docker (MariaDB)"

    ``` bash
    docker exec -it bbdd mariadb -uusuario -pContrasinalMariano123.
    ```

    - Podemos engadir `-hX.X.X.X` para conectar con outro equipo.

=== "Conectar cun cliente doutro host (MariaDB)"

    ``` bash
    mariadb -hX.X.X.X -P9906 -uusuario -pContrasinalMariano123.
    ```

    - `X.X.X.X` é a IP do servidor ao que queremos conectar.

**Nota**: Dende consola, en caso de certos caracteres especiais, pódense escapar con barra invertida ou poñer todo o contrasinal entre comillas simples.

## (GUI) Conectar a MariaDB/MySQL con DBeaver

Se queremos conectar dende DBeaver na nosa máquina local e temos instalado o contedor de MariaDB/MySQL nunha máquina remota, tampouco debemos esquecer configurar o porto:

![Configuración DBeaver](images/mysql-server-docker/dbeaver.png "Opciones de conexión en DBeaver")

Na lapela Driver properties lembra mudar o valor de **allowPublicKeyRetrieval** a **TRUE** posto que é necesario no caso de empregar cifrado. Segundo a configuración, pode ser necesario.

Podes acceder a un manual máis detallado en [🦫 DBeaver e túneles SSH](https://jfsanchez.es/docs/dbeaver-tunel-ssh/) onde tamén aprenderás como realizar un túnel SSH. Este túnel pode ser necesario si o servidor de base de datos está detrás dun firewall.


## Comandos básicos

- Ver as bases de datos:
    ``` sql
    show databases;
    ```
- Seleccionar unha base de datos:
     ``` sql
     use database;
     ```
- Ver as táboas da BBDD actual seleccionada:
     ``` sql
     show tables;
     ```
- Ver información do estado do servidor:
    ```
    \s
    ```
- Saír do cliente. Tamén funcionaría: ```quit``` ou ```Crtl+D```:
    ```
    \q
    ```
- Executar un arquivo .sql (útil para recuperar un backup)
    ``` sql
    source /ruta/ao/arquivo.sql
    ```

## Crear usuario, BBDD e permisos

``` sql
CREATE USER 'usuario-a-crear'@'%' IDENTIFIED BY 'contrasinal-abc123.';
GRANT ALL PRIVILEGES ON base-de-datos.* TO 'usuario-a-crear'@'%';
FLUSH PRIVILEGES;
```

## Importar BBDD de proba

Debes saber o contrasinal de root (mira arriba).

Este exemplo funciona se seguiches as instruccións e hai un directorio compartido no contedor.

Descargamos dende a máquina as dúas bases de datos de proba

``` bash
cd $HOME/bd
wget https://github.com/datacharmer/test_db/releases/download/v1.0.7/test_db-1.0.7.tar.gz
wget https://downloads.mysql.com/docs/world-db.tar.gz
tar -xzf test_db-1.0.7.tar.gz
tar -xzf world-db.tar.gz
cd test_db
docker exec -it bbdd /bin/bash
```

Agora estamos dentro do docker, conectamos co cliente:

=== "MySQL"
    ``` bash
    cd /bd/test_db
    mysql -hlocalhost -uroot -p
    ```

=== "MariaDB"
    ``` bash
    cd /bd/test_db
    mariadb -hlocalhost -uroot -p
    ```

Escribe o contrasinal que tes apuntado para acceder e entrarás na consola de MySQL/MariaDB, despois executa os scripts para crear as bases de datos, os usuarios e dar permisos.

``` sql
SOURCE employees.sql
CREATE USER 'empregado'@'%' IDENTIFIED BY 'Exemplar.123';
GRANT ALL PRIVILEGES ON employees.* TO 'empregado'@'%';
SOURCE ../world-db/world.sql
CREATE USER 'mundo'@'%' IDENTIFIED BY 'MundoMundial.456';
GRANT ALL PRIVILEGES ON world.* TO 'mundo'@'%';
FLUSH PRIVILEGES;
SHOW DATABASES;
```

**Webgrafía**:

- <https://dev.mysql.com/doc/employee/en/employees-installation.html> (<https://github.com/datacharmer/test_db>)
- <https://downloads.mysql.com/docs/world-db.tar.gz>


## Backup con MySQLdump

=== "Backup dunha BBDD"

    ``` bash
    mysqldump -uUSUARIO -pCLAVE --databases BASE_DATOS > YYYY-mm-dd_mysql_backup.sql
    ```
=== "Backup de todas as BBDD"

    ``` bash
    mysqldump -uUSUARIO -pCLAVE --all-databases > YYYY-mm-dd_mysql_backup.sql
    ```

## Conectar a MySQL dende Python

- <https://github.com/jfsanchez/SBD/blob/main/notebooks/bbdd/mysql.ipynb>


⚠️ **AVISO**: Esta configuración NON pretende ser segura, o seu obxectivo é montar de xeito rápido un contorno para a aprendizaxe. Entre outras cousas deberíamos deshabilitar o usuario root para conexións remotas, borrar as BBDD de proba e impedir o acceso directo ao servidor de base de datos.

## Adicional

**Envío de arquivo a servidor remoto por scp**

Se estiveras a conectar a un servidor remoto que non permite descargar arquivos externos, deberás baixar o script en local e logo copialo ao servidor:

``` bash
scp -i chave-ssh.key employees_db-full-1.0.7.tar.gz usuario@IP-DO-SERVIDOR:/tmp/
```

**Problemas de versión (engine)**

Se estás a traballar coa versión: employees_db-full-1.0.6.tar.bz2 pode ser que teñas algún problema co **engine**. Neste caso, engadir "default_" diante das dúas liñas en employees.sql axuda. Fonte: [stackoverflow](https://stackoverflow.com/questions/36322903/error-1193-when-following-employees-database-install-tutorial-with-mysql-5-7-1).

**Porto aberto?**

En GNU/Linux podes ver qué portos están abertos con:

``` bash
netstat -atun
```

En docker podes ver as redireccións de portos don `docker inspect`.

No caso de instalación con docker, se ves que non tes aberto o 9906/9907 (segundo o exemplo) no anfitrión ou o 3306 onde teñas MySQL, probablemente debas cambiar o bind-address na configuración de MySQL ou MariaDB.

Edita o arquivo correspondente (en MySQL: /etc/mysql/mysql.conf.d/mysqld.cnf) e mete ou descomenta esta liña:

```
bind-address por 0.0.0.0
```

Ollo! Si é que non conectas ao porto 3306 pero o ves aberto, moi probablemente estea filtrado no firewall (na computación na nube ás veces filtran ese porto aínda que tí o abras explícitamente).
