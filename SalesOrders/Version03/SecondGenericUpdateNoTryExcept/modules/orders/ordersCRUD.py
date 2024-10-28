# Import the genericCRUD CRUD modules
from modules.genericCRUD.crudFunctions import updateRecord

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
  print("Here Are The Orders: ")

  # Run the select query
  cursor.execute("SELECT * FROM Orders")

  # Fetch all of the records found
  rows = cursor.fetchall()
  for row in rows:
    # Print all of the records found
    print(row)

def updateOrder(cursor):
  updateRecord(cursor, "Orders", ['OrderID'],
               ['OrderDate', 'OrderShipDate',
                'CustomerID', 'EmployeeID'])

def deleteOrder(cursor):
  # Prompt for record to delete
  orderID = input("Enter OrderID Of Record To Delete: ")

  # Run the delete query
  cursor.execute("""
                    DELETE FROM orders
                    WHERE OrderID = ?
                """,
                (orderID,))

  print("Order Deleted.")
