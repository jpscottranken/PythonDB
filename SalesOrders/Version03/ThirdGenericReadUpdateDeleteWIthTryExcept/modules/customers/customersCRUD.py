# Import the genericCRUD CRUD modules
from modules.genericCRUD.crudFunctions import updateRecord
from modules.genericCRUD.crudFunctions import readRecords
from modules.genericCRUD.crudFunctions import deleteRecord

# Handle the CRUD operations for the Customers table
def createCustomer(cursor):
  # Input fields for new record
  customerFirstName       = input("Enter Customer First Name: ")
  customerLastName        = input("Enter Customer Last  Name: ") 
  customerStreetAddress   = input("Enter Customer Street Address: ")
  customerCity            = input("Enter Customer City: ")
  customerState           = input("Enter Customer State: ")
  customerZipCode         = input("Enter Customer Zip Code: ")
  customerAreaCode        = input("Enter Customer Area Code: ")
  customerPhoneNumber     = input("Enter Customer Phone Number: ") 

  # Run the insert query
  cursor.execute("""
                      INSERT INTO customers
                      (CustomerFirstName, CustomerLastName,
                       CustomerStreetAddress,
                       CustomerCity, CustomerState, CustomerZipCode,
                       CustomerAreaCode, CustomerPhoneNumber)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                 """,
                (customerFirstName, customerLastName,
                 customerStreetAddress,
                 customerCity, customerState, customerZipCode,
                 customerAreaCode, customerPhoneNumber,))
  print("Customer Created.")

def readCustomers(cursor):
  readRecords(cursor, "Customers")

def updateCustomer(conn, cursor):
  updateRecord(conn, cursor, "Customers", ['CustomerID'],
               ['CustomerFirstName', 'CustomerLastName',
                'CustomerStreetAddress',
                'CustomerCity', 'CustomerState', 'CustomerZipCode',
                'CustomerAreaCode', 'CustomerPhoneNumber'])

def deleteCustomer(conn, cursor):
  customerIDValue = input("Enter the number (CustomerID) of the record to delete: ")

  # Then pass it into the deleteRecord function
  primaryKeys = {"CustomerID": customerIDValue}
  deleteRecord(conn, cursor, "Customers", primaryKeys)
