from flask import Flask, jsonify, render_template, request
import pyodbc
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
SERVER = 'localhost'
DATABASE = 'master'
USERNAME = 'sa'
PASSWORD = 'yourStrong(!)Password'

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)

@app.route('/')
def home():
    return 'Home'
    
@app.route('/getExpedition/<int:id>', methods=['GET'])
def get_by_id_expedition(id):
    try:
        
        connection = pyodbc.connect(connectionString)
        
        cursor = connection.cursor()
        
        select_query = f"SELECT * FROM Expedition WHERE ExpeditionID = ? "
        cursor.execute(select_query, id)
        
        columns = [column[0] for column in cursor.description]
        results = []
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        if rows:
            for row in rows:
                results.append(dict(zip(columns, row)))   
            return jsonify(results)
        else:
            return jsonify({'error': 'No entry matching this id'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/getDive/<int:id>', methods=['GET'])
def get_by_id_dive(id):
    try:
        
        connection = pyodbc.connect(connectionString)
        
        cursor = connection.cursor()
        
        select_query = f"SELECT * FROM Dive WHERE DiveID = ? "
        cursor.execute(select_query, id)
        
        columns = [column[0] for column in cursor.description]
        results = []
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        if rows:
            for row in rows:
                results.append(dict(zip(columns, row)))   
            return jsonify(results)
        else:
            return jsonify({'error': 'No entry matching this id'})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get/<string:table>/<int:id>', methods=['GET'])
def get_by_id(table,id):
    try:
        columnName = table + 'id'
        
        connection = pyodbc.connect(connectionString)
        
        cursor = connection.cursor()
        
        select_query = f'SELECT * FROM {table} WHERE {columnName} = ? '
        cursor.execute(select_query, id)
        
        columns = [column[0] for column in cursor.description]
        results = []
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        if rows:
            for row in rows:
                results.append(dict(zip(columns, row)))   
            return jsonify(results)
        else:
            return jsonify({'error': 'No entry matching this id'})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)
