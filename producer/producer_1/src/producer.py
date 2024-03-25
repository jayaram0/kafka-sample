from kafka import KafkaProducer
import json
import time


class KafkaProducerApp:
    def __init__(self, topic, servers):
        self.producer = KafkaProducer(bootstrap_servers=servers,
                                      value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        self.topic = topic

    def run(self):
        try:
            count = 0
            while True:
                count += 1
                message = {"data": "Hello Kafka I'm from Producer 1", "count": count, "timestamp": time.time()}
                self.producer.send(self.topic, value=message)
                print(f"Message sent: {message}")
                time.sleep(1)  # Simulate some data generation delay
        except KeyboardInterrupt:
            print("Stopped.")
        finally:
            self.producer.close()
