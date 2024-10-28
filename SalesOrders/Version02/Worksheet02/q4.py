import sqlite3

def runQ4(conn):
  # Show a query that shows each separate product name 
  # (no repeats), along with the associated category 
  # description.
  # 
  # Sort by category description and then by product 
  # name, both in ascending order.
  try:
    c = conn.cursor()

    q4Query = """
                  SELECT 	DISTINCT(p.ProductName),
		                      c.CategoryDescription 
                  FROM		products p
                  JOIN		categories c ON p.CategoryID = c.CategoryID
                  ORDER BY 	c.CategoryDescription, p.ProductName;        
              """
    c.execute(q4Query)   
    print("\nQ4. Product Name And Associated Description:")
    print(c.fetchall())
  except sqlite3.Error as e:
    print(f"\nQ4. Problem trying to display database records: {e}")
    return None