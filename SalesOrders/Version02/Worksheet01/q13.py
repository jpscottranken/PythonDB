import sqlite3

def vowelAND(conn):
  # Write a query to select all customers whose first name
  # begins with an uppercase or lowercase vowel (a, e, i, o, u)
  # OR ends with an uppercase or lowercase vowel (a, e, i, o, u).
  #
  # Sort the rsults by last name ASC, then by first name ASC
  try:
    c = conn.cursor()

    vowelANDquery = """
                  SELECT *
                  FROM customers
                  WHERE ((upper(CustomerFirstName)  LIKE 'A%'
                  OR     upper(CustomerFirstName)   LIKE 'E%'
                  OR     upper(CustomerFirstName)   LIKE 'I%'
                  OR     upper(CustomerFirstName)   LIKE 'O%'
                  OR     upper(CustomerFirstName)   LIKE 'U%')
                  AND   (lower(CustomerLastName)    LIKE '%a'
                  OR     lower(CustomerLastName)    LIKE '%e'
                  OR     lower(CustomerLastName)    LIKE '%i'
                  OR     lower(CustomerLastName)    LIKE '%o'
                  OR     lower(CustomerLastName)    LIKE '%u'))
                  ORDER BY CustomerLastName ASC,
                           CustomerFirstName                  
                    """
    c.execute(vowelANDquery)   
    print("\nQ13. Those employees whose first name starts with a vowel AND whose last name ends with a vowel  (unformatted):")
    print(c.fetchall())

    c.execute(vowelANDquery)
    print("\nQ13. Those employees whose first name starts with a vowel AND whose last name ends with a vowel (formatted):")
    rows = c.fetchall()
    for row in rows:
        print(f"ID: {row[0]} Name: {row[1]} {row[2]}  Address: {row[3]}  CSZ: {row[4]} {row[5]} {row[6]}  Phone: {row[7]} {row[8]}")
  except sqlite3.Error as e:
    print(f"\nQ13. Problem trying to display database records: {e}")
    return None