import sqlite3

def categoriesRecordCount(conn):
  try:
    c = conn.cursor()

    # Get a count of the number of records in the categories table
    numberCategoryRecords =   """
                                SELECT COUNT(*)
                                FROM   categories
                              """
    c.execute(numberCategoryRecords)   
    print("\nQ1. The number of records in the categories table via fetchall:")
    print(c.fetchone())
  except sqlite3.Error as e:
    print(f"\nQ1. Problem trying to insert database records: {e}")
    return None