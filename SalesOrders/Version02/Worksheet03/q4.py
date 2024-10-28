import sqlite3

def runQ4(conn):
  # Show a query to show the total number of employees per state.
  # Include both the state name and the count in your answer.
  # 
  # Order the result by the count in descending 	order.
  try:
    c = conn.cursor()

    q4Query = """
                  SELECT  EmployeeState,
                          count(EmployeeState)
                  FROM    employees
                  GROUP BY EmployeeState
                  ORDER BY count(EmployeeState) DESC;                   
              """
    c.execute(q4Query)   
    print("\nQ4. Total Number Employees Per State:")
    print(c.fetchall())
  except sqlite3.Error as e:
    print(f"\nQ4. Problem trying to display database records: {e}")
    return None