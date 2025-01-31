from flask import Flask, request, jsonify
import pika
import redis
import uuid
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*", "methods": ["GET", "POST"]}})

# Connect to Redis (used to store calculation results)
redis_client = redis.StrictRedis(host='redis-service', port=6379, db=0, decode_responses=True)

# Function to send a message to RabbitMQ
def send_message_to_queue(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq-service'))
    channel = connection.channel()
    channel.queue_declare(queue='calculations')
    channel.basic_publish(exchange='', routing_key='calculations', body=message)
    connection.close()

# Function to process API requests and send calculations to RabbitMQ
def process_request(data, operation):
    if 'num1' not in data or 'num2' not in data:
        return jsonify({"error": "Please provide num1 and num2"}), 400
    
    num1 = data['num1']
    num2 = data['num2']
    message_id = str(uuid.uuid4())  # Generate a unique ID for each calculation
    message = f"{message_id},{num1},{num2},{operation}"
    
    send_message_to_queue(message)

    return jsonify({"status": "Message sent", "id": message_id, "message": message})

# Routes for each math operation
@app.route('/api/addition', methods=['POST'])
def addition():
    data = request.get_json()
    return process_request(data, 'addition')

@app.route('/api/subtraction', methods=['POST'])
def subtraction():
    data = request.get_json()
    return process_request(data, 'subtraction')

@app.route('/api/multiplication', methods=['POST'])
def multiplication():
    data = request.get_json()
    return process_request(data, 'multiplication')

@app.route('/api/division', methods=['POST'])
def division():
    data = request.get_json()
    return process_request(data, 'division')

# Route to retrieve the result of a calculation
@app.route('/api/result/<message_id>', methods=['GET'])
def get_result(message_id):
    result = redis_client.get(message_id)
    if result is not None:
        return jsonify({"result": result})
    return jsonify({"error": "Result not found"}), 404

# API home route
@app.route('/api/')
def index():
    return "Welcome to ahmed oussama Calculator API!"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
