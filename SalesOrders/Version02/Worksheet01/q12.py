import sqlite3

def vowelGoodWay2(conn):
 # Write a query to select all customers whose last name
  # ends with a vowel (a, e, i, o, u).
  #
  # Sort the results by last name ASC, then by first name ASC
  try:
    c = conn.cursor()

    vowelGoodWay2Query = """
                  SELECT *
                    FROM customers
                    WHERE (Lower(CustomerLastName)  LIKE '%a'
                      OR    Lower(CustomerLastName) LIKE '%e'
                      OR    Lower(CustomerLastName) LIKE '%i'
                      OR    Lower(CustomerLastName) LIKE '%o'
                      OR    Lower(CustomerLastName) LIKE '%u')
                    ORDER BY CustomerLastName,
                              CustomerFirstName                  
                    """
    c.execute(vowelGoodWay2Query)   
    print("\nQ12. Those employees whose first OR last name start/end with a vowel (unformatted):")
    print(c.fetchall())

    c.execute(vowelGoodWay2Query)
    print("\nQ12. Those employees whose first OR last name start/end with a vowel (formatted):")
    rows = c.fetchall()
    for row in rows:
        print(f"ID: {row[0]} Name: {row[1]} {row[2]}  Address: {row[3]}  CSZ: {row[4]} {row[5]} {row[6]}  Phone: {row[7]} {row[8]}")
  except sqlite3.Error as e:
    print(f"\nQ12. Problem trying to display database records: {e}")
    return None