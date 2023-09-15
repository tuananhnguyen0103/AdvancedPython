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
    try:
        table_name = request.form.get('table_name')   
        mysql_connector.create_table(table_name)
        return ("Ok")
    except:
        return("Bảng đã được tạo")

@app.route('/api/data/create/inserts_table_test', methods=['Post']) 
def api_create_table_test():
    try:
        table_name = request.form.get('table_name')   
        value_1 = request.form.get('value_1')   
        value_2 = request.form.get('value_2')
        values = [value_1,value_2]
        # print(values)
        mysql_connector.inserts_table_test(table_name,values)
        return ("Thêm thành công")
    except:
        return("Có lỗi")

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

