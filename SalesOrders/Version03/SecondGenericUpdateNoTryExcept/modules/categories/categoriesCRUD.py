# Import the genericCRUD CRUD modules
from modules.genericCRUD.crudFunctions import updateRecord

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
  print("Here Are The Categories: ")

  # Run the select query
  cursor.execute("SELECT * FROM categories")

  # Fetch all of the records found
  rows = cursor.fetchall()
  for row in rows:
    # Print all of the records found
    print(row)

def updateCategory(cursor):
  updateRecord(cursor, "Categories", ['CategoryID'],
               ['CategoryDescription'])

def deleteCategory(cursor):
  # Prompt for record to delete
  categoryID = input("Enter CategoryID Of Record To Delete: ")

  # Run the delete query
  cursor.execute("""
                    DELETE FROM categories
                    WHERE CategoryID = ?
                """,
                (categoryID,))
  
  print ("Category Deleted.")
