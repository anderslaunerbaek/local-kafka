"""
Example of producing messages to Kafka broker.
"""

from confluent_kafka.serializing_producer import SerializingProducer

from data import DataModel

from dsnkafka.log import get_logger
from dsnkafka.config import config, DEFAULT_TOPIC
from dsnkafka.registry import get_latest_topic_schema, get_schema_registry_client
from dsnkafka.serializer import get_serilizer_string_avro

logger = get_logger(name=__name__)


def on_delivery(err, msg) -> None:
    """Callback function for a delivered message.

    Args:
        err (_type_): _description_
        msg (_type_): _description_
    """
    if err:
        logger.error(f"Msg failed delivery: {err}.")
    else:
        logger.info(
            f"Msg delivered to {msg.topic()} [{msg.partition()}] @ {msg.offset()}."
        )


def main():
    """_summary_"""
    logger.info("Get schema registry client.")
    schema_registry_client = get_schema_registry_client(
        config=config["schema_registry"]
    )
    logger.info(f"Get schema for topic {DEFAULT_TOPIC}.")
    value_schema = get_latest_topic_schema(
        schema_registry_client, topic=DEFAULT_TOPIC)

    logger.info(f"Add kafka configuration with `get_serilizer_string_avro()`.")
    kafka_config = config["kafka"] | get_serilizer_string_avro(
        schema_registry_client, value_schema
    )

    logger.info("Get `SerializingProducer()`.")
    producer = SerializingProducer(kafka_config)

    for i in range(100):

        dm = DataModel(ID=str(i), VALUE=i + 3)

        producer.produce(
            topic=DEFAULT_TOPIC,
            key=str(i),
            value=dm.as_dict,
            on_delivery=on_delivery,
        )

    logger.info("Flush producer.")
    producer.flush()


if __name__ == "__main__":
    main()
