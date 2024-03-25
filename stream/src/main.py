from stream import KafkaStreamApp

if __name__ == "__main__":
    stream_app = KafkaStreamApp(input_topic="test-topic", output_topic="processed-topic", servers=['localhost:9092'])
    stream_app.process_messages()