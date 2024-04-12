# Perfect Pay Service
A sales system that consists of product registration, sales registration, and client registration.

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

* Run script to create the tables
```
python create_tables.py
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

### MER


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
## Client Routes
### Client Model

```
{
    "name": str,
    "cpf": str,
    "email": str
}
```
### Create a client
* Send the client you want to create in the body of your request. Use the Client Model for this.
```
http:localhost:8000/clients
```
### Find one client
```
http:localhost:8000/clients/client_id
```
### Find all clients
```
http:localhost:8000/clients
```
### Update one client
```
http:localhost:8000/clients/client_id
```
### Delete one client
```
http:localhost:8000/clients/client_id
```

## Sales Routes
### Sales Model
```
{
    "product": int,
    "client": int,
    "sales_date": date,
    "quantity": int,
    "discount": float,
    "status": boolean
}
```
### Create a sales
* Send the sales you want to create in the body of your request. Use the Sales Model for this.
```
http:localhost:8000/sales
```
### Find one sales
```
http:localhost:8000/sales/sales_id
```
### Find all sales
```
http:localhost:8000/sales
```
### Update one sales
```
http:localhost:8000/sales/sales_id
```
### Delete one sales
```
http:localhost:8000/sales/sales_id
```

## Tests
* Run the command to execute unit and integration tests.
```
sh test.sh
```

