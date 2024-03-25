from kafka import KafkaConsumer, KafkaProducer


class KafkaStreamApp:
    def __init__(self, input_topic, output_topic, servers):
        self.output_topic = output_topic
        self.consumer = KafkaConsumer(input_topic, bootstrap_servers=servers)
        self.producer = KafkaProducer(bootstrap_servers=servers)

    def process_messages(self):
        try:
            for message in self.consumer:
                # Simulate some processing logic
                processed_value = message.value.upper()  # Example: convert messages to uppercase
                self.producer.send(self.output_topic, processed_value)
                print(f"Processed and sent: {processed_value}")
        except KeyboardInterrupt:
            print("Stopped.")
        finally:
            self.consumer.close()
            self.producer.close()
# Path: stream/src/stream.py
