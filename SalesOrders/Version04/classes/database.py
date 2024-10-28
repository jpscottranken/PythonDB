#	classes/database.py:
import sqlite3

class Database:
    def __init__(self, dbName="SalesOrders.db"):
        self.connection = sqlite3.connect(dbName)
        self.cursor = self.connection.cursor()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()