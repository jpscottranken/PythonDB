import sqlite3

def vendorsRecordCount(conn):
  try:
    c = conn.cursor()

    # Get a count of the number of records in the categories table
    numberVendorRecords =   """
                                SELECT COUNT(*)
                                FROM   vendors
                              """
    c.execute(numberVendorRecords)   
    print("\nQ8. The number of records in the vendors table via fetchall:")
    print(c.fetchone())
  except sqlite3.Error as e:
    print(f"\nQ8. Problem trying to insert database records: {e}")
    return None