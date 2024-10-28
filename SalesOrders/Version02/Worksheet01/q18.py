import sqlite3

def runQ18(conn):
  # Write a query to select all category descriptions, 
  # product names, retail price, wholesale price, and
  # vendor name.
  # 
  # Sort results by category description in ascending 
  # order, then vendor name in descending order, then
  # retail price in descending order, then
  # wholesale price in descending order.
  try:
    c = conn.cursor()

    q18Query = """
                  SELECT c.CategoryDescription, p.ProductName, 
		                     p.ProductPrice, pv.ProductVendorWholesalePrice,
                         v.VendorName
	                FROM products p
	                JOIN categories c      ON p.CategoryID = c.CategoryID
                  JOIN productVendors pv ON pv.ProductID = p.ProductID
	                JOIN vendors v         ON pv.VendorID  = v.VendorID
                  ORDER BY c.CategoryDescription ASC, 
                      v.VendorName DESC, 
                      p.ProductPrice DESC, 
                      pv.ProductVendorWholesalePrice DESC;           
                    """

    c.execute(q18Query)   
    print("\nQ18 Results Formatted:")
    rows = c.fetchall()
    for row in rows:
        print(f"Category: {row[0]}  Product: {row[1]}  Retail: ${row[2]}  Wholesale: ${row[3]}  Vendor: {row[4]}")
  except sqlite3.Error as e:
    print(f"\nQ18. Problem trying to display database records: {e}")
    return None