import sqlite3

def runQ7(conn):
  # Show a query where you select one field from each 
  # of the tables as follows: customerid, employeeid, 
  # shipdate (cast as date), wholesaleprice, retailprice, 
  # quotedprice, category description, and vendorid where 
  # the quotedprice  is not equal to the retailprice and 
  # the wholesaleprice is between 125.00 and 130.00 and 
  # the employeeid is equal to 705.
  # 
  # Order the results by categorydescription, then 
  # customerid, both in ascending order.

  try:
    c = conn.cursor()

    q7Query = """
                  SELECT  o.CustomerID, 
                          o.EmployeeID, 
                          o.OrderShipDate, 
                          pv.ProductVendorWholesalePrice,
                          p.ProductPrice,
                          od.OrderDetailQuotedPrice, 
                          c.CategoryDescription,
                          pv.VendorID
                  FROM Orders o
                  JOIN OrderDetails od    ON o.OrderID    = od.OrderID
                  JOIN Products p         ON od.ProductID = p.ProductID
                  JOIN ProductVendors pv  ON p.ProductID  = pv.ProductID
                  JOIN Categories c       ON p.CategoryID = c.CategoryID
                  WHERE od.OrderDetailQuotedPrice != p.ProductPrice
                  AND pv.ProductVendorWholesalePrice BETWEEN 125.00 AND 130.00
                  AND o.EmployeeID = 705
                  ORDER BY c.CategoryDescription ASC,
                           o.CustomerID ASC;
              """
    c.execute(q7Query)   
    print("\nQ7. Big Query2 Results:")
    print(c.fetchall())
  except sqlite3.Error as e:
    print(f"\nQ7. Problem trying to display database records: {e}")
    return None