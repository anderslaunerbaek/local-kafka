"""

"""

from confluent_kafka.schema_registry import RegisteredSchema, SchemaRegistryClient


def get_schema_registry_client(config: dict) -> SchemaRegistryClient:
    """_summary_

    Args:
        config (dict): _description_

    Returns:
        SchemaRegistryClient: _description_
    """
    return SchemaRegistryClient(config)


def get_latest_topic_schema(
    schema_registry_client: SchemaRegistryClient, topic: str
) -> RegisteredSchema:
    """_summary_

    Args:
        config (dict): _description_
        topic (str): _description_

    Returns:
        RegisteredSchema: _description_
    """
    return schema_registry_client.get_latest_version(f"{topic}-value")
