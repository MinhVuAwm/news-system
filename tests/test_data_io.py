from db import data_io
from db.client import Client


DB_CONFIG = {
    "driver": "",
    "sever": "",
    "database": "",
    "port": "",
    "user": "",
    "password": ""
}

client = Client(
    driver = DB_CONFIG["driver"],
    server = DB_CONFIG["server"],
    database = DB_CONFIG["database"],
    port = DB_CONFIG["port"],
    user = DB_CONFIG["user"],
    password = DB_CONFIG["password"]
)

cursor = client.get_cursor()

def test_get_news_by_id():
    news_id = 1
    data = data_io.get_news_by_id(news_id)
    print(data)


test_get_news_by_id()
