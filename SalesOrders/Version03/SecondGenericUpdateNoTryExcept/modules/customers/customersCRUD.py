# Import the genericCRUD CRUD modules
from modules.genericCRUD.crudFunctions import updateRecord

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
  print("Here Are The Customers: ")

  # Run the select query
  cursor.execute("SELECT * FROM customers")

  # Fetch all of the records found
  rows = cursor.fetchall()
  for row in rows:
    # Print all of the records found
    print(row)

def updateCustomer(cursor):
  updateRecord(cursor, "Customers", ['CustomerID'],
               ['CustomerFirstName', 'CustomerLastName',
                'CustomerStreetAddress',
                'CustomerCity', 'CustomerState', 'CustomerZipCode',
                'CustomerAreaCode', 'CustomerPhoneNumber'])

def deleteCustomer(cursor):
  # Prompt for record to delete
  customerID = input("Enter CustomerID Of Record To Delete: ")

  # Run the delete query
  cursor.execute("""
                    DELETE FROM customers
                    WHERE CustomerID = ?
                """,
                (customerID,))
  print ("Customer Deleted.")
