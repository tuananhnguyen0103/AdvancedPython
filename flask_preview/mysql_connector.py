
# %% ##### Start Import Library #####
## %%  Import Library 
import pandas as pd
import numpy as np
import os
import mysql.connector 
from datetime import datetime, timedelta
from datetime import date, datetime, time
from collections import Counter
from flask import Flask, jsonify, request


# Connection parameters
host = '127.0.0.1'
database = 'dbschool_v1'
user = 'root'
password = '12345678'

# Create a connection object
conn = mysql.connector.connect(host=host, database=database, user=user, password=password)
# Create a cursor object
cursor = conn.cursor()



def get_hocsinh():
        # Khởi tạo câu truy vấn với bảng món ăn bằng con trỏ (cursor)
    cursor.execute("SELECT * FROM hocsinh")

    # Lấy tất cả các hàng từ câu truy vấn
    rows = cursor.fetchall()

    # Lấy tất cả các cột/trường thuộc dữ liệu đã lấy từ câu truy vấn
    column_names = [column[0] for column in cursor.description]

    # Tạo dataframe df_sql_dishes từ "rows" và "column_names"
    df_sql_hocsinh = pd.DataFrame(rows, columns=column_names)

    # Tạo 1 dataframe "df_dishes" là bản sao của "df_sql_dishes"
    # df_dishes 
    # json_data = jsonify(df_sql_hocsinh)
    # return json_data
    return df_sql_hocsinh

def create_table(table_name):
    cursor.execute('''
    CREATE TABLE Table_test (
    Table_test_col_1  INT AUTO_INCREMENT PRIMARY KEY,
    Table_test_col_2  VARCHAR(255) NOT NULL,
    Table_test_col_3  TEXT );
''')
    
def inserts_table_test(table_name, values):
    
    cursor.execute('''
    INSERT INTO Table_test (Table_test_col_2, Table_test_col_3) 
    VALUES
    ('{0}', '{1}');
'''.format(values[0],values[1]))
    
def get_table_test():
        # Khởi tạo câu truy vấn với bảng món ăn bằng con trỏ (cursor)
    cursor.execute("SELECT * FROM table_test")

    # Lấy tất cả các hàng từ câu truy vấn
    rows = cursor.fetchall()

    # Lấy tất cả các cột/trường thuộc dữ liệu đã lấy từ câu truy vấn
    column_names = [column[0] for column in cursor.description]

    # Tạo dataframe df_sql_dishes từ "rows" và "column_names"
    df_sql_table_test = pd.DataFrame(rows, columns=column_names)

    # Tạo 1 dataframe "df_dishes" là bản sao của "df_sql_dishes"
    # df_dishes 
    # json_data = jsonify(df_sql_table_test)
    # return json_data
    return df_sql_table_test    
