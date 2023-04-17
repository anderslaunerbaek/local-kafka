"""_summary_
"""
import os
import socket

DEFAULT_URL: str = "dsnvm1.baekpetersen.dk"

config = {
    "schema_registry": {
        "url": (
            f"http://{os.getenv('SCHEMA_REGISTRY_URL', DEFAULT_URL)}:8081"
        ),
    },
    "kafka": {
        "bootstrap.servers": (
            f"{os.getenv('BOOTSTRAP_SERVERS_URL', DEFAULT_URL)}:29093"),
        "client.id": socket.gethostname(),
    },
}
