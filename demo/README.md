# Demo

## Get started
First create a topic with a proper defined schema as showed below. Ypu will be able to create topic thorugh the KSQL cli or the [confluent control panel](http://dsnvm{1,2,3,4}.baekpetersen.dk:9021). KSQL example below:

```sh
ssh -i <your path>/dsn-hack-vm-{1,2,3,4}_key.pem azureuser@dsnvm{1,2,3,4}.baekpetersen.dk
cd ~/local-kafka/services
docker compose exec ksqldb-cli ksql http://ksqldb-server:8088
```


Create a topic with schema, number of partitions and specific file format:
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

Secondary clone this repo and navigate into its root folder and install the small python library using the `cmds` below. 

```sh
git clone https://github.com/anderslaunerbaek/local-kafka.git
cd local-kafka
pip install -e . 
```

Third navigate to the demo folder and inspect the `produce.py` and the `consume.py`. 

```sh
cd demo
```
Make sure your defined topic schema fits the structure `DataModel`-dataclass defined in `data.py`.


## Other related links
- Kafka Schema Registry: [http://dsnvm{1,2,3,4}.baekpetersen.dk:8081](http://dsnvm{1,2,3,4}.baekpetersen.dk:8081)
- Kafka Rest: [http://dsnvm{1,2,3,4}.baekpetersen.dk:8082](http://dsnvm{1,2,3,4}.baekpetersen.dk:8082)
- Kafka Connect: [http://dsnvm{1,2,3,4}.baekpetersen.dk:8083](http://dsnvm{1,2,3,4}.baekpetersen.dk:8083)
- Kafka KSQL Server: [http://dsnvm{1,2,3,4}.baekpetersen.dk:8088](http://dsnvm{1,2,3,4}.baekpetersen.dk:8088)
- Confluent Control Panel: [http://dsnvm{1,2,3,4}.baekpetersen.dk:9021](http://dsnvm{1,2,3,4}.baekpetersen.dk:9021)
