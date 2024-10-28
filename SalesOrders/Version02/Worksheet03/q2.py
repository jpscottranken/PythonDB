import sqlite3

def runQ2(conn):
  # Show a query that shows how many orderShipDates 
  # dates from the 	orders 	table are incorrect (i.e. 
  # they are 0000-00-0000 00:00:00).
  # 
  # Please be aware: The answer to the query may be 0 (empty)
  try:
    c = conn.cursor()

    q2Query = """
                  SELECT OrderID, 
                         OrderShipDate
                  FROM   orders 
                  WHERE  OrderShipDate = '0000-00-00 00:00:00'                   
              """
    c.execute(q2Query)   
    print("\nQ2. Invalid Ship Dates:")
    print(c.fetchall())
  except sqlite3.Error as e:
    print(f"\nQ2. Problem trying to display database records: {e}")
    return None