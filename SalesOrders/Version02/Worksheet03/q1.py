import sqlite3

def runQ1(conn):
  # Show a query that shows how many order 
  # dates from the 	orders 	table are incorrect (i.e. 
  # they are 0000-00-0000 00:00:00).
  # 
  # Please be aware: The answer to the query may be 0 (empty)
  try:
    c = conn.cursor()

    q1Query = """
                  SELECT OrderID, 
                         OrderDate
                  FROM   orders 
                  WHERE  OrderDate = '0000-00-00 00:00:00'                   
              """
    c.execute(q1Query)   
    print("\nQ1. Invalid Order Dates:")
    print(c.fetchall())
  except sqlite3.Error as e:
    print(f"\nQ1. Problem trying to display database records: {e}")
    return None