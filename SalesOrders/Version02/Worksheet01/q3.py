import sqlite3

def employeesRecordCount(conn):
  try:
    c = conn.cursor()

    # Get a count of the number of records in the employees table
    numberEmployeeRecords =   """
                                SELECT COUNT(*)
                                FROM   employees
                              """
    c.execute(numberEmployeeRecords)   
    print("\nQ3. The number of records in the employees table via fetchall:")
    print(c.fetchone())
  except sqlite3.Error as e:
    print(f"\nQ3. Problem trying to insert database records: {e}")
    return None