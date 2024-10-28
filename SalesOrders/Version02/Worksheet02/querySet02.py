# https://www.sqliz.com/sqlite-ref/
#
# https://www.sqlitetutorial.net/
#

import sqlite3
import createConnection           as dbc
import q1
import q2
import q3
import q4
import q5
import q6
import q7
import q8

def main():
  # Attempt to connect to database
  conn = dbc.createConnection()

  # Show show a query that will tell whether or not 
  # any employee has a telephone number.  Include the
  # employee first name and last name in the query results.
  q1.runQ1(conn)

  # Show a query that shows the total quantity 
  # on hand for each category.
  q2.runQ2(conn)

  # Show a query that shows each separate product name 
  # (no repeats), along with the associated category 
  # description.
  # 
  # Sort by category description and then by product 
  # name, both in ascending order.
  q3.runQ3(conn)

  # Show a query that shows customer first name, 
  # customer last name, order number, quantity 
  # ordered, product name, and category description.
  q4.runQ4(conn)

  # Show a query to show the vendor name, product name, 
  # quantity ordered, and quantity on hand, where the 
  # quantity ordered is greater than the quantity on hand. 
  q5.runQ5(conn)

  # Show a query to show the vendor name, product name, 
  # quantity ordered, and quantity on hand, where the 
  # quantity ordered is greater than the quantity on hand. 
  # No repeats for vendor name allowed.
  q6.runQ6(conn)

  # Show a query that gives the customer first name, 
  # customer last name, order date, ship date, product 
  # price, and quoted price for those records where the 
  # quoted price is not equal to the product price.
  # 
  # Sort by order number in ascending order.
  q7.runQ7(conn)

  # Show a query that shows only the vendor name and 
  # product wholesale price, but only for those vendor 
  # names that either start with an 's' or end with an
  # 's', and have a wholesale price between 10 and 20.
  #  # Show a query that shows the customer first name, 
  # customer last name, order number, ship date (cast),
  # order date (cast), product name, and 	retail price, 
  # but only for those orders that shipped exactly one 
  # day after they were ordered.  Use the date_add()
  # function in your answer.
  #
  # Sort the results based on wholesale price descending 
  # then by vendor name ascending. 
  q8.runQ8(conn)

if (__name__ == "__main__"):
  main()