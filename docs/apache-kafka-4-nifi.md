# 💧 Nifi &mdash; ➿ Conexión con Apache Kafka

![Logo Apache Kafka](images/kafka/Apache_Kafka_logo.svg#derecha "Logo Apache Kafka")

Existen dous procesadores:

- **ConsumerKafka**. Permite recibir datos. Na lapela **Properties**:
    - Crear un novo **Kafka Connection Service** (se non existe)
    - **Group ID**: 1
    - **Topics**: metamorfosis

- **ProducerKafka**: Permite enviar datos. Na lapela **Properties**:
    - Crear un novo **Kafka Connection Service** (se non existe)
    - **Topic Name**: metamorfosis

Ambos precisan dun:

- **KafkaConnectionService**. Na lapela **Properties** debemos mudar:
    - **Bootstrap servers**: O nome DNS/host do servidor de Kafka. ⚠️ Ollo, se ese nome é localhost e estás noutro host, tratará de conectarse a onde estás.
