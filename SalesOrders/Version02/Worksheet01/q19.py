import sqlite3

def runQ19(conn):
  # Do a Union query to combine all customer first and last names
  # with all employee first and last names.
  try:
    c = conn.cursor()

    q19Query =  """   
                    SELECT  c.customerfirstname, c.customerlastname
                    FROM    customers c
                    UNION
                    SELECT  e.employeefirstname, e.employeelastname
                    FROM    employees	 e         
                """
    
    c.execute(q19Query)   
    print("\nQ19 Results - Customer/Employee Name List:")
    rows = c.fetchall()
    for row in rows:
        print(f"Name: {row[0]} {row[1]}")
  except sqlite3.Error as e:
    print(f"\nProblem trying to display database records: {e}")
    return None