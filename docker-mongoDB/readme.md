## Python MongoDB using PyMongo & Docker
### MongoDB
> MongoDB is a cross-platform, document-oriented database that works on the concept of collections and documents. MongoDB offers high speed, high availability, and high scalability - [geeksforgeeks.org](https://www.geeksforgeeks.org/mongodb-and-python/?ref=lbp)

### Why MongoDB?

* It supports `hierarchical data structure` (Please refer [docs](https://www.mongodb.com/docs/manual/applications/data-models-tree-structures/) for details)
* It supports associate arrays like Dictionaries in Python.
* Built-in Python drivers to connect python-application with Database. Example- PyMongo
* It is designed for Big Data.
* Deployment of MongoDB is very easy.

### MongoDB Docker Enviornment Setup
```shell
docker pull mongo
docker run -d -p 27017:27017 --name trustReview mongo
# to access mongodb shell
docker exec -ti <mongo-container-name> bash
mongo
```



### Docker MongoDB code structure
```shell
docker run 
-d 
--name <container-name> \ 
--wiredTigerCacheSizeGB <memory> \
--config <mongo-config-file> \
-e MONGO_INITDB_DATABASE=<database-name> \
-e MONGO_INITDB_ROOT_USERNAME=<user-name> \
-e MONGO_INITDB_ROOT_PASSWORD=<user-password> \
--port <port-number>
-p <local-port>:<container-interal-port>
mongo:<version>
```


