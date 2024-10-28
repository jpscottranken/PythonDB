# This function will attempt to create
# and return a database connection.
import sqlite3
def createConnection():
  try:
    conn = sqlite3.connect("salesOrders.db")
    print(f"\nDatabase connection established.")
    return conn
  except sqlite3.Error as e:
    print(f"\nProblem trying to create database connection: {e}")
    return None