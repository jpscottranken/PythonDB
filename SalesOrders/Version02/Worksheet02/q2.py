import sqlite3

def runQ2(conn):
  # Show a query that a query that shows the total quantity 
  # on hand for each category.
  try:
    c = conn.cursor()

    q2Query = """
                  SELECT 	c.CategoryDescription,
       		                SUM(p.ProductQty)
                  FROM   	categories c
                  JOIN    products p ON c.CategoryID = p.CategoryID
                  GROUP BY 	c.CategoryID        
              """
    c.execute(q2Query)   
    print("\nQ2. Total Qty On Hand For Each Category:")
    print(c.fetchall())
  except sqlite3.Error as e:
    print(f"\nQ2. Problem trying to display database records: {e}")
    return None