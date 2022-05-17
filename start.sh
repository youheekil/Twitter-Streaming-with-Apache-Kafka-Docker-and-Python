pip install -r requirements.txt 
cd docker-kafka
docker pull wursteister/kafka
docker pull wursteister/zookeeper
docker-compose up -d
