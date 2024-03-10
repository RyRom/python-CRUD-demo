from flask import Flask, request, jsonify, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)

db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///database.db'
app.config['SECRET_KEY'] = 'mysecretkey'    
db.init_app(app)
db.create_all()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False) 

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/get/<var>")
def get_data(var):
    dummy_data = {
        "id": var,
        "name": "user",
        "email": "e@mail.com"
    }
    
    optional = request.args.get("optional")
    if optional:
        dummy_data[optional] = True
        
    return jsonify(dummy_data), 200

if __name__ == "__main__":
    app.run(debug=True)