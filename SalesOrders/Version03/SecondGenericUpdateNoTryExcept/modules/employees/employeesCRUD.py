# Import the genericCRUD CRUD modules
from modules.genericCRUD.crudFunctions import updateRecord

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
  print("Here Are The Employees: ")

  # Run the select query
  cursor.execute("SELECT * FROM employees")

  # Fetch all of the records found
  rows = cursor.fetchall()
  for row in rows:
    # Print all of the records found
    print(row)

def updateEmployee(cursor):
  updateRecord(cursor, "Employees", ['EmployeeID'],
               ['EmployeeFirstName', 'EmployeeLastName',
                'EmployeeStreetAddress',
                'EmployeeCity', 'EmployeeState', 'EmployeeZipCode',
                'EmployeeAreaCode', 'EmployeePhoneNumber'])

def deleteEmployee(cursor):
  # Prompt for record to delete
  employeeID = input("Enter EmployeeID Of Record To Felete: ")

  # Run the delete query
  cursor.execute("""
                    DELETE FROM employees
                    WHERE EmployeeID = ?
                """,
                (employeeID,))
  print ("Employee Deleted.")
