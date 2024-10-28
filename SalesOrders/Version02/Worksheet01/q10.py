import sqlite3

def vowelGoodWay1(conn):
  # Write a query to select all customers whose first name
  # begins with an uppercase or lowercase vowel (a, e, i, o, u)
  #
  # Sort the rsults by last name ASC, then by first name ASC
  try:
    c = conn.cursor()

    vowelFirst2 = """
                  SELECT *
                  FROM Customers
                  WHERE (Upper(CustomerFirstName) LIKE 'A%'
                  OR    Upper(CustomerFirstName) LIKE 'E%'
                  OR    Upper(CustomerFirstName) LIKE 'I%'
                  OR    Upper(CustomerFirstName) LIKE 'O%'
                  OR    Upper(CustomerFirstName) LIKE 'U%')
                  ORDER BY CustomerLastName  ASC,
                            CustomerFirstName ASC
                  """

    c.execute(vowelFirst2)   
    print("\nQ10. Those employees whose first name starts with a vowel (unformatted):")
    print(c.fetchall())

    c.execute(vowelFirst2)
    print("\nQ10. Those employees whose first name starts with a vowel (formatted):")
    rows = c.fetchall()
    for row in rows:
        print(f"ID: {row[0]} Name: {row[1]} {row[2]}  Address: {row[3]}  CSZ: {row[4]} {row[5]} {row[6]}  Phone: {row[7]} {row[8]}")
  except sqlite3.Error as e:
    print(f"\nProblem trying to display database records: {e}")
    return None