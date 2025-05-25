# ➿ Apache Kafka &mdash; 🐳 Instalación

![Logo Apache Kafka](images/kafka/Apache_Kafka_logo.svg#derecha "Logo Apache Kafka")

- Baseado na imaxe oficial: <https://hub.docker.com/r/apache/kafka>

## Crear o contedor

Lanzamos un novo contedor **brokerkafkiano** que escoita no porto 9092.

``` bash
docker run -d  \
  --name brokerkafkiano \
  --hostname brokerkafkiano.local \
  -p 9092:9092 -p 9093:9093 \
  -e KAFKA_NODE_ID=1 \
  -e KAFKA_PROCESS_ROLES=broker,controller \
  -e KAFKA_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 \
  -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://brokerkafkiano.local:9092 \
  -e KAFKA_CONTROLLER_LISTENER_NAMES=CONTROLLER \
  -e KAFKA_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT \
  -e KAFKA_CONTROLLER_QUORUM_VOTERS=1@brokerkafkiano.local:9093 \
  -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 \
  -e KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR=1 \
  -e KAFKA_TRANSACTION_STATE_LOG_MIN_ISR=1 \
  -e KAFKA_GROUP_INITIAL_REBALANCE_DELAY_MS=0 \
  -e KAFKA_NUM_PARTITIONS=3 \
  --restart unless-stopped \
  apache/kafka:latest
```

⚠️ O nome **brokerkafkiano.local** debería ser cambiado por un nome DNS ou nome presente no `etc/hosts` que se resolvese ben dende tódolos sitios que conecten con Kafka.


## Crear un topic

Empregando o script `kafka-topics.sh` crearemos o topic (tema) **metamorfosis**.

``` bash
docker exec -it brokerkafkiano \
  /opt/kafka/bin/kafka-topics.sh \
  --bootstrap-server brokerkafkiano.local:9092 \
  --create --topic metamorfosis
```

## Escribir mensaxes ao topic (produtor)

Imos escribir unha serie de mensaxes no produtor, aínda que ninguén estea suscrito ao topic consumindo estes datos. Para lanzar un produtor (enviar datos a Kafka) empregamos o producer de consola de dentro do contedor:

``` bash
docker exec -it brokerkafkiano \
	/opt/kafka/bin/kafka-console-producer.sh \
  	--bootstrap-server brokerkafkiano.local:9092 \
	--topic metamorfosis
```
Agora poderemos escribir algúns textos, por exemplo:

```
Hola Mundo!
Clave=Valor
1234567890
abc
```

Se queremos sair da consola, premeremos Ctrl+C.

## Recibir mensaxes do topic (consumidor)

Os datos anteriores seguen en Kafka e podemos ter acceso ao topic dende o inicio do mesmo:

``` bash
docker exec --interactive -it brokerkafkiano \
	/opt/kafka/bin/kafka-console-consumer.sh \
	--bootstrap-server brokerkafkiano.local:9092 \
	--topic metamorfosis \
	--from-beginning
```

Se deixamos aberta esta consola e noutra lanzamos un produtor que envíe datos ao **metamorfosis**, deberían reflectirse nesta primeira consola en pouco tempo.


## Ligazóns a máis información

### Descargas oficiais do software
- <http://kafka.apache.org>
- <https://hub.docker.com/r/apache/kafka>

### Configuración de autenticación e cifrado
- <https://kafka.apache.org/documentation/#security_authz>
- Titorial (non probado): <https://www.baeldung.com/ops/kafka-authentication-topics-sh>
