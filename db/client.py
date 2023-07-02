import pyodbc
import pandas as pd

# Định nghĩa một class gồm các method để connect và thao tác với database

class Client:
    def __init__(self, connection_string):
        connection = pyodbc.connect(connection_string)
        self.client = connection
        print('Connected to Database!')

    def query_sql(self,query):
        sql_query = pd.read_sql(query, self.client)
        return sql_query

    def update(self, table, values):
        sql_statetment = pd.read_sql(f'SELECT * FROM {table}', self.client)
        df1 = pd.DataFrame(sql_statetment)
        df_update = df1.update(values)
        print('update succussfully!')

    def delete(self, table, del_statement):
        sql_statement = pd.read_sql(f'SELECT * FROM {table}', self.client)
        df1 = pd.DataFrame(sql_statement)
        df_delete = df1.drop(del_statement)
        print('delete succussfully!')

    def is_exist_record(self, id, table):
        sql_statement = pd.read_sql(f'SELECT id FROM {table}', self.client)
        for i in sql_statement:
            if i == id:
                print('id is exist')
                return False
            return True
        # kiểm tra xem bài báo có id như này đã tồn tại chưa
