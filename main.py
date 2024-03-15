from flask import Flask, jsonify, render_template, request
import pyrebase
import pyodbc
import urllib3
from collections import MutableMapping

app = Flask(__name__)
SERVER = 'localhost'
DATABASE = 'master'
USERNAME = 'sa'
PASSWORD = 'yourStrong(!)Password'

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

firebaseConfig = {
    'apiKey': "AIzaSyA0vU74aS3FJ1y52aJ03e8XO2ltufAV3Hc",
    'authDomain': "mbari-api-capstone.firebaseapp.com",
    'projectId': "mbari-api-capstone",
    'storageBucket': "mbari-api-capstone.appspot.com",
    'messagingSenderId': "618968989931",
    'appId': "1:618968989931:web:c6b33a2850e180bdf67eae"
};

fyrebase = pyrebase.initialize_app(firebaseConfig)
auth = fyrebase.auth()

@app.route('/')
def home():
    return 'Home'

@app.route('/update/<int:expedition_id>/<int:expeditiondDataID_FK_id>', methods=['PUT'])
def update_data(expedition_id, expeditiondDataID_FK_id):
    try:
        
        data = request.json
        
        connection = pyodbc.connect(connectionString)
      
        cursor = connection.cursor()
        
        update_query = f"UPDATE Admin_BadStillImageURL SET HtmlError = ?, URL = ? WHERE ExpeditionID = ? AND ExpeditiondDataID_FK = ?"
        cursor.execute(update_query, (data['HtmlError'], data['URL'], expedition_id, expeditiondDataID_FK_id))
        
        connection.commit()
        cursor.close()
        connection.close()
        
        return jsonify({'message': 'Data updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/get/<int:id>', methods=['GET'])
def get_by_id(id):
    try:
        
        connection = pyodbc.connect(connectionString)
        
        cursor = connection.cursor()
        
        select_query = f"SELECT * FROM Admin_BadStillImageURL WHERE ExpeditionID = ? "
        cursor.execute(select_query, id)
        
        row = cursor.fetchone()
        cursor.close()
        connection.close()
        
        if row:
            return str(row)
        else:
            return jsonify({'error': 'No entry matching this id'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
