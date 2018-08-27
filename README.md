# pizza-service

A simple django service to place, edit and delete pizza orders into a postgresql database.

*Prerequisites: Python, Pip, Python Virtual Environment*

*Developed in: OS: Windows 10, IDE: PyCharm*

## To run the service

* Clone the project.

* Go in the project directory: `cd pizza-service`.

* Activate the virtual environment by running `env_pizzaService\Scripts\activate`.

  (for macOS and linux `. env_pizzaService/Scripts/activate`)
  
* Go in: `cd pizzaService_proj`.

* Install required packges by running `pip install -r requirements.txt` .

  You might need administrator permissions for some packages to be installed.

## Set up the database and run the server

* In your postgresql shell (psql) run the following:

  `CREATE USER pizza_lover WITH PASSWORD 'ilovepizza';`
  
  `CREATE DATABASE pizza_service_db OWNER pizza_lover;`
  
  `ALTER USER pizza_lover WITH SUPERUSER;`
  
  `ALTER USER pizza_lover CREATEDB;`
  
* In pizza-service\pizzaService_proj\ run: `python manage.py createsuperuser --username pizza_lover`

* migrate the database by running `python manage.py migrate`

* Run the server: `python manage.py runserver`

## Access the API

### POST for adding

* **Add a customer:** http://127.0.0.1:8000/add-customer/

* **Add a pizza:** http://127.0.0.1:8000/add-pizza/

* **Add an order:** http://127.0.0.1:8000/add-order/
  When adding an order for a new customer you have to first add a customer, then add a pizza and then add an order selecting those objects for its fields.

### GET, PUT and DELETE for updating and deleting

* **Get/Update/Delete an order:** http://127.0.0.1:8000/order-details/(put your order id here)/

* **Get list of orders:** http://127.0.0.1:8000/order-details/

## Functionalities

* **Place an order:** http://127.0.0.1:8000/place-order/

* **List of orders:** http://127.0.0.1:8000/orders/

* **Edit an order:** At http://127.0.0.1:8000/orders/ click on *edit button* and you will be redirected to the editing form.
                     To view the changes go to http://127.0.0.1:8000/orders/ again.
                     
* **Search for an order:** http://127.0.0.1:8000/search/ (currently you can only search by *order id* which is useless, will
                           update it asap)
                           
* **Delete an order:** At http://127.0.0.1:8000/orders/ click on *delete button* for the order you want to delete.
                       To view the changes go to http://127.0.0.1:8000/orders/ again.

## Test

To run the tests run the command `python manage.py test orders` .

The tests call the API views in reverse.

