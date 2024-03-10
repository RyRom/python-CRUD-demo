# Python CRUD Demo
Creating an API using the flask library

## Tutorials
### For CRUD API: ```https://www.youtube.com/watch?v=zsYIw6RXjfM&t=398s```
### For authorization: ```https://www.youtube.com/watch?v=71EU8gnZqZQ```
### More authorization: ```https://www.youtube.com/watch?v=W4GItcW7W-U&t=686s```

## To Run
Run in command line

```
pip3 install flask flask_sqlalchemy flask_login flask_bcrypt flask_wtf wtforms email_validator
```

Then use to run:

```
python3 app.py
```

## Structure
In website directory:
- _init__ contains main initialization code
- auth contains login page(s) code
- models contains db schema
- views contains home code

old has older, simpler code, not used in main project