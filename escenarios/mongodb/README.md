# Escenario Vagrant para MongoDB
Este escenario instala y configura mongodb en una máquina Ubuntu y carga automáticamente un dataset de ejemplo en JSON.

## Características de la máquina

* **RAM**: 2 GiB
* **Box**: ubuntu/focal64 (20.04 LTS)
* **Puerto**: 27017 expuesto al anfitrión
* **Nombre**: bigiamongodb
* **Preparado para**: Virtual Box (con vagrant)

Existe comentada una versión para el box xenial64.

## Características del dataset de pruebas
Este escenario es para pruebas con MongoDB, se emplean como ejemplo algunos datos de COVID de Italia en formato JSON.

Descargado de: <https://www.kaggle.com/datasets/paultimothymooney/coronavirus-in-italy>

Licencia: CC-BY-4.0. <https://github.com/pcm-dpc/COVID-19/blob/master/LICENSE>

## Cómo empezar
Sitúate en este directorio (donde está este archivo).

Puedes lanzar la máquina con:
 `vagrant up`

Puedes pararla con:
 `vagrant halt`
 
Puedes entrar en ella con:
 `vagrant ssh`

Puedes borrarla con:
 `vagrant destroy`

El borrado sólo actúa sobre la máquina en VIrtual Box y no sobre las imágenes descargadas.

# Ejemplos de comandos

El escenario para vagrant ya importa la base de datos y expone al anfitrión el puerto por defecto de mongodb.

Está pensado para su uso con Virtual Box.

Sólo hay que clonar el repositorio, situarse en este directorio y hacer vagrant up.

## Conectar a mongo
 `mongosh --host IP-del-host`

## Import de la base de datos
 `gunzip /vagrant/dpc-covid19-ita-province.json.gz`

 `mongoimport --db covid --collection coviditalia --file /vagrant/dpc-covid19-ita-province.json --jsonArray`

## Volcado/Dump de la base de datos
 `mongodump --host localhost:27017 --gzip --db covid --out /vagrant/dbs`

## Restaurar/Restore la base de datos
 `mongorestore --host localhost:27017 --gzip --db covid /vagrant/dbs/covid`

## Comandos de búsqueda

### Desde consola
Con mongosh (con mongo es el mismo ejemplo):

 `mongosh covid --eval "db.coviditalia.find().pretty()`

 `mongosh covid --eval "db.coviditalia.find({"codice_provincia" : 979}).pretty()"`

### Desde mongo
1) Entrar en mongo: mongosh (o mongo en versiones anteriores)

`use covid;`

`db.coviditalia.find({"codice_provincia" : 979})`

2) Para salir:

Desde mongosh: `quit`

Desde mongo: `quit();`

## Borrar/Drop la base de datos (desde mongosh)
`use covid;`

`db.dropDatabase()`

## Resto de comandos CRUD
Se dan como ejemplo de sintaxis, pueden no funcionar según los datos presentes.

### Inserción/Insert:
**Desde shell:**
`mongosh covid --eval "db.coviditalia.insertOne({ codice_regione: '99999', totale_casi: 999999999, stato: 'ITA' })"`

**Desde mongosh**
`db.coviditalia.insertOne({'codice_regione': '99999', 'totale_casi': '999999999', 'stato': 'ITA'})`

### Búsqueda de un registro por valor
**Desde shell**
`mongosh covid --eval "db.coviditalia.find({ 'totale_casi': 999999999}).pretty()"`

**Desde mongosh**

`db.coviditalia.find({'codice_provincia': 110, 'data': '2020-04-03T17:00:00'}).pretty()`

`db.coviditalia.find({ 'totale_casi': 999999999}).pretty()`

### Actualización/Update
**Desde shell**
`mongosh covid --eval "db.coviditalia.updateOne({ 'codice_regione': 99999 }, { \$set: { 'codice_regione': 199999 } })"`

**Desde mongosh**
`db.coviditalia.updateOne({ 'codice_regione': 99999 }, { $set: { 'codice_regione': 199999 } })`

### Borrado/Delete
**Desde shell**
`mongosh covid --eval "db.coviditalia.deleteOne({'codice_regione': '99999', 'totale_casi': '999999999', 'stato': 'ITA'})"`

**Desde mongosh**
`db.coviditalia.deleteOne({'codice_regione': '99999', 'totale_casi': '999999999', 'stato': 'ITA'})`

