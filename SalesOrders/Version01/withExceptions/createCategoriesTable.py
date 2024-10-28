import sqlite3

# Step 2.  Function createCategoriesTable()
#
# This function will attempt to create
# a database table.
def createCategoriesTable(conn):
  try:
    c = conn.cursor()
    createCategoriesTableQuery = """
        CREATE TABLE IF NOT EXISTS categories
        (
          CategoryID 					  INTEGER			PRIMARY KEY,
          CategoryDescription   TEXT			  NULL 
        )
    """

    c.execute(createCategoriesTableQuery)
    conn.commit()
    print(f"\nCategories table successfully created.")
  except sqlite3.DatabaseError as e:
    print(f"\nDatabase Error: {e}")
    return None
  except sqlite3.OperationalError as e:
    print(f"\nOperational Error: {e}")
    return None
  except sqlite3.ProgrammingError as e:
    print(f"\Programming Error: {e}")
    return None
  except sqlite3.Error as e:
    print(f"\nGeneric SQLite3 Error: {e}")
    return None