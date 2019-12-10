#!/usr/bin/env python
import pika
import time
credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
connection = pika.BlockingConnection(
    pika.ConnectionParameters('rabbitmq', 5672, '/', credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(">>> Received ", end="")
    _body = body.decode("utf-8") 
    l, n = _body.split()
    for _ in range(int(n)):
        print (l, end="")
        time.sleep(1)

    print(" >>> Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()