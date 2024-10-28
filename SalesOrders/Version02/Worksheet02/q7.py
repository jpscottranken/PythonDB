import sqlite3

def runQ7(conn):
  # Show a query that gives the customer first name, 
  # customer last name, order date, ship date, retail 
  # price, and quoted price for those records where the 
  # quoted price is not equal to the retail price.
  # 
  # Sort by order number in ascending order.
  try:
    c = conn.cursor()

    q7Query = """
                  SELECT		c.CustomerFirstName,
                            c.CustomerLastName,
                            date(o.orderdate),
                            date(o.ordershipdate),
                            p.productprice, 
                            od.orderdetailquotedprice
                  FROM		customers c
                  JOIN		orders o		ON c.CustomerID	= o.CustomerID
                  JOIN		orderDetails od	ON o.OrderID	= od.OrderID
                  JOIN		products p	ON od.productID	= p.productID
                  WHERE		od.OrderDetailQuotedPrice <> p.ProductPrice
                  ORDER BY	o.orderID

              """
    c.execute(q7Query)   
    print("\nQ7. Quoted Price Not Equal To Product Price:")
    print(c.fetchall())
  except sqlite3.Error as e:
    print(f"\nQ7. Problem trying to display database records: {e}")
    return None