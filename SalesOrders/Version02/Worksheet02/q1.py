import sqlite3

def runQ1(conn):
  # Show a query that will tell whether or not 
  # any employee has a telephone number.  Include the
  # employee first name and last name in the query results.
  try:
    c = conn.cursor()

    q1Query = """
                  SELECT	EmployeeFirstName,
	                        EmployeeLastName
                  FROM	  Employees
                  WHERE	  EmployeePhoneNumber IS NULL                 
                    """
    c.execute(q1Query)   
    print("\nQ1. Those employees with no phone number:")
    print(c.fetchall())

    c.execute(q1Query)
    print("\nQ1. Those employees with no phone number:")
    rows = c.fetchall()
    for row in rows:
        print(f"Name: {row[1]} {row[2]}")
  except sqlite3.Error as e:
    print(f"\nQ1. Problem trying to display database records: {e}")
    return None