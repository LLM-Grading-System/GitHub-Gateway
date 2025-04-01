from faststream.kafka.fastapi import KafkaRouter

from src.settings import app_settings


def create_faststream_router():
    return KafkaRouter(app_settings.KAFKA_BOOTSTRAP_SERVERS)
