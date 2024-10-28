# Import the genericCRUD CRUD modules
from modules.genericCRUD.crudFunctions import updateRecord

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
  updateRecord(cursor, "OrderDetails", ['OrderID', 'ProductID'],
               ['OrderDetailQuotedPrice',
                'OrderDetailQuantityOrdered'])

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
