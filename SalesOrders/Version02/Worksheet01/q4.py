import sqlite3

def orderDetailsRecordCount(conn):
  try:
    c = conn.cursor()

    # Get a count of the number of records in the orderDetails table
    numberorderDetailsRecords =   """
                                    SELECT COUNT(*)
                                    FROM   orderDetails
                                  """
    c.execute(numberorderDetailsRecords)   
    print("\nQ4. The number of records in the orderDetails table via fetchall:")
    print(c.fetchone())
  except sqlite3.Error as e:
    print(f"\nQ4. Problem trying to insert database records: {e}")
    return None