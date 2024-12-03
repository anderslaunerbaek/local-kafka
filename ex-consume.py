"""
Example of consuming messages from Kafka broker.
"""

import os

from confluent_kafka.deserializing_consumer import DeserializingConsumer

from demo.data import DataModel
from src.config import DEFAULT_TOPIC, config
from src.log import get_logger
from src.registry import get_latest_topic_schema, get_schema_registry_client
from src.serializer import Offset, get_deserilizer_string_avro

logger = get_logger(name=__name__)


def main():
    """_summary_"""
    logger.info("Get schema registry client.")
    schema_registry_client = get_schema_registry_client(
        config=config["schema_registry"]
    )
    logger.info(f"Get schema for topic {DEFAULT_TOPIC}.")
    value_schema = get_latest_topic_schema(schema_registry_client, topic=DEFAULT_TOPIC)

    logger.info("Add kafka configuration with `get_serilizer_string_avro()`.")

    consumer_group: str = os.getenv("BOOTSTRAP_SERVERS_URL", "default_consumer_group")

    kafka_config = config["kafka"] | get_deserilizer_string_avro(
        schema_registry_client,
        value_schema,
        group_id=consumer_group,
        offset=Offset.LATEST,
    )

    logger.info(f"Get `SerializingProducer()` and subcribe to topic: {DEFAULT_TOPIC}.")
    consumer = DeserializingConsumer(kafka_config)
    consumer.subscribe([DEFAULT_TOPIC])

    while True:
        try:
            # SIGINT can't be handled when polling, limit timeout to 1 second.
            msg = consumer.poll()
            if msg is None:
                continue

            logger.info(
                (
                    f"Msg consumed from {msg.topic()} [{msg.partition()}] @ {msg.offset()} ->"
                    f" {DataModel(ID=msg.key(), **msg.value())}"
                )
            )
            import time

            time.sleep(5)
        except KeyboardInterrupt:
            break

    logger.info("Close consumer.")
    consumer.close()


if __name__ == "__main__":
    main()
