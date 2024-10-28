import sqlite3

# https://www.slingacademy.com/article/python-sqlite3-define-a-table-with-auto-incrementing-primary-key/
def insertCategoryRecords(conn):
  try:
    c = conn.cursor()

   # Insert data
    categories = [
                  ('Accessories'), 
                  ('Bikes'), 
                  ('Clothing'), 
                  ('Components'), 
                  ('Car racks'),
                  ('Wheels')
                 ]
    # Insert each category record
    for category in categories:
        c.execute("INSERT INTO categories (CategoryId, CategoryDescription) VALUES (NULL, ?)", (category,))

    conn.commit()
    print(f"\nMultiple categories successfully inserted into the table.")

    # Fetch and display all records in the categories table
    categoriesQuery = "SELECT * FROM categories"
    c.execute(categoriesQuery)   
    print("\nThese are the categories in the categories table via fetchall:")
    print(c.fetchall())

    c.execute(categoriesQuery)
    print("\nThese are the categories in the categories table via for loop:")
    rows = c.fetchall()
    for row in rows:
        print(f"ID: {row[0]}\tDescription: {row[1]}")
  except sqlite3.IntegrityError as e:
    print(f"\nIntegrity Error: {e}")
    return None
  except sqlite3.DataError as e:
    print(f"\nData Error: {e}")
    return None
  except sqlite3.DatabaseError as e:
    print(f"\nDatabase Error: {e}")
    return None
  except sqlite3.OperationalError as e:
    print(f"\nOperational Error: {e}")
    return None
  except sqlite3.ProgrammingError as e:
    print(f"\nProgramming Error: {e}")
    return None
  except sqlite3.Error as e:
    print(f"\nGeneric Database Error: {e}")
    return None

