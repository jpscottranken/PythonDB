# Handle the CRUD operations for the OrderDetails
def createOrderDetail(cursor):
  # Input fields for new record
  orderID                     = input("Enter OrderDetails OrderID: ")
  productID                   = input("Enter OrderDetails ProductID: ")
  orderDetailQuotedPrice      = input("Enter OrderDetails Quoted Price: ")
  orderDetailQuantityOrdered  = input("Enter OrderDetail Qty Ordered: ")

  # Run the insert query
  cursor.execute("""
                      INSERT INTO orderDetails
                      (OrderID, ProductID,
                       OrderDetailQuotedPrice,
                       OrderDetailQuantityOrdered)
                      VALUES (?, ?, ?, ?)
                 """,
                (orderID, productID,
                 orderDetailQuotedPrice,
                 orderDetailQuantityOrdered))
  print("OrderDetail Created.")

def readOrderDetails(cursor):
  print("Here Are The OrderDetails: ")

  # Run the select query
  cursor.execute("SELECT * FROM OrderDetails")

  # Fetch all of the records found
  rows = cursor.fetchall()
  for row in rows:
    # Print all of the records found
    print(row)

def updateOrderDetail(cursor):
  print("NOTE: You CANNOT Update The OrderID/Product (PK)!")
  # Determine row to update
  orderID   = input("Enter OrderID   of record to update: ")
  productID = input("Enter ProductID of record to update: ")

  # Add updated fields
  newOrderDetailQuotedPrice      = input("Enter Updated OrderDetails Quoted Price: ")
  newOrderDetailQuantityOrdered  = input("Enter Updated OrderDetail Qty Ordered: ")


  # Update the database
  cursor.execute("""
                    UPDATE orderDetails
                    SET    OrderDetailQuotedPrice     = ?,
                           OrderDetailQuantityOrdered = ?
                    WHERE  OrderID                    = ?
                    AND    ProductID                  = ?
                """,
                (newOrderDetailQuotedPrice,
                newOrderDetailQuantityOrdered,
                orderID, productID,))

  print("OrderDetail Updated.")

def deleteOrderDetail(cursor):
  # Prompt for record to delete
  orderID   = input("Enter OrderID Of Record To Delete: ")
  productID = input("Enter ProductID Of Record To Delete: ")

  # Run the delete query
  cursor.execute("""
                    DELETE FROM orderDetails
                    WHERE OrderID   = ?
                    AND   ProductID = ?
                """,
                (orderID, productID),)

  print("OrderDetail Deleted.")
