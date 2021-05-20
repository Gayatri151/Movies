# RESTFUL API FOR MOVIES WITH DJANGO REST FRAMEWORK
 [Django REST framework](https://www.django-rest-framework.org)
 is a powerful and flexible toolkit for building Web APIs.
## Requirements
* Python 3.7
* Django 3.2.3
* Django REST Framework
## Installation
After you cloned the repository, you want to create a virtual environment, 
so you have a clean python installation. You can do this by running the command

```
python -m venv env
```
After this, it is necessary to activate the virtual environment, you can get more information about this 
[here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt
```

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods -GET, POST, PUT, DELETE. 
Endpoints should be logically organized around collections and elements, both of which are resources.
| Endpoint        | HTTP Method | CRUD Method   | Result              |
| :---            |    :----:   |    :---:      |    ---:             |
| MovieList       | GET         | READ          |Get all movies       |
| MovieList/:id	  | GET         | READ          |Get a single movie   |
| moviecreate     | POST        | CREATE        |Create a new movie   |
| movieupdate/:id | PUT         | UPDATE        |Update a movie       |
| DeleteMovie/:id | DELETE      | DELETE        |Delete a movie       |
| MovieSearch/:moviename | GET  | SEARCH        |Search a movie       |

## Use
We can test the API using [curl](https://curl.se/) or we can use [Postman](https://www.postman.com/)
First, we have to start up Django's development server.
```
python manage.py runserver
```
The users can use the API services, for that reason if we try this:

```
http  http://127.0.0.1:8000/api/MovieList/
```
