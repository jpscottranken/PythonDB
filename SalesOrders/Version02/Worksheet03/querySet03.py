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

def main():
  # Attempt to connect to database
  conn = dbc.createConnection()

  # Show a query that shows how many order 
  # dates from the 	orders 	table are incorrect (i.e. 
  # they are 0000-00-0000 00:00:00).
  # 
  # Please be aware: The answer to the query may be 0 (empty)
  q1.runQ1(conn)
  
  # Show a query that shows how many orderShipDates 
  # dates from the 	orders 	table are incorrect (i.e. 
  # they are 0000-00-0000 00:00:00).
  # 
  # Please be aware: The answer to the query may be 0 (empty)
  q2.runQ2(conn)
  
  # Show a query that shows the total number of customers per state.
  # Include both the state name and the count in your answer.
  # 
  # Order the result by the count in descending order.
  q3.runQ3(conn)
  
  # Show a query to show the total number of employees per state.
  # Include both the state name and the count in your answer.
  # 
  # Order the result by the count in descending 	order.
  q4.runQ4(conn)
  
  # Show a query that shows each category description, 
  # along with a count of the number of products in that 
  # category description.
  # 
  # Sort by the count of 	the number of products 
  # descending and then category description ascending. 
  q5.runQ5(conn)
  
  # Select one field from each of the tables as follows: 
  # order date, ship date, quantity ordered, wholesale 
  # price, retail price, quoted price, category description,
  # and vendor name where the vendor name begins with an 'A' 
  # and the quoted price > 150.00.
  # 
  # Order the results by category description
	# ascending, then quoted price descending.
  q6.runQ6(conn)
  
  # Show a query where you select one field from each 
  # of the tables as follows: customerid, employeeid, 
  # shipdate (cast as date), wholesaleprice, retailprice, 
  # quotedprice, category description, and vendorid where 
  # the quotedprice  is not equal to the retailprice and 
  # the wholesaleprice is between 125.00 and 130.00 and 
  # the employeeid is equal to 705.
  # 
  # Order the results by categorydescription, then 
  # customerid, both in ascending order. 
  q7.runQ7(conn)
  
if (__name__ == "__main__"):
  main()