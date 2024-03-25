from consumer import KafkaConsumerApp

if __name__ == "__main__":
    topic_name = "test-topic-1"
    bootstrap_servers = ['localhost:9092']  # Adjust as per your Kafka setup
    group_id = "test-group"

    consumer_app = KafkaConsumerApp(topic_name, bootstrap_servers, group_id)
    consumer_app.run()
