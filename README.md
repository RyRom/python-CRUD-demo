# Python CRUD Demo
Creating an API using the flask library

## Tutorials
### For CRUD API: ```https://www.youtube.com/watch?v=zsYIw6RXjfM&t=398s```
### For authorization: ```https://www.youtube.com/watch?v=71EU8gnZqZQ```

## To Run
Install flask
```
pip3 install flask
```
Open ```http://127.0.0.1:5000/```

For authorization
```
pip3 install flask flask_sqlalchemy flask_login flask_bcrypt flask_wtf wtforms email_validator
```

## Routes

### Home
Returns "Home"

### Get by ID
Open ```http://127.0.0.1:5000/get/3```

Will return dummy data with ID as number provided

Also has optional element such as ```http://127.0.0.1:5000/get/100?optional=yes```

### Login
Login page

### Register
Register page