import sqlite3

def runQ17(conn):
  # Show a query to select all category descriptions, product names,
  # and retail prices, but only for a category description of neither
  # 'Wheels' nor 'Bikes'.
  #
  # Sort results by category description in ascending order, then
  # retail price in descending order.
  try:
    c = conn.cursor()

    q17Query = """
                  SELECT c.CategoryDescription, 
                         p.ProductName, 
                         p.ProductPrice
                  FROM products p
                  JOIN categories c ON p.CategoryID = c.CategoryID
                  WHERE c.CategoryDescription <> 'Wheels'
                  AND   c.CategoryDescription <> 'Bikes'
                  ORDER BY c.CategoryDescription ASC, 
			                     p.ProductPrice DESC;           
                    """

    c.execute(q17Query)   
    print("\nQ17 Results Formatted:")
    rows = c.fetchall()
    for row in rows:
        print(f"Category: {row[0]}\tProduct Name: {row[1]}\tProduct Price: ${row[2]}")
  except sqlite3.Error as e:
    print(f"\nQ17. Problem trying to display database records: {e}")
    return None