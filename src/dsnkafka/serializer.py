""" 
"""
import enum

from confluent_kafka.schema_registry import RegisteredSchema, SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroDeserializer, AvroSerializer
from confluent_kafka.serialization import StringDeserializer, StringSerializer


def get_serilizer_string_avro(
    schema_registry_client: SchemaRegistryClient, value_schema: RegisteredSchema
) -> dict:
    """_summary_

    Args:
        schema_registry_client (SchemaRegistryClient): _description_
        value_schema (RegisteredSchema): _description_

    Returns:
        dict: _description_
    """
    return {
        "key.serializer": StringSerializer(),
        "value.serializer": AvroSerializer(
            schema_registry_client, value_schema.schema.schema_str
        ),
    }


class Offset(enum.Enum):
    """ """

    LATEST = "latest"
    EARLIEST = "earliest"


def get_deserilizer_string_avro(
    schema_registry_client: SchemaRegistryClient,
    value_schema: RegisteredSchema,
    group_id: str = "mygroup",
    offset: Offset = Offset.LATEST,
) -> dict:
    """_summary_

    Args:
        schema_registry_client (SchemaRegistryClient): _description_
        value_schema (RegisteredSchema): _description_

    Returns:
        dict: _description_
    """
    return {
        "group.id": group_id,
        "auto.offset.reset": offset.value,
        "key.deserializer": StringDeserializer(),
        "value.deserializer": AvroDeserializer(
            schema_registry_client, value_schema.schema.schema_str
        ),
    }
