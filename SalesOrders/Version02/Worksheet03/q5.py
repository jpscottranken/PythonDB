import sqlite3

def runQ5(conn):
  # Show a query that shows each category description, 
  # along with a count of the number of products in
  # that category description.
  # 
  # Sort by the count of the number of products 
  # descending and then category description ascending.
  try:
    c = conn.cursor()

    q5Query = """
                  SELECT c.CategoryDescription,
                         count(p.ProductID)
                  FROM   products   p
                  JOIN   categories c ON c.CategoryID = p.CategoryID
                  GROUP BY c.CategoryDescription
                  ORDER BY count(p.ProductID) DESC,
                           c.CategoryDescription;
                   
              """
    c.execute(q5Query)   
    print("\nQ5. Category Description And # Products:")
    print(c.fetchall())
  except sqlite3.Error as e:
    print(f"\nQ5. Problem trying to display database records: {e}")
    return None