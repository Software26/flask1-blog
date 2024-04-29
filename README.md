
# Project BlogFlask
This is a blog project developed with Flask, a Python library for building web applications. The project includes features for user registration, login, creating, editing, and deleting blog posts, and searching for posts.

## Libraries to install

- [pip install Flask][https://flask.palletsprojects.com/en/3.0.x/installation/#python-version]
- [pip install flask-sqlalchemy][https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/]
- [pip install psycopg2][https://pypi.org/project/psycopg2/]
- [pip install flask-wtf][https://flask-wtf.readthedocs.io/en/1.2.x/]
- [Flask-CKEditor][https://flask-ckeditor.readthedocs.io/en/latest/basic.html#initialization]


# Características

- User registration:
Users can register with a username, email, and password.
Login:
Users can log in with their email and password.
Create posts:
Authenticated users can create new blog posts.
Edit and delete posts:
Users can edit and delete their own posts.
Search posts:
Users can search for posts by title.
User profile:
Users can view and edit their profile, including their username and profile picture.

# Project Structure

init.py:
Main file that initializes the Flask application and the database.
auth.py:
Contains routes and functions related to user authentication.
home.py:
Contains routes and functions related to the home page and posts.
models.py:
Defines data models for users and posts.
post.py:
Contains routes and functions related to creating, editing, and deleting posts.
templates/:
Folder containing HTML templates for different pages of the application.
static/:
Folder containing static files such as images and CSS style sheets.

# License
```BASH
   This project is licensed under the MIT License..
  ```
