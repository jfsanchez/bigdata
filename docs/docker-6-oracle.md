# 🧾 Oracle Free

⚠️ **AVISO:** Apuntes en elaboración. Incompletos.

 - Baseado en: <https://www.oracle.com/es/database/free/get-started/>

## 1. Instalación

### 1.1. Baixar a imaxe

``` bash
docker pull container-registry.oracle.com/database/free:latest
```

### 1.2. Executar o contenedor

``` bash
docker run -p 5560:5560 -d --name oracle_free \
    container-registry.oracle.com/database/free
```

## 2. Conexión

``` bash
docker exec -it oracle_free sqlplus / as sysdba
```

Para conectar a Oracle, dependendo se o temos instalado directamente ou nun docker, podemos empregar os seguintes comandos.

### 3. Comandos para conexión directa:

``` bash
sqlplus sys@localhost:1521/FREEPDB1 as sysdba
sqlplus sys@localhost:1521/FREE as sysdba
```

### 4. Comandos para docker:

``` bash
docker exec -it dbname sqlplus / as sysdba
docker exec -it dbname sqlplus sys/cdb-user-password@cdb-sid as sysdba
docker exec -it dbname sqlplus system/cdb-user-password@cdb-sid
docker exec -it dbname sqlplus pdbadmin/pdb-user-password@pdbname
```

### 5. Exemplo de creación de usuario e asignación de permisos

``` sql
CREATE USER oraclefreeuser
  IDENTIFIED BY Abc12300 
  DEFAULT TABLESPACE tablespace
  TEMPORARY TABLESPACE tbs_temp_01
  QUOTA UNLIMITED on tablespace;
```

``` sql
GRANT CREATE VIEW, CREATE PROCEDURE,
    CREATE SEQUENCE, CREATE TRIGGER to oraclefreeuser;

GRANT ALTER ANY TABLE to oraclefreeuser;
GRANT ALTER ANY PROCEDURE to oraclefreeuser;
GRANT ALTER ANY TRIGGER to oraclefreeuser;
GRANT DELETE ANY TABLE to oraclefreeuser;
GRANT DROP ANY PROCEDURE to oraclefreeuser;
GRANT DROP ANY TRIGGER to oraclefreeuser;
GRANT DROP ANY VIEW to oraclefreeuser;
GRANT CREATE TABLE to oraclefreeuser;
```

- Máis información sobre a creación de usuarios: <https://blog.devart.com/how-to-create-oracle-user.html>

## 6. Conexión dende Python

``` py title="oracle.py"
import oracledb

conn = oracledb.connect(user="[Username]", password="[Password]", \
                             dsn="localhost:1521/FREEPDB1")
with conn.cursor() as cur:
   cur.execute("SELECT 'Hello World!' FROM dual")
   res = cur.fetchall()
   print(res)
```


## 7. Limitacións de Oracle Free:

- Uso máximo de memoria RAM: 2 GB
- Cores que emprega como máximo: 2
- Tamaño máximo de BD: 12 GB
- Unha soa instancia por medio lóxico.
   

## 8. Máis información:

- <https://www.oracle.com/es/database/free/get-started/>
- <https://docs.oracle.com/en/database/oracle/oracle-database/21/deeck/index.html>
- <https://docs.oracle.com/en/database/oracle/oracle-database/23/xeinl/licensing-restrictions.html>
