from consumer import KafkaConsumerApp

if __name__ == "__main__":
    topic_names = ["test-topic-1", "test-topic-2"]
    bootstrap_servers = ['localhost:9092']  # Adjust as per your Kafka setup
    group_id = "test-group"

    consumer_app = KafkaConsumerApp(topic_names, bootstrap_servers, group_id)
    consumer_app.run()
