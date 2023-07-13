import pyodbc


class Client:
    def __init__(self, driver, server, database, port, user, password):
        connection_string = """DRIVER={{{driver}}};Server={server};Database={database};
                            Port={port};User ID={user};Password={password}""".format(
                                driver=driver,
                                server=server,
                                database=database,
                                port=port,
                                user=user,
                                password=password
                            )
        self.client = pyodbc.connect(connection_string)

    def get_connection(self):
        print('Connected to database!')
        return self.client

    def close_connection(self):
        if self.client:
            print('Closed connection!')
            return self.client.close()

    def get_cursor(self, query):
        cursor = self.client.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def update(self, query):
        cursor = self.client.cursor()
        cursor.execute(query)
        self.client.commit()
        cursor.close
        print('Update is succusfully!')