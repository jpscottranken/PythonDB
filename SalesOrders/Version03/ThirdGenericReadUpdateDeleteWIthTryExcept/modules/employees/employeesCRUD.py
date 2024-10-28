# Import the genericCRUD CRUD modules
from modules.genericCRUD.crudFunctions import updateRecord
from modules.genericCRUD.crudFunctions import readRecords
from modules.genericCRUD.crudFunctions import deleteRecord

# Handle the CRUD operations for the Employee table
def createEmployee(cursor):
  # Input fields for new record
  employeeFirstName       = input("Enter Employee First Name: ")
  employeeLastName        = input("Enter Employee Last  Name: ") 
  employeeStreetAddress   = input("Enter Employee Street Address: ")
  employeeCity            = input("Enter Employee City: ")
  employeeState           = input("Enter Employee State: ")
  employeeZipCode         = input("Enter Employee Zip Code: ")
  employeeAreaCode        = input("Enter Employee Area Code: ")
  employeePhoneNumber     = input("Enter Employee Phone Number: ") 

  # Run the insert query
  cursor.execute("""
                      INSERT INTO employees
                      (EmployeeFirstName, EmployeeLastName,
                       EmployeeStreetAddress,
                       EmployeeCity, EmployeeState, EmployeeZipCode,
                       EmployeeAreaCode, EmployeePhoneNumber)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                 """,
                (employeeFirstName, employeeLastName,
                 employeeStreetAddress,
                 employeeCity, employeeState, employeeZipCode,
                 employeeAreaCode, employeePhoneNumber,))
  print("Employee Created.")

def readEmployees(cursor):
  readRecords(cursor, "Employees")

def updateEmployee(conn, cursor):
  updateRecord(conn, cursor, "Employees", ['EmployeeID'],
               ['EmployeeFirstName', 'EmployeeLastName',
                'EmployeeStreetAddress',
                'EmployeeCity', 'EmployeeState', 'EmployeeZipCode',
                'EmployeeAreaCode', 'EmployeePhoneNumber'])

def deleteEmployee(conn, cursor):
  employeeIDValue = input("Enter the number (EmployeeID) of the record to delete: ")

  # Then pass it into the deleteRecord function
  primaryKeys = {"EmployeeID": employeeIDValue}
  deleteRecord(conn, cursor, "Employees", primaryKeys)
