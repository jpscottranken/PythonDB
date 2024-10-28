import sqlite3

# Step 9.  Function createOrderDetailsTable()
#
# This function will attempt to create
# a database table.
def createOrderDetailsTable(conn):
  try:
    c = conn.cursor()
    createOrderDetailsTableQuery = """
        CREATE TABLE IF NOT EXISTS orderDetails
        (
          OrderID 					          INTEGER,
          ProductID 					        INTEGER 		  NOT NULL,
          OrderDetailQuotedPrice 		  NUMBER (15,2) 	  NULL,
          OrderDetailQuantityOrdered 	INTEGER			      NULL,
          PRIMARY KEY (OrderID, ProductID) 
        )
    """

    c.execute(createOrderDetailsTableQuery)
    conn.commit()
    print(f"\nOrderDetails table successfully created.")
  except sqlite3.Error as e:
    print(f"\nProblem trying to create database table: {e}")
    return None