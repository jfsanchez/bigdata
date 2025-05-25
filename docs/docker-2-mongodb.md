# 🧾 MongoDB

![Logo MongoDB](images/mongodb/MongoDB_Logomark_SpringGreen.svg#derecha "Logo MongoDB")

 - Baseado na imaxe oficial: <https://hub.docker.com/_/mongo>

 - Se queres [instalar mongo en modo replica set ou sharded cluster, consulta a presentación](/docencia/mongodb#instalacionpro).

## Introdución

Podemos executar MongoDB de tres modos diferentes:

- **Standalone server**: Un só servidor, útil para *desenvolvemento e probas*.
- **Replica set** (ou cluster simple): Útil en *produción*, varias instancias de servidor en execución. Engade redundancia e dispoñibilidade (escalado horizontal).
- **Sharded cluster**: Útil en *produción*, varias instancias de servidor en execución. Engade a posibilidade de particionar os datos. Permite un manexo de alto volume de datos e operacións.

Non confundamos estes modos de operación coa licencia ou version de mongo:

- **Community**: Gratuita.
- **Enterprise**: Versión comercial con soporte e optimizacións. Gratuita para desenvolvemento.
- **Atlas**: Versión na nube. Gratuita ata 512MB.

## Instalación en modo standalone server (simple):

- **Instalación**:

    ``` bash
    docker run -d --name mongo \
      -e MONGO_INITDB_ROOT_USERNAME=mongoadmin \
      -e MONGO_INITDB_ROOT_PASSWORD=abc123Secret \
      -p 27017:27017 \
      mongo
    ```

- **Conexión con parámetros**:

    ``` bash
    docker exec -it mongo \
    mongosh --host localhost --port 27017 --apiVersion 1 \
    --username mongoadmin --password abc123Secret
    ```

- **Conexión con URL**:

    ``` bash
    docker exec -it mongo mongosh \
      "mongodb://mongoadmin:abc123Secret@localhost:27017/?directConnection=true&serverSelectionTimeoutMS=2000"
    ```

No docker de instalación, podes mapear un cartafol co host para ver como almacena mongo os datos coa opción: `-v /root/mongo:/data/db`, máis o recomendado é gardar os datos nun volume.

**Webgrafía**:

- <https://hub.docker.com/_/mongo>
- <https://www.mongodb.com/docs/mongodb-shell/connect/>


## Conexión a mongodb (cliente)

Estas instrucción son só no caso de querer instalar o cliente en local. Lembremos que sempre podemos conectar co cliente mongosh de dentro do contedor.

Instruccións para GNU/Linux Debian 12 Bookworm:

1. Instalación de dependencias:
    ``` bash
    sudo apt-get install gnupg curl
    ```

2. Baixar a chave GNUpg que firma os paquetes do repositorio:

    ``` bash
    curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | \
     sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
     --dearmor
    ```

3. Engadir o novo repositorio:

    ``` bash
    echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] http://repo.mongodb.org/apt/debian bookworm/mongodb-org/7.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
    ```

4. Actualizar a información de paquetes dos repositorios:

    ``` bash
    sudo apt-get update
    ```

5. Instalar os paquetes:

    ``` bash
    sudo apt-get install -y mongodb-org
    ```

Coidado co ulimit! O número de arquivos abertos máximos debe ser superior a 64.000.

**Webgrafía**:
- <https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-debian/>

### (GUI) Conectar con Compass

Compass é un cliente gráfico gratuito oficial que nos permite conectar con Mongo e mesmo ver algunhas estatísticas do servidor. Debido a que mongodb é amplamente empregado no mundo empresarial, moitos clientes de base de datos que teñen versión community soen ser de pago con mongo (exemplo: DBeaver).

Podes baixar compass da súa páxina oficial:
- <https://www.mongodb.com/products/tools/compass>

E para conectar, podes empregar a cadea de conexión:

`mongodb://mongoadmin:abc123Secret@localhost:27017/?directConnection=true&serverSelectionTimeoutMS=2000`

Lembra premer no botón de "Save and connect" para gardar a conexión co usuario e contrasinal á esquerda e non ter que volver introducilos manualmente (ou ter que introducir a cadea de conexión que tamén inclúe eses datos).

### Conectar contra Atlas (servidor na nube)

#### (CLI) Mongosh contra atlas

- Chamamos á consola mongosh cos parámetros:

    ``` bash
     mongosh "mongodb+srv://.../" --apiVersion 1 --username USUARIO
    ```

#### (CLI) Cliente Atlas

- Instalación:

    ``` bash
    sudo apt install mongodb-atlas-cli
    ```

- Iniciar sesión:

    ``` bash
    atlas auth login
    ```

## Lecturas complementarias

- [Apuntes de MongoDB en formato presentación](https://jfsanchez.es/docencia/mongodb/)
- [Conectar a MongoDB dende Python (notebook)](https://github.com/jfsanchez/SBD/blob/main/notebooks/bbdd/mongodb.ipynb)
- [Como securizar un servidor mongo accesible en internet (inglés, páxina oficial)](https://www.mongodb.com/docs/manual/administration/security-checklist/#std-label-security-checklist)

## Creando un cluster/replica set de mongo en docker

Fai falta seguir uns pasos lóxicos: Crear una nova rede en docker para que se comuniquen os contedores entre eles, executar alomenos tres contedores de mongo asociados a esa rede e finalmente facer que se unan entre eles nun replica set.

### Crear a rede en docker

Como en calquer caso, creamos unha nova rede cun nome que nos guste:

``` bash
docker network create mongoReplicado
```

### Lanzar os contedores

``` bash
docker run -d -p 27017:27017 --name mongoVermello --network mongoReplicado mongo mongod --replSet replicados --bind_ip localhost,mongoVermello
docker run -d -p 27027:27017 --name mongoVerde --network mongoReplicado mongo mongod --replSet replicados --bind_ip localhost,mongoVerde
docker run -d -p 27037:27017 --name mongoAzul --network mongoReplicado mongo mongod --replSet replicados --bind_ip localhost,mongoAzul
```

Os portos redirixidos do anfitrión ao contedor van ser os seguintes:

- 27017: mongoVermello (o por defecto)
- 27027: mongoVerde
- 27037: mongoAzul

### Unir os servidores

``` bash
docker exec -it mongoVermello mongosh --eval "rs.initiate({
 _id: \"replicados\",
 members: [
   {_id: 0, host: \"mongoVermello\"},
   {_id: 1, host: \"mongoVerde\"},
   {_id: 2, host: \"mongoAzul\"}
 ]
})"
```

### Probar que estean funcionando en modo replica set

``` bash
docker exec -it mongoVermello mongosh --eval "rs.status()"
```

E se paramos o "principal":

``` bash
docker stop mongoVermello
``` 

E consultamos os outros, todo debería seguir funcionando igual, os datos seguen dispoñibles:

``` bash
docker exec -it mongoVerde mongosh --eval "rs.status()"
docker exec -it mongoAzul mongosh --eval "rs.status()"
```


**Webgrafía:**

- <https://www.mongodb.com/resources/products/compatibilities/deploying-a-mongodb-cluster-with-docker>
- <https://www.mongodb.com/docs/manual/tutorial/convert-standalone-to-replica-set/>
- <https://www.mongodb.com/docs/manual/reference/replica-configuration/#std-label-replica-set-configuration-document>

## Conversión do Replica Set a Sharded Cluster

O principal obxectivo deste tipo de configuración é ter particionado os datos cunha [shard key](https://www.mongodb.com/docs/manual/core/sharding-choose-a-shard-key/#std-label-sharding-shard-key-selection).

Hai un titorial na web oficial de mongodb sobre como pasar dun replica set (con autenticación habilitada) a un sharded cluster:

- <https://www.mongodb.com/docs/manual/tutorial/convert-replica-set-to-replicated-shard-cluster/>



