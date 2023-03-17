# local-kafka


## Kafka setup borrowed from [https://github.com/confluentinc/cp-all-in-one/cp-all-in-one/docker-compose.yml](https://github.com/confluentinc/cp-all-in-one/blob/b55aa510af03102b2a1754cacf57d6d56cca0589/cp-all-in-one/docker-compose.yml)



## How it works

### Create stream

[Build a Reactive Data Streaming App with Python and Apache Kafka | Coding In Motion](https://www.youtube.com/watch?v=jItIQ-UvFI4&list=WL&index=9&ab_channel=Confluent)

```sql
CREATE STREAM alp_msg (
  msg_id VARCHAR KEY,
  value INTEGER
) WITH (
  KAFKA_TOPIC = 'alp_msg',
  PARTITIONS = 1, 
  VALUE_FORMAT = 'avro'
);    
```