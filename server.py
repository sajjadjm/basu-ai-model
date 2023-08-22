import pika, model, time, os

crendtials = pika.PlainCredentials(
    os.environ.get("BROKER_USERNAME"), os.environ.get("BROKER_PASSWORD")
)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=os.environ.get("BROKER_HOST"),
        port=os.environ.get("BROKER_PORT"),
        credentials=crendtials,
    )
)

ch = connection.channel()

ch.queue_declare(queue="data_stream")


def callback(ch, method, properties, body):
    # Converting b'string to normal string
    data = string_to_list(body.decode("ascii"))
    print("Model is working on your data...")

    try:
        time.sleep(10)
        Model_Prediction = model.predict(data)
        ch.basic_publish(
            exchange="",
            routing_key=properties.reply_to,
            properties=pika.BasicProperties(correlation_id=properties.correlation_id),
            body=str(Model_Prediction),
        )

        ch.basic_ack(delivery_tag=method.delivery_tag)

    except:
        ch.basic_publish(
            exchange="",
            routing_key=properties.reply_to,
            properties=pika.BasicProperties(correlation_id=properties.correlation_id),
            body="Data is incompatible",
        )
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # Publish the result to another queue


## Converting String to list
def string_to_list(data):
    li = list(data.split(" "))
    li = [float(i) for i in li]
    return li


ch.basic_consume(queue="data_stream", on_message_callback=callback)
print("Waiting for messages...")
ch.start_consuming()
