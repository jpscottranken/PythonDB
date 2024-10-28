import sqlite3

# Step 6.  Function createProductsTable()
#
# This function will attempt to create
# a database table.
def createProductsTable(conn):
  try:
    c = conn.cursor()
    createProductsTableQuery = """
        CREATE TABLE IF NOT EXISTS products
        (
          ProductID 					  INTEGER			    PRIMARY KEY,
          ProductName 				  TEXT			      NULL,
          ProductDescShort 			TEXT			      NULL,
          ProductDescLong 			TEXT 			      NULL,
          ProductImage				  TEXT			      NULL,
          ProductPrice 				  NUMBER (15,2) 	NULL,
          ProductQty 					  INTEGER			    NULL,
          CategoryID 					  INTEGER			    NULL 
        )
    """

    c.execute(createProductsTableQuery)
    conn.commit()
    print(f"\nProducts table successfully created.")
  except sqlite3.Error as e:
    print(f"\nProblem trying to create database table: {e}")
    return None