from flask import Flask, request, jsonify, render_template, url_for

app = Flask(__name__)

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