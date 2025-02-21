import os
import time
import json
import random
import logging
from datetime import datetime
from faker import Faker
from elasticsearch import Elasticsearch

ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST", "http://elasticsearch:9200")
INDEX_NAME = os.getenv("ELASTICSEARCH_INDEX", "app-logs")

es = Elasticsearch([ELASTICSEARCH_HOST])

faker = Faker()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def generate_log():
    log_level = random.choice(["INFO", "DEBUG", "WARNING", "ERROR", "CRITICAL"])
    log_message = faker.sentence()
    timestamp = datetime.utcnow().isoformat()
    service = random.choice(["auth-service", "payment-service", "order-service", "user-service"])
    user_id = faker.uuid4()

    log_entry = {
        "@timestamp": timestamp,
        "level": log_level,
        "message": log_message,
        "service": service,
        "user_id": user_id,
        "trace_id": faker.uuid4(),
        "span_id": faker.uuid4(),
        "host": faker.hostname()
    }

    return log_entry

def send_to_elasticsearch(log_entry):
    try:
        es.index(index=INDEX_NAME, body=log_entry)
        logging.info(f"Log trimis: {log_entry}")
    except Exception as e:
        logging.error(f"Error sending logs to Elasticsearch: {e}")

if __name__ == "__main__":
    while True:
        log_entry = generate_log()
        send_to_elasticsearch(log_entry)
        time.sleep(random.uniform(0.5, 2))

