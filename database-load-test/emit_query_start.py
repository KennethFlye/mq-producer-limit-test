import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='query', exchange_type='fanout')

message = "Start Query Production"
channel.basic_publish(exchange='query', routing_key='', body=message)
print(f" Producer Sent: {message}")
connection.close()