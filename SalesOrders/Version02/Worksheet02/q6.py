import sqlite3

def runQ6(conn):
  # Show a query to show the vendor name, product name, 
  # quantity ordered, and quantity on hand, where the 
  # quantity ordered is greater than the quantity on hand. 
  # No repeats for vendor name allowed.
  try:
    c = conn.cursor()

    q6Query = """
                    SELECT  	DISTINCT(v.VendorName),
                              p.ProductName,
                              od.OrderDetailQuantityOrdered,
                              p.ProductQty
                    FROM	vendors v
                    JOIN	productVendors pv 	ON v.VendorID    = pv.VendorID
                    JOIN	products p	ON pv.ProductID = p.ProductID
                    JOIN	orderDetails od	ON p.ProductID   = od.ProductID
                    WHERE	od.OrderDetailQuantityOrdered > p.ProductQty
              """
    c.execute(q6Query)   
    print("\nQ6. Product Info Where Quantity Ordered > Quantity On Hand:")
    print(c.fetchall())
  except sqlite3.Error as e:
    print(f"\nQ6. Problem trying to display database records: {e}")
    return None