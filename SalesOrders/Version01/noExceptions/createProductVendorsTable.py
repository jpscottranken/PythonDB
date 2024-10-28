import sqlite3

# Step 7.  Function createProductVendorsTable()
#
# This function will attempt to create
# a database table.
def createProductVendorsTable(conn):
  try:
    c = conn.cursor()
    createProductVendorsTableQuery = """
        CREATE TABLE IF NOT EXISTS productVendors
        (
          ProductID  					        INTEGER,
          VendorID 					          INTEGER		      NOT NULL,
          ProductVendorWholesalePrice	NUMBER (15,2) 	NULL,
          ProductVendorDaysToDeliver	INTEGER 		    NULL,
          PRIMARY KEY (ProductID, VendorID)
        )
    """

    c.execute(createProductVendorsTableQuery)
    conn.commit()
    print(f"\nProductVendors table successfully created.")
  except sqlite3.Error as e:
    print(f"\nProblem trying to create database table: {e}")
    return None