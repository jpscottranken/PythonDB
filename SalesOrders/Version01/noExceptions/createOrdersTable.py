import sqlite3

# Step 8.  Function createOrdersTable()
#
# This function will attempt to create
# a database table.
def createOrdersTable(conn):
  try:
    c = conn.cursor()
    createOrdersTableQuery = """
        CREATE TABLE IF NOT EXISTS orders
        (
          OrderID  					  INTEGER			PRIMARY KEY,
          OrderDate 					TEXT	 		  NULL,
          OrderShipDate 		  TEXT	 		  NULL,
          CustomerID 					INTEGER			NULL,
          EmployeeID 					INTEGER			NULL 
        )
    """

    c.execute(createOrdersTableQuery)
    conn.commit()
    print(f"\nOrders table successfully created.")
  except sqlite3.Error as e:
    print(f"\nProblem trying to create database table: {e}")
    return None