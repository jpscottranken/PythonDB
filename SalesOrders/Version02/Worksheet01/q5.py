import sqlite3

def ordersRecordCount(conn):
  try:
    c = conn.cursor()

    # Get a count of the number of records in the orders table
    numberOrderRecords =   """
                                SELECT COUNT(*)
                                FROM   orders
                           """
    c.execute(numberOrderRecords)   
    print("\nQ5. The number of records in the orders table via fetchall:")
    print(c.fetchone())
  except sqlite3.Error as e:
    print(f"\nQ5. Problem trying to insert database records: {e}")
    return None