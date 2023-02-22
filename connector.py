import mysql.connector

class UrlQueue:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS UrlQueue (id INT AUTO_INCREMENT PRIMARY KEY, url VARCHAR(2048))")

    def put(self, url):
        request = "INSERT INTO UrlQueue (url) VALUES (%s)"
        values = (url,)
        self.cursor.execute(request, values)
        self.db.commit()

    def get(self):
        request = "SELECT url FROM UrlQueue LIMIT 1 FOR UPDATE"
        self.cursor.execute(request)
        result = self.cursor.fetchone()
        if result is None:
            return None
        url = result[0]
        delete_request = "DELETE FROM UrlQueue WHERE url = %s"
        self.cursor.execute(delete_request, (url,))
        self.db.commit()
        return url

class DataStore:


    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Datastore (id INT AUTO_INCREMENT PRIMARY KEY, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, url VARCHAR(255),keywords VARCHAR(255));")


    def add_data(self, url, keywords=None):
        if keywords is not None:
            request = "INSERT INTO Datastore (url, keywords) VALUES (%s, %s)"
            values = (url, keywords)
        else:
            request = "INSERT INTO Datastore (url) VALUES (%s)"
            values = (url,)
        self.cursor.execute(request, values)
        self.db.commit()

    '''def delete_data(self, id):
        request = "DELETE FROM Datastore WHERE id = %s"
        values = (id,)
        self.cursor.execute(request, values)
        self.db.commit()'''