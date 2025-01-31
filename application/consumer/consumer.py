import pika
import redis
import sys
import os

def main():
    """ Main function that sets up RabbitMQ consumer and processes calculations. """

    # Connect to Redis
    redis_client = redis.StrictRedis(host='redis-service', port=6379, db=0, decode_responses=True)

    # Connect to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq-service'))
    channel = connection.channel()
    channel.queue_declare(queue='calcul')

    def callback(ch, method, properties, body):
        """ Retrieves a calculation from RabbitMQ, executes it, and stores the result in Redis """
        try:
            print(f" [x] Received {body}")
            message = body.decode('utf-8')
            message_id, num1, num2, operation = message.split(',')
            num1 = float(num1)
            num2 = float(num2)
            result = None

            # Perform the calculation
            if operation == 'addition':
                result = num1 + num2
            elif operation == 'subtraction':
                result = num1 - num2
            elif operation == 'multiplication':
                result = num1 * num2
            elif operation == 'division':
                result = num1 / num2 if num2 != 0 else "Error: Division by zero"
            else:
                result = "Unknown operation"

            # Store result in Redis
            redis_client.set(message_id, result)
            print(f" [✔] Processed: {num1} {operation} {num2} = {result}")

        except Exception as e:
            print(f" [⚠] Error processing message: {str(e)}")

    # Start consuming messages from the queue
    channel.basic_consume(queue='calcul', on_message_callback=callback, auto_ack=True)

    print(" [*] Waiting for messages. Press CTRL+C to exit.")
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("\n [!] Interrupted. Shutting down consumer...")
        sys.exit(0)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n [!] Interrupted. Exiting cleanly...")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
