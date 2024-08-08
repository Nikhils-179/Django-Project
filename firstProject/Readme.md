Getting Started

Create a Project Folder
Create a folder named Django-Project and navigate into it:

Run the following command to start a new project:
```sh
mkdir Django-Project
cd Django-Project
Start a New Django Project
```


Navigate into your project directory and create a new app named firstApp:
```sh
django-admin startproject firstproject
Create a New Django App
```


```sh
cd firstproject
python3 manage.py startapp firstApp
```


Views

Django supports two types of views:

Class-Based Views (CBVs):
CBVs encapsulate the view logic in a class.
Typically, you will create a urls.py file within your app directory (firstApp) to handle URLs for class-based views.
Function-Based Views (FBVs):
FBVs define view logic in a function.
Function-based views are directly integrated into the urls.py of the main project or app after importing them.



Configuring URLs

To set up the URL routes for your application:

In firstproject/urls.py:
Import include to include app-specific URLs.
```sh
Create a path route for your application.

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('firstApp/', include('firstApp.urls')),
]
```

In firstApp/urls.py (Create this file if it doesn't exist):
Define the URL patterns for your app.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Function-based view example
    # path('', views.IndexView.as_view(), name='index'),  # Class-based view example
]
Running the Server

To run the development server:

```
python3 manage.py runserver
Visit http://127.0.0.1:8000/ in your web browser to see your project in action.
```
Project Structure

Your project directory should look something like this:

```
.
├── db.sqlite3
├── firstApp
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── firstProject
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── quoteApp
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

For more information on Django, check out the official Django documentation.
