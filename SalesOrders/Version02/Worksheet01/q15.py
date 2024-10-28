import sqlite3

def runQ15(conn):
  # Show a query to select all category descriptions, product names,
  # and retail prices.
  #
  # Sort results by category description in ascending order, then
  # retail price in descending order.
  try:
    c = conn.cursor()

    q15Query = """
                  SELECT c.CategoryDescription, 
                         p.ProductName, 
                         p.ProductPrice
                  FROM products p
                  JOIN categories c ON p.CategoryID = c.CategoryID
                  ORDER BY c.CategoryDescription ASC, 
			                     p.ProductPrice DESC;           
                    """

    c.execute(q15Query)   
    print("\nQ15 Results Formatted:")
    rows = c.fetchall()
    for row in rows:
        print(f"Category: {row[0]}\tProduct Name: {row[1]}\tProduct Price: ${row[2]}")
  except sqlite3.Error as e:
    print(f"\nQ15. Problem trying to display database records: {e}")
    return None