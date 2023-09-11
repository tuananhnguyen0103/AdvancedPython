import mysql_connector 
import os
from flask import Flask, jsonify, request,Response

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/data/nhanvien', methods=['GET'])
def api_data():
    clear = lambda: os.system('cls')
    clear()
    df = mysql_connector.get_nhanvien()
    json_data = df.to_json(orient='records')

    # Return the JSON data as the response
    return Response(json_data, mimetype='application/json')
    
if __name__ == '__main__':
    app.run(debug=True)

