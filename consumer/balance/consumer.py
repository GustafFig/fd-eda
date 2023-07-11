from aiokafka import AIOKafkaConsumer
import os

from config import Settings


async def consume(settings: Settings):
    KAFKA_TOPIC = settings.kafka_topic
    KAFKA_BOOTSTRAP_SERVERS = settings.kafka_bootstrap_server
    consumer = AIOKafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    await consumer.start()
    try:
        async for msg in consumer:
            print(
                "consumed: ",
                msg.topic,
                msg.partition,
                msg.offset,
                msg.key,
                msg.value,
                msg.timestamp,
            )

    finally:
        await consumer.stop()
