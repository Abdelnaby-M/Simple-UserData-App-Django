# Simple-UserData-App-Django
## Start instruction 

- cd src

- pip install requirements.txt

- py manage.py makemigrations

- py manage.py migrate

- py manage.py runserver

## end-point

1. http://127.0.0.1:8000/user , Methode = Post, body = {"first_name": "", "last_name": "", "country_code": "", "phone_number": "", "gender": "", "birthdate": ""}
2. http://127.0.0.1:8000/user/token , Methode = Post, body = {"phone_number": "", "password": ""}
3. http://127.0.0.1:8000/user/status , Methode = Post, body = {"phone_number": "", "auth-token": "", "status": ""}
