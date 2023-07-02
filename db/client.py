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
        return self.client
    
    def get_cursor(self):
        return self.client.cursor()
