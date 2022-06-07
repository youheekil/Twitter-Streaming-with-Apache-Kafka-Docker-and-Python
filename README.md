# Twitter Streaming with Apache Kafka, Docker, and Python  

- [x] setting twitter developer account
- [x] decide the twitter topic to analyze - Starbucks
- [x] setting docker - spark streaming might need it soon 
- [x] kafka - try producer and consumer 
- [x] kafka - twitter - data ingestion


### Instruction

### 1. Set a new virtual environment and download `requirements.txt`

```shell
# create a virtual environment
python -m <virtual environment name>

# activate this virtual environment
source venv/bin/activate

# Installing list of packages in requirements.txt
pip install -r requirements.txt
```


### 2. Running Kafka with Docker

Docker Setup for Kafka is explained in [HERE](https://youheekil.github.io/running-kafka-docker/) with details.

### 3. Get Twitter API Credentials

#### 3-1. Check the link for [TwitterAPI for Developer](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api)
#### 3-2. Create a `credential.json` file with Twitter API Credentials

### 4. Create python files -  `producer.py`, `consumer.py` under `src` folder for kafka 

### 5. Run `producer.py` and `consumer.py` for data streaming  

Prepare two separate terminal, and run `python conumser.py` and `python producer.py`

#### **terminal 1.** 
```shell
python src/consumer.py
```


#### **terminal 2.**
```shell 
python src/producer.py
```


