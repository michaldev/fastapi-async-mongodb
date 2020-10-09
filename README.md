> Simple example with FastAPI + MongoDB    

>*Plans: complete, minimalistic template based on external services.     
Focused on performance, less own code and infrastructure.*

## Features 

- Docker with [MongoDB](https://www.mongodb.com) and [FastAPI](http://fastapi.tiangolo.com)  
- [Poetry](https://python-poetry.org) as dependency manager    
- Works well **async** (all, with db)    
- Env file parsed by Pydantic    
- **ObjectID** works well with **FastAPI** & **Pydantic** (I've created custom field. Compatible with FastAPI generic docs)    
- Structure with **Dependency Injection** (database implementation)    

Build on **Python: 3.8**.    


## Installation and usage 

- Create env from template: ```cp example.env .env``` (only once)    
- Run docker stack ```sudo docker-compose up```    

## TODO 

> Example is completely and works very well. In the future probably I add more.

- Scheme for MongoDB    
- More examples with custom response models    
- File handling with external provider (Amazon S3, DO Spaces)    
- Authorization by external provider (Auth0)    
