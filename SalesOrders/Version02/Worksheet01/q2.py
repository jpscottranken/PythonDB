import sqlite3

def customersRecordCount(conn):
  try:
    c = conn.cursor()

    # Get a count of the number of records in the categories table
    numberCustomerRecords =   """
                                SELECT COUNT(*)
                                FROM   customers
                              """
    c.execute(numberCustomerRecords)   
    print("\nQ2. The number of records in the customers table via fetchall:")
    print(c.fetchone())
  except sqlite3.Error as e:
    print(f"\nQ2. Problem trying to insert database records: {e}")
    return None