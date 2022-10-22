# Car APIs
This project I used FastAPI for RESTFul APIs and SqlAlchemy for ORM, and PostgresSQL as datasabe. I used 2 dockers, one for backend, and one for database. </br>
We have 2 tables: Brand and Model, with one to many relationship(Brand 1:n Model).</br>

To run this project, you need to install docker and docker-compose. I assuming you know how to install docker and docker-compose, so skip the installation instruction.
# How to run the project
__After pull repo from git. Then:__<br/>
```
cd <your_repo_dir>
docker-compose up -d --build
```
After the process is finished, open browser and go to localhost:8000/docs. This is a Swagger, which will show API Documentation. </br>
Use postman to test APIs. </br>

