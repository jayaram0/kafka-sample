from producer2 import KafkaProducer2App

if __name__ == "__main__":
    topic_name = "test-topic-2"
    bootstrap_servers = ['localhost:9092']  # Adjust as per your Kafka setup

    producer_app = KafkaProducer2App(topic_name, bootstrap_servers)
    producer_app.run()
