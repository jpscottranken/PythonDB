import sqlite3

def vowelBadWay2(conn):
  # Write a query to select all customers whose last name
  # ends with a vowel (a, e, i, o, u).
  #
  # Sort the rsults by last name ASC, then by first name ASC
  try:
    c = conn.cursor()

    vowelLast1 = """
                    SELECT *
                    FROM customers
                    WHERE (CustomerLastName  LIKE '%a'
                      OR    CustomerLastName LIKE '%A'
                      OR    CustomerLastName LIKE '%e'
                      OR    CustomerLastName LIKE '%E'
                      OR    CustomerLastName LIKE '%i'
                      OR    CustomerLastName LIKE '%I'
                      OR    CustomerLastName LIKE '%o'
                      OR    CustomerLastName LIKE '%O'
                      OR    CustomerLastName LIKE '%u'
                      OR    CustomerLastName LIKE '%U')
                    ORDER BY CustomerLastName,
                              CustomerFirstName
                  """
    c.execute(vowelLast1)   
    print("\nQ11. Those employees whose last name ends with a vowel (unformatted):")
    print(c.fetchall())

    c.execute(vowelLast1)
    print("\nQ11. Those employees whose last name ends with a vowel (formatted):")
    rows = c.fetchall()
    for row in rows:
        print(f"ID: {row[0]} Name: {row[1]} {row[2]}  Address: {row[3]}  CSZ: {row[4]} {row[5]} {row[6]}  Phone: {row[7]} {row[8]}")
  except sqlite3.Error as e:
    print(f"\nQ11. Problem trying to display database records: {e}")
    return None