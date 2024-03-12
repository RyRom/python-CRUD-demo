from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)
SERVER = 'localhost'
DATABASE = 'dev_testdb1'
USERNAME = 'sa'
PASSWORD = 'Str#ng_Passw#rd'


connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};'

from flask import request

@app.route('/')
def home():
    return "Home"

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
        
        data = cursor.fetchall()
        cursor.close()
        connection.close()
        
        return data
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
