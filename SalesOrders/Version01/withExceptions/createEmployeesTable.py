import sqlite3

# Step 4.  Function createEmployeesTable()
#
# This function will attempt to create
# a database table.
def createEmployeesTable(conn):
  try:
    c = conn.cursor()
    createEmployeesTableQuery = """
        CREATE TABLE IF NOT EXISTS employees
        (
          EmployeeID 					    INTEGER			PRIMARY KEY,
          EmployeeFirstName 			TEXT			  NULL,
          EmployeeLastName 			  TEXT			  NULL,
          EmployeeStreetAddress   TEXT			  NULL,
          EmployeeCity 				    TEXT			  NULL,
          EmployeeState 			    TEXT			  NULL,
          EmployeeZipCode 			  TEXT 			  NULL,
          EmployeeAreaCode 			  TEXT	 		  NULL,
          EmployeePhoneNumber 		TEXT			  NULL
        )
    """

    c.execute(createEmployeesTableQuery)
    conn.commit()
    print(f"\nEmployees table successfully created.")
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