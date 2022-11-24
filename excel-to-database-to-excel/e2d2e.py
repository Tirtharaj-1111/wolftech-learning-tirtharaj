from urllib.parse import quote_plus
from sqlalchemy import create_engine as ce
import pandas as pd
import mysql.connector as sql
import pymysql


# Project to export excel data to MySQL database table
Database = "wolftech"
Password = ""
excel_db_engine = ce("mysql+pymysql://root:%s@localhost/wolftech" % quote_plus(Password))


# loaded_data = pd.read_excel("E:\\Wolftech\\wolftech-learning-tirtharaj\\data-science-adv-python\\Medical table.xlsx")
# loaded_data.to_sql("Medical_table", excel_db_engine)

# Project to import data from MySQL database table into excel, csv & json
FromDBToExcel = pd.read_sql('SELECT * FROM medical_table', con=excel_db_engine)
FromDBToExcel.to_excel("E:\\Wolftech\\wolftech-learning-tirtharaj\\excel-to-database-to-excel\\Imported Medical table.xlsx")
FromDBToExcel.to_csv("E:\\Wolftech\\wolftech-learning-tirtharaj\\excel-to-database-to-excel\\Imported Medical table.csv")
json_file_1 = FromDBToExcel.to_json(orient="records")
with open('Imported Medical table_1.json', 'w') as f:
    f.write(json_file_1)


json_file_2 = FromDBToExcel.to_json(orient="index")
with open('Imported Medical table_2.json', 'w') as f:
    f.write(json_file_2)


