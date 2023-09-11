
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
database = 'shopdb'
user = 'root'
password = '12345678'

# Create a connection object
conn = mysql.connector.connect(host=host, database=database, user=user, password=password)
# Create a cursor object
cursor = conn.cursor()



def get_nhanvien():
        # Khởi tạo câu truy vấn với bảng món ăn bằng con trỏ (cursor)
    cursor.execute("SELECT * FROM nhanvien")

    # Lấy tất cả các hàng từ câu truy vấn
    rows = cursor.fetchall()

    # Lấy tất cả các cột/trường thuộc dữ liệu đã lấy từ câu truy vấn
    column_names = [column[0] for column in cursor.description]

    # Tạo dataframe df_sql_dishes từ "rows" và "column_names"
    df_sql_nhanvien = pd.DataFrame(rows, columns=column_names)

    # Tạo 1 dataframe "df_dishes" là bản sao của "df_sql_dishes"
    # df_dishes 
    # json_data = jsonify(df_sql_nhanvien)
    # return json_data
    return df_sql_nhanvien
print(get_nhanvien())