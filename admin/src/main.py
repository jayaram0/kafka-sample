from admin import KafkaAdminApp

if __name__ == "__main__":
    admin_app = KafkaAdminApp(servers=['localhost:9092'])
    admin_app.create_topic("test-topic-3", 3, 3)
    print("Existing topics:", admin_app.list_topics())