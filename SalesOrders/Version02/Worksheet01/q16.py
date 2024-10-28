import sqlite3

def runQ16(conn):
  # Show a query to select all category descriptions, product names,
  # and retail prices, but only for a category description of either
  # 'Wheels' or 'Bikes'.
  #
  # Sort results by category description in ascending order, then
  # retail price in descending order.
  try:
    c = conn.cursor()

    q16Query = """
                  SELECT c.CategoryDescription, 
                         p.ProductName, 
                         p.ProductPrice
                  FROM products p
                  JOIN categories c ON p.CategoryID = c.CategoryID
                  WHERE c.CategoryDescription = 'Wheels'
                  OR    c.CategoryDescription = 'Bikes'
                  ORDER BY c.CategoryDescription ASC, 
			                     p.ProductPrice DESC;           
                    """

    c.execute(q16Query)   
    print("\nQ16 Results Formatted:")
    rows = c.fetchall()
    for row in rows:
        print(f"Category: {row[0]}\tProduct Name: {row[1]}\tProduct Price: ${row[2]}")
  except sqlite3.Error as e:
    print(f"\nQ16. Problem trying to display database records: {e}")
    return None