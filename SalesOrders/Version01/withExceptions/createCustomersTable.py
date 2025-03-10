import sqlite3

# Step 3.  Function createCustomersTable()
#
# This function will attempt to create
# a database table.
def createCustomersTable(conn):
  try:
    c = conn.cursor()
    createCustomersTableQuery = """
        CREATE TABLE IF NOT EXISTS customers
        (
          CustomerID 					    INTEGER 		PRIMARY KEY,
          CustomerFirstName 			TEXT			  NULL,
          CustomerLastName 			  TEXT 			  NULL,
          CustomerStreetAddress   TEXT			  NULL,
          CustomerCity 				    TEXT			  NULL,
          CustomerState 				  TEXT			  NULL,
          CustomerZipCode 			  TEXT			  NULL,
          CustomerAreaCode 			  TEXT	 		  NULL,
          CustomerPhoneNumber 		TEXT			  NULL 
        )
    """

    c.execute(createCustomersTableQuery)
    conn.commit()
    print(f"\nCustomers table successfully created.")
  except sqlite3.DatabaseError as e:
    print(f"\nDatabase Error: {e}")
    return None
  except sqlite3.OperationalError as e:
    print(f"\nOperational Error: {e}")
    return None
  except sqlite3.ProgrammingError as e:
    print(f"\Programming Error: {e}")
    return None
  except sqlite3.Error as e:
    print(f"\nGeneric SQLite3 Error: {e}")
    return None