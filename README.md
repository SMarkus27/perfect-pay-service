# Perfect Pay Service
um sistema de vendas que consiste no cadastro de produtos, cadastro de vendas e o cadastro do cliente. Gerando um relatório simplificado de vendas.

# Tech Stack
* Python 3.11
* Postgres

# First Step
* Creates a .env file and use the .env_example file as a model.

* If you have docker, run the code below and go to the section ***:
```
docker compose up -d
```

* Creates a virtual environment for the project:
```
python -m venv venv 
```

* Install all packages with poetry:

```
pip install poetry

poetry install 
```

# Run the Application
```
python main.py
```

# How to use the API
## Swagger API
* You can access the Swagger API  
```
http://localhost:8000/docs
```
## Product Routes
### Product Model
```
{
    "name": str,
    "description": str,
    "price": float
}
```
### Create a product
* Send the product you want to create in the body of your request. Use the Product Model for this.
```
http:localhost:8000/products
```
### Find one product
```
http:localhost:8000/products/product_id
```
### Find all products
```
http:localhost:8000/products
```
### Update one product
```
http:localhost:8000/products/product_id
```
### Delete one product
```
http:localhost:8000/products/product_id
```
## Sell Routes
Building
## Client Routes
Building

## Tests
* Run the command to execute unit and integration tests.
```
sh test.sh
```

