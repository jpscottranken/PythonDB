# classes/tables/order.py
import sqlite3

from classes.table import Table

class Order(Table):
    def __init__(self, db):
        super().__init__(db, "Orders")

    def create(self, orderDate, orderShipDate, 
               customerID, employeeID):
        fields = ["OrderDate", "OrderShipDate",
                  "CustomerID", "EmployeeID"]
        values = [orderDate, orderShipDate, 
                  customerID, employeeID]
        super().create(fields, values)

    def delete(self, recordID):
        super().delete({"OrderID": recordID})
    
    def getRecordById(self, recordID):
        return super().getRecordById(recordID, "OrderID")

