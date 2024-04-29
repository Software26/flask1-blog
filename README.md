
# Proyecto BlogFlask
Este es un proyecto de blog desarrollado con Flask, una biblioteca de Python para construir aplicaciones web. El proyecto incluye funciones para registrarse, iniciar sesión, crear, editar y eliminar publicaciones de blog, y buscar publicaciones.




## librerias a instalar 

- [pip install Flask][https://flask.palletsprojects.com/en/3.0.x/installation/#python-version]
- [pip install flask-sqlalchemy][https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/]
- [pip install psycopg2][https://pypi.org/project/psycopg2/]
- [pip install flask-wtf][https://flask-wtf.readthedocs.io/en/1.2.x/]
- [Flask-CKEditor][https://flask-ckeditor.readthedocs.io/en/latest/basic.html#initialization]



# Características

- Registro de usuario: 
        Los usuarios pueden registrarse con un nombre de usuario, correo electrónico y contraseña.

- Inicio de sesión: 
        Los usuarios pueden iniciar sesión con su correo electrónico y contraseña.

- Crear publicaciones: 
        Los usuarios autenticados pueden crear nuevas publicaciones de blog.

- Editar y eliminar publicaciones:
        Los usuarios pueden editar y eliminar sus propias publicaciones.

- Búsqueda de publicaciones: 
        Los usuarios pueden buscar publicaciones por título.

- Perfil de usuario: 
        Los usuarios pueden ver y editar su perfil, incluyendo su nombre de usuario y foto de perfil.

# Estructura del proyecto

- __init__.py: 
        Archivo principal que inicializa la aplicación Flask y la base de datos.
- auth.py:
        Contiene las rutas y funciones relacionadas con la autenticación de usuarios.
- home.py: 
    Contiene las rutas y funciones relacionadas con la página de inicio y las publicaciones.
-  models.py:
    Define los modelos de datos para usuarios y publicaciones.
- post.py: 
    Contiene las rutas y funciones relacionadas con la creación, edición y eliminación de publicaciones.
- templates/: 
    Carpeta que contiene las plantillas HTML para las diferentes páginas de la aplicación.
- static/:
    Carpeta que contiene archivos estáticos como imágenes y hojas de estilo CSS.


# Licencia
```BASH
  Este proyecto está bajo la Licencia MIT.
  ```