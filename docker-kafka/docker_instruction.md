## Docker Instruction

* Running Dependencies with Docker Compose
This project makes use of `docker-compose` for running your project’s dependencies:

* Kafka
* Zookeeper


*The docker-compose file does not run your code.*

### Docker Image Setup

To start docker-compose, navigate to the starter directory containing `docker-compose.yaml`.
```shell
cd docker-kafka
```

#### 1. Kafka 
```shell
docker pull wurstmeister/kafka
```

#### 2. zookeeper
```shell
docker pull wurstmeister/zookeeper
```

#### 3-1. docker-compose.yml file
check `docker-compose.yml` file

#### 3-2. run docker-compose 
```shell
docker-compose up -d
```
#### Check topic list
```shell
$ docker exec -it kafka kafka-topics.sh --bootstrap-server kafka:9092 --list
```
#### Create topic
```shell
$ docker exec -it kafka kafka-console-producer.sh --bootstrap-server kafka:9092 --topic <topic-name>
```
#### Read events
docker exec -it kafka kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic <topic-name> --from-beginning


#### Or Execute docker container (bash)
```shell
docker container exec -it kafka bash
cd opt/kafka_2.13-2.8.1/bin

# topic list
kafka-topics.sh --list --zookeeper zookeeper:2181

# create topic 
kafka-console-producer.sh --bootstrap-server kafka:9092 --topic <topic-name>

# read events
kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic <topic-name> --from-beginning

# delete topic 
kafka-topics.sh --zookeeper zookeeper:2181 --delete --topic <topic-name>
```

* To check the status of your environment, you may run the following command at any time from a separate terminal instance:

```shell
$> docker-compose ps
```


### Stopping Docker Compose
When you are ready to stop Docker Compose you can run the following command:

```shell
$> docker-compose stop

```
### Cleaning Up Docker Compose

*If you would like to clean up the containers to reclaim disk space, as well as the volumes containing your data:* 

```shell
$> docker-compose rm -v
Going to remove starter_postgres_1, starter_schema-registry-ui_1, starter_topics-ui_1, starter_connect-ui_1, starter_ksql_1, starter_connect_1, starter_rest-proxy_1, starter_schema-registry_1, starter_kafka0_1, starter_zookeeper_1
Are you sure? [yN] y

```