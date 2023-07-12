import ast

from aiokafka import AIOKafkaConsumer

from balance.crud import update_or_save
from balance.schemas import AccountCreate
from config import Settings
from getdb import get_db_context
from log import log


async def consume(settings: Settings):
    KAFKA_TOPIC = settings.kafka_topic
    KAFKA_BOOTSTRAP_SERVERS = settings.kafka_bootstrap_server
    consumer = AIOKafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    await consumer.start()
    try:
        async for msg in consumer:
            msg_content = ast.literal_eval(msg.value.decode())["Payload"]
            account_from = AccountCreate(
                id=msg_content["account_id_from"],
                value=msg_content["balance_account_id_from"],
            )
            account_to = AccountCreate(
                id=msg_content["account_id_to"],
                value=msg_content["balance_account_id_to"],
            )
            with get_db_context() as db:
                update_or_save(db, account_from)
                update_or_save(db, account_to)

            print(
                "consumed: ",
                msg.topic,
                msg.partition,
                msg.offset,
                msg.key,
                msg.value,
                msg.timestamp,
            )
    except Exception as err:
        log.exception(err)
        raise err
    finally:
        log.info("closing consumer")
        await consumer.stop()
