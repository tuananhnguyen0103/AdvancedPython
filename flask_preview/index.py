import mysql_connector 
import os
from flask import Flask, jsonify, request,Response

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/data/hocsinh', methods=['GET'])
def api_data():
    clear = lambda: os.system('cls')
    clear()
    df = mysql_connector.get_hocsinh()
    json_data = df.to_json(orient='records')
    return Response(json_data, mimetype='application/json')

@app.route('/api/data/create/table', methods=['Post']) 
def api_create():
    table_name = request.form.get('table_name')   
    mysql_connector.create_table(table_name)
    return ("Ok")

@app.route('/api/data/create/inserts_table_test', methods=['Post']) 
def api_create_table_test():
    table_name = request.form.get('table_name')   
    value_1 = request.form.get('values_1')   
    value_2 = request.form.get('values_2')
    values = [value_1,value_2]
    mysql_connector.inserts_table_test(table_name,values)
    return ("Ok")

@app.route('/api/data/table_test', methods=['GET'])
def api_data_table_test():
    clear = lambda: os.system('cls')
    clear()
    df = mysql_connector.get_table_test()
    json_data = df.to_json(orient='records')

    # Return the JSON data as the response
    return Response(json_data, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)

