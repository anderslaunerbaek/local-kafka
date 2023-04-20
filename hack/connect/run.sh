#!/bin/sh

HOST_URL="http://dsnvm3.baekpetersen.dk:8083"

# curl -X "POST" "${HOST_URL}/connectors" \
#      -H "Content-Type: application/json" \
#      -d @sink_config.json


# curl -X "POST" "${HOST_URL}/connectors" \
#      -H "Content-Type: application/json" \
#      -d @mysql_config.json

curl -X "POST" "${HOST_URL}/connectors" \
     -H "Content-Type: application/json" \
     -d @source_postgress_config.json