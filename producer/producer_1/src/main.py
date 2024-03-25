from producer import KafkaProducerApp

if __name__ == "__main__":
    topic_name = "test-topic-1"
    bootstrap_servers = ['localhost:9092']  # Adjust as per your Kafka setup

    producer_app = KafkaProducerApp(topic_name, bootstrap_servers)
    producer_app.run()
