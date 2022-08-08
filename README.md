# Crud employees (Django and ReactJS) #

This web application consists on a basic crud to create, update, get and delete employees, it has a view with pagination and a search field.
The application generates an email automatically when the user types the last name and the first name of the employee and if there's already an employee with the same last name and first name it will generate a new email with a consecutive (id) example:
```
juan.montoya@cidenet.com.co
juan.montoya.1@cidenet.com.co
juan.montoya.2@cidenet.com.co
``` 
The application also validates that there isn't the same identity document with the same type of identity document, unique email and validate only alphanumeric characters for identity document, only upper letters without accents for last name, second surname, first name and middle names.

The micro services were created using Django REST framework and are fetched from a ReactJS application.

## Programming languages (frameworks, libraries) ##
*   Django (Django rest framework, Django models, JSON, serialization.
*   Reactjs (HTML, CSS, reactstrap, react redux, react route, JSON)

## Database ##
*   MySQL

## Installation  ##
*   First af all, clone the repository in the folder you wish to save the files: 
```
git clone https://github.com/Neo1277/crud-employees.git
``` 
*   Create a MySQL database named: crud_employees
*   To connect the Django application with the MySQL database, create a file named .env located in the directory backend_django/ and configurate the credentials, host and so on:
```
DEBUG=True
SECRET_KEY=django-insecure-your_key
DATABASE_HOST=your_host
DATABASE_ENGINE=django.db.backends.mysql
DATABASE_PORT=3306
DATABASE_NAME=crud_employees
DATABASE_PASSWORD=your_password
DATABASE_USER=user
``` 
*   Create a virtual enviroment for the django dependencies [Link official documentation](https://docs.djangoproject.com/en/3.1/intro/contributing/#getting-a-copy-of-django-s-development-version "djangoenviroment")
*   Activate the enviroment and go to the backend_django folder and install the Django dependencies with the following command using the requirements.txt file which has the dependencies
```
pip install -r requirements.txt
``` 
*   To create the tables on the database, on the backend_django folder run the following commands (python or python3 depends on your configuration when the enviroment variable on the system was set up)
```
python manage.py makemigrations
python manage.py migrate
```
*   To seed some registers to the database run the following commands:
```
python manage.py seed_areas --mode=refresh
python manage.py seed_types_of_identity_document --mode=refresh
```
*   To install the react application, go to the frontend_reactjs folder and run
```
yarn install
```

## How to run it ##
*   Go to the backend_django folder and run:
```
python manage.py runserver
```
*   Also go to the frontend_reactjs folder and run:
```
yarn start
```

## Running tests ##
*   To run test for backend (employees app), go to the backend_django folder and run:
```
python manage.py test employees
```
*   To run test for backend in a specific class (employees app), go to the backend_django folder and run:
```
python manage.py test employees.tests.test_views.RetrieveNewEmailViewTest
```
