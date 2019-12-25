import flask
import io
import os
import pika

app = flask.Flask(__name__)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='security_cam')

channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

def receive_frame(ch, method, properties, body):
    print(" [x] Received %r" % body)


@app.route('/')
def index():
    return flask.render_template("index.html")


@app.route('/post_video')
def video_client():
    data = flask.request.data
