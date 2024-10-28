import sqlite3

def runQ6(conn):
  # Select one field from each of the tables as follows: 
  # order date (cast as date), ship date (cast as date), 
  # quantity ordered, wholesale price, retail price, 
  # quoted price, category description, and vendor 
	# name where the vendor name begins with an 'A' and 
  # the quoted price > 150.00.
  # 
  # Order the results by category description
	# ascending, then quoted price descending.
  try:
    c = conn.cursor()

    q6Query = """
                  SELECT o.OrderDate, 
                         o.OrderShipDate, 
                         od.OrderDetailQuantityOrdered, 
                         pv.ProductVendorWholesalePrice, 
                         p.ProductPrice, 
                         od.OrderDetailQuotedPrice, 
                         c.CategoryDescription, 
                         v.VendorName
                  FROM Orders o
                  JOIN OrderDetails od  ON o.OrderID    = od.OrderID
                  JOIN Products p       ON od.ProductID = p.ProductID
                  JOIN ProductVendors pv ON p.ProductID = pv.ProductID
                  JOIN Categories c     ON p.CategoryID = c.CategoryID
                  JOIN Vendors v        ON pv.VendorID  = v.VendorID
                  WHERE v.VendorName LIKE 'A%' 
                  AND od.OrderDetailQuotedPrice > 150.00
                  ORDER BY c.CategoryDescription ASC, 
                           od.OrderDetailQuotedPrice DESC;
              """
    c.execute(q6Query)   
    print("\nQ6. Big Query 1 Results:")
    print(c.fetchall())
  except sqlite3.Error as e:
    print(f"\nQ6. Problem trying to display database records: {e}")
    return None