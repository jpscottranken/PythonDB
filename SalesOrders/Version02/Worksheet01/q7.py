import sqlite3

def productVendorsRecordCount(conn):
  try:
    c = conn.cursor()

    # Get a count of the number of records in the productVendors table
    numberproductVendorsRecords =   """
                                SELECT COUNT(*)
                                FROM   productVendors
                              """
    c.execute(numberproductVendorsRecords)   
    print("\nQ7. The number of records in the productVendors table via fetchall:")
    print(c.fetchone())
  except sqlite3.Error as e:
    print(f"\nQ7. Problem trying to insert database records: {e}")
    return None