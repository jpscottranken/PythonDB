import sqlite3

# Step 5.  Function createVendorsTable()
#
# This function will attempt to create
# a database table.
def createVendorsTable(conn):
  try:
    c = conn.cursor()
    createVendorsTableQuery = """
        CREATE TABLE IF NOT EXISTS vendors
        (
          VendorID 					    INTEGER			PRIMARY KEY,
          VendorName 					  TEXT			  NULL,
          VendorStreetAddress   TEXT			  NULL,
          VendorCity 					  TEXT			  NULL,
          VendorState 				  TEXT			  NULL,
          VendorZipCode 				TEXT			  NULL,
          VendorPhoneNumber 	  TEXT			  NULL,
          VendorFaxNumber 			TEXT			  NULL,
          VendorWebPage 				TEXT 			  NULL,
          VendorEMailAddress 	  TEXT			  NULL 
        )
    """

    c.execute(createVendorsTableQuery)
    conn.commit()
    print(f"\nVendors table successfully created.")
  except sqlite3.Error as e:
    print(f"\nProblem trying to create database table: {e}")
    return None