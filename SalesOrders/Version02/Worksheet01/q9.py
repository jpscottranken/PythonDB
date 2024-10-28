import sqlite3

def vowelBadWay1(conn):
  # Write a query to select all customers whose first name
  # begins with an uppercase or lowercase vowel (a, e, i, o, u)
  #
  # Sort the rsults by last name ASC, then by first name ASC
  try:
    c = conn.cursor()

    vowelFirst1 = """
                          SELECT *
                          FROM customers
                          WHERE ((CustomerFirstName LIKE 'a%'
                          OR    CustomerFirstName LIKE 'A%'
                          OR    CustomerFirstName LIKE 'e%'
                          OR    CustomerFirstName LIKE 'E%'
                          OR    CustomerFirstName LIKE 'i%'
                          OR    CustomerFirstName LIKE 'I%'
                          OR    CustomerFirstName LIKE 'o%'
                          OR    CustomerFirstName LIKE 'O%'
                          OR    CustomerFirstName LIKE 'u%'
                          OR    CustomerFirstName LIKE 'U%'))
                          ORDER BY CustomerLastName,
                                   CustomerFirstName
                        """

    c.execute(vowelFirst1)   
    print("\nQ9. Those employees whose first name starts with a vowel (unformatted):")
    print(c.fetchall())

    c.execute(vowelFirst1)
    print("\nQ9. Those employees whose first name starts with a vowel (formatted):")
    rows = c.fetchall()
    for row in rows:
        print(f"ID: {row[0]} Name: {row[1]} {row[2]}  Address: {row[3]}  CSZ: {row[4]} {row[5]} {row[6]}  Phone: {row[7]} {row[8]}")
  except sqlite3.Error as e:
    print(f"\nProblem trying to display database records: {e}")
    return None