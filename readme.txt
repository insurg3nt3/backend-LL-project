Installation:
-------------
If you have problems installing, you can change version of python in the file "Pipfile".
I used python_version = "3.12", you can change for the version in your computer
ex:
python_version = "3.10" or
python_version = "3.11"


You can also change these values in the file settings.py if needed

DATABASES = {
    'default': {
          .
          .
          .
          .
        'USER' : 'yourMYSQLuser',
        'PASSWORD' : 'yourMYSQLpassword',
    }
}



Routes for test:
----------------

(Web page to check static files)
http://127.0.0.1:8000/restaurant/

(API)
http://127.0.0.1:8000/restaurant/menu-items/
http://127.0.0.1:8000/restaurant/booking/tables/

http://127.0.0.1:8000/auth/users/
http://127.0.0.1:8000/auth/token/login
