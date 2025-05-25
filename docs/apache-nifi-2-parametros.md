# 💧 Apache Nifi &mdash; 🎯 Parámetros e segredos

![Logo Apache Nifi](images/nifi/Apache-nifi-logo.svg#derecha "Logo Apache Nifi")

## Parámetros (Parameters) e Contextos (Parameter Context)

Un **parámetro** pode ser un usuario, servidor, contrasinal, axuste ou texto que vaiamos repetir ou queramos mudar dependendo da execución. Tes un axuste que introduces en varios sitios? Xa tes un parámetro!

Estes **parámetros** podémolos **agrupar** en **contextos** chamados **Parameter Context**.

**Propiedades** dos **contextos**:

- So podemos asociar **un** contexto por grupo de procesamento.
- Un contexto pode herdar os parámetros doutros contextos (útil para aplicar "varios" contextos a un grupo de procesamento).
- Un contexto pódese aplicar de xeito recursivo a un grupo de procesadores (ou ao principal **Nifi Flow** para que se aplique a todo).

Un **exemplo** dun parámetro é a **ruta** a onde está gardado o driver **JDBC** que se emprega na conexión a unha BBDD.

## Creando un contexto de parámetros

![Menú Apache Nifi](images/nifi/menu-principal.png#izquierda-sin-ajuste "Menú Apache Nifi")

Imos ao **Menu principal** (as tres raias horizontais de arriba á dereita) &rarr; e prememos en **Parameter Context**.

Dende esta sección da páxina prememos á dereita no botón + e introducimos:

- Lapela **Settings**:
    - **Name**: Drivers MySQL.
- Lapela **Parameters**, crearemos **dous** parámetros:
    - **Name**: **MYSQL8_JDBC**. Value: `/opt/nifi/compartido/jdbc/mysql-connector-j-8.4.0.jar`.
    - **Name**: **MYSQL9_JDBC**. Value: `/opt/nifi/compartido/jdbc/mysql-connector-j-9.2.0.jar`.
    - **Name**: **MYSQL_CLASSNAME**.Value: `com.mysql.cj.jdbc.Driver`.

## Asociando un contexto de parámetros a grupo de procesamento

Hai dúas opcións:

- Na **creación** dun grupo de procesamento: Elexiremos do despregable o **Parameter Context**.
- **Despois da creación** &rarr; Click dereito no grupo &rarr; Configure &rarr; Na lapela **Settings** escollémolo no despregable **Parameter Context**.

## Herdanza de contextos

Un **contexto de parámetros** pode herdar doutro. Por exemplo podemos ter un contexto Kafka e outro Mongo para ter os axustes de cada servidor organizados e ter outro chamado BBDD que conteña ambos.

1. Vai ao **Menu principal** &rarr; **Parameter Context**.
2. Preme no + para crear un novo contexto.
3. Lapela **Settings** &rarr; **Name**: MySQL Nifiniano.
4. Lapela **Parameters** creamos os seguintes parámetros:
    - MYSQL_SERVER: `jdbc:mysql://X.X.X.X:3306/nifi`. Substitúe X.X.X.X pola IP do teu contedor.
    - MYSQL_USER: `nifi`.
    - *MYSQL_PASSWORD*: `Nifi.Abc123`. Marca a opción: **Sensitive Value** como **Yes**.
5. Lapela **Inheritance** &rarr; Arrastramos o contexto **Drivers MySQL** da zona **Available Parameter Contexts** a **Selected Parameter Contexts**.
6. Finalmente prememos en **Apply** para gardar e pechar.

A opción de sensitive value permite dúas cousas: Por unha banda que non se exporten os segredos e por outra que nos permita poñer ese parámetro nun campo sensible (por exemplo de contrasinal).

## Empregando os parámentros nun procesador

Escolle un grupo de procesamento no que configuraras un **DBCPConnectionPool**.

Agora imos ao grupo de procesamento e prememos Click dereito &rarr; **Configure** (opcionalmente tamén click dereito &rarr; **Configure** dende dentro do grupo, nunha parte libre do Canvas).

Dentro da lapela **Settings**, en **Parameter Context** poderemos seleccionar o contexto que temos creado: **MySQL Nifiniano**. Finalmente prememos en **Apply** para gardar e pechar.

Dentro do grupo de procesamento &rarr; click dereito nunha parte libre do canvas &rarr; **Controller Services** e editamos o **DBCPConnectionPool**. Na lapela **Properties** en **Database Driver Location(s)** escribimos #{ e logo prememos Ctrl+Espacio para poder ver a lista de parámetros a seleccionar. Escollemos: `#{MYSQL8_JDBC}`.

Agora, se por calquer motivo mudamos a ruta onde gardamos o JDBC e dita ruta está en varios controis, bastaría con cambiar unha soa vez o parámetro. Ademáis, para meter esta ruta en novos controis, se nos autocompletaría.

## E agora ti...

Engade un novo contexto chamado **MongoDB** cos seguintes parámetros (obtén os datos dun servidor de mongo que teñas montado):

- MONGO_SERVER: `mongodb+srv://xxx.yyy.mongodb.net`.
- MONGO_USER: `usuario_mongo`.
- *MONGO_PASSWORD*: `Contrasinal_Mongo`.  Marca a opción: **Sensitive Value** como **Yes**.

Por último crea un contexto chamado **BBDD** onde mediante herdanza metas todos os parámetros de **MySQL** e **MongoDB**.

## Xestor de parámetros

(en elaboración)

- DatabaseParameterProvider

## Xestión de segredos

(en elaboración)

- Xestor de contrasinais: 1Password, AWS, Google Cloud...

- HashiCorpVaultParameterProvider

Mentres os parámetros podemos almacenalos en bases de datos, para os contrasinais é recomendable empregar un xestor de segredos específico, xa ben sexa un do estilo dos empregados por docker/kubernetes/etc ou un xestor de contrasinais que admita API.