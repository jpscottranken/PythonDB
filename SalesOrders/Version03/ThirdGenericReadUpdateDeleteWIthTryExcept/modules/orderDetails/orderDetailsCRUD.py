# Import the genericCRUD CRUD modules
from modules.genericCRUD.crudFunctions import updateRecord
from modules.genericCRUD.crudFunctions import readRecords
from modules.genericCRUD.crudFunctions import deleteRecord

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
  readRecords(cursor, "OrderDetails")

def updateOrderDetail(conn, cursor):
  updateRecord(conn, cursor, "OrderDetails", ['OrderID', 'ProductID'],
               ['OrderDetailQuotedPrice',
                'OrderDetailQuantityOrdered'])

def deleteOrderDetail(conn, cursor):
    orderIDValue   = input("Enter the number (OrderID)   of the record to delete: ")
    productIDValue = input("Enter the number (ProductID) of the record to delete: ")

    # Then pass it into the deleteRecord function
    primaryKeys = {"OrderID": orderIDValue, "ProductID": productIDValue}
    deleteRecord(conn, cursor, "OrderDetails", primaryKeys)

