import sqlite3

def runQ3(conn):
  # Show a query that shows the total number of customers per state.
  # Include both the state name and the count in your answer.
  # 
  # Order the result by the count in descending order.
  try:
    c = conn.cursor()

    q3Query = """
                  SELECT  CustomerState,
                          count(CustomerState)
                  FROM    customers
                  GROUP BY CustomerState
                  ORDER BY count(CustomerState) DESC;                   
              """
    c.execute(q3Query)   
    print("\nQ3. Total Number Customers Per State:")
    print(c.fetchall())
  except sqlite3.Error as e:
    print(f"\nQ3. Problem trying to display database records: {e}")
    return None