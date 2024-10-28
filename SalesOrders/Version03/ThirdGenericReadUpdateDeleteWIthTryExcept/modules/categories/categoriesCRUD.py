# Import the genericCRUD CRUD modules
#from modules.genericCRUD.crudFunctions import createRecord
from modules.genericCRUD.crudFunctions import readRecords
from modules.genericCRUD.crudFunctions import updateRecord
from modules.genericCRUD.crudFunctions import deleteRecord

# Handle the CRUD operations for the Categories table
def createCategory(cursor):
  # Input field for new record
  categoryDescription = input("Enter Category Description: ")

  # Run the insert query
  cursor.execute("""
                      INSERT INTO categories
                      (CategoryDescription)
                      VALUES (?)
                 """,
                (categoryDescription,))
  
  print("Category Created.")

def readCategories(cursor):
  readRecords(cursor, "Categories")

def updateCategory(conn, cursor):
  updateRecord(conn, cursor, "Categories", ['CategoryID'],
               ['CategoryDescription'])

def deleteCategory(conn, cursor):
  categoryIDValue = input("Enter the number (CategoryID) of the record to delete: ")

  # Then pass it into the deleteRecord function
  primaryKeys = {"CategoryID": categoryIDValue}
  deleteRecord(conn, cursor, "Categories", primaryKeys)
