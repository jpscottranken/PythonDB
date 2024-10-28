# Import the genericCRUD CRUD modules
from modules.genericCRUD.crudFunctions import updateRecord
from modules.genericCRUD.crudFunctions import readRecords
from modules.genericCRUD.crudFunctions import deleteRecord

# Handle the CRUD operations for the Orders table
def createOrder(cursor):
  # Input fields for new record
  orderDate       = input("Enter Orders Date: ")
  orderShipDate   = input("Enter Orders Ship Date: ") 
  customerID      = input("Enter Orders CustomerID: ")
  employeeID      = input("Enter Orders EmployeeID: ")

  # Run the insert query
  cursor.execute("""
                      INSERT INTO orders
                      (OrderDate, OrderShipDate,
                       CustomerID, EmployeeID)
                      VALUES (?, ?, ?, ?)
                 """,
                (orderDate, orderShipDate,
                 customerID, employeeID))

  print("Order Created.")

def readOrders(cursor):
  readRecords(cursor, "Orders")

def updateOrder(conn, cursor):
  updateRecord(conn, cursor, "Orders", ['OrderID'],
               ['OrderDate', 'OrderShipDate',
                'CustomerID', 'EmployeeID'])

def deleteOrder(conn, cursor):
  orderIDValue = input("Enter the number (OrderID) of the record to delete: ")

  # Then pass it into the deleteRecord function
  primaryKeys = {"OrderID": orderIDValue}
  deleteRecord(conn, cursor, "Orders", primaryKeys)
    