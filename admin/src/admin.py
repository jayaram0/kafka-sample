from kafka.admin import KafkaAdminClient, NewTopic

class KafkaAdminApp:
    def __init__(self, servers):
        self.admin_client = KafkaAdminClient(bootstrap_servers=servers)

    def create_topic(self, topic_name, num_partitions, replication_factor):
        topic = NewTopic(name=topic_name, num_partitions=num_partitions, replication_factor=replication_factor)
        self.admin_client.create_topics(new_topics=[topic], validate_only=False)
        print(f"Topic {topic_name} created.")

    def list_topics(self):
        return self.admin_client.list_topics()