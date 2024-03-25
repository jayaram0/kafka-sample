from kafka import KafkaConsumer
import json


class KafkaConsumerApp:
    def __init__(self, topic, servers, group_id):
        self.consumer = KafkaConsumer(group_id=group_id,
                                      bootstrap_servers=servers,
                                      auto_offset_reset='earliest',
                                      value_deserializer=lambda x: json.loads(x.decode('utf-8')))
        print("Consumer initialized.")
        print(f"Subscribing to topic: {topic}")
        self.consumer.subscribe(topics=topic)
        print("Subscribed")

    def run(self):
        try:
            for message in self.consumer:
                print(f"Received message: {message.value}")
        except KeyboardInterrupt:
            print("Stopped.")
        finally:
            self.consumer.close()
