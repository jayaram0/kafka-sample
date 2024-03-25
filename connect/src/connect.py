from kafka import KafkaProducer, KafkaConsumer


class KafkaConnectApp:
    def __init__(self, topic, servers):
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers=servers)
        self.consumer = KafkaConsumer(topic, bootstrap_servers=servers)

    def simulate_external_system_producer(self, message):
        # Simulate sending data to Kafka from an external system
        self.producer.send(self.topic, message.encode('utf-8'))

    def simulate_external_system_consumer(self):
        # Simulate consuming data from Kafka to an external system
        for msg in self.consumer:
            print(f"Received: {msg.value.decode('utf-8')}")
