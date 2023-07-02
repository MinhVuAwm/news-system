from db.client import Client


def get_news_by_id(cursor, news_id):
    """Lấy bài báo theo id trong database

    Args:
        cursor (pyodbc cursor): cursor tạo ra từ connection để thao tác với cơ sở dữ liệu
        news_id (int): news id

    Returns:
        dictionary: ...
    """
    pass


def get_news_in_range_date(cursor, from_date, to_date):
    """Lấy các bài báo từ from_date đến to_date

    Args:
        cursor (pyodbc cursor): cursor tạo ra từ connection để thao tác với cơ sở dữ liệu
        from_date (datetime): ngày bắt đầu lấy dữ liệu
        to_date (datetime): ngày cuối cùng lấy dữ liệu
    
    Returns:
        dictionary: ...
    """
    pass
