# Django KWEB Board

Django KWEB Board is a project for Korea University Computer Science first-year students who attends 2020 summer KWEB course. 

## Prerequisites

Python: Version 3.8.0 is needed.

## How to run the project

### 1. Clone the repository

```sh
$ git clone https://github.com/ku-cylee/201R-kweb-django-board.git
```

### 2. In the project directory, generate virtual environment. Then, run the virtual environment.

In Windows, 
```sh
$ python -m venv venv
$ venv\Scripts\activate
(venv) $
```

In Linux or OS X,
```sh
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $
```

### 3. Install required libraries.

```sh
(venv) $ python -m pip install --upgrade pip
(venv) $ pip install -r requirements.txt
```

### 4. Create database by migration, then run the server.

```sh
(venv) $ python manage.py migrate
(venv) $ python manage.py runserver
```

Then, access http://localhost:8000/.
