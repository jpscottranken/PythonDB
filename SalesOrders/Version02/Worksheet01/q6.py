import sqlite3

def productsRecordCount(conn):
  try:
    c = conn.cursor()

    # Get a count of the number of records in the products table
    numberProductRecords =   """
                                SELECT COUNT(*)
                                FROM   products
                              """
    c.execute(numberProductRecords)   
    print("\nQ6. The number of records in the products table via fetchall:")
    print(c.fetchone())
  except sqlite3.Error as e:
    print(f"\nQ6. Problem trying to insert database records: {e}")
    return None