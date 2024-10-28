# classes/tables/customer.py
import sqlite3

from classes.table import Table

class Customer(Table):
    def __init__(self, db):
        super().__init__(db, "Customers")

    def create(self, firstName, lastName, street, 
               city, state, zipCode, areaCode, phone):
        fields = ["CustomerFirstName", "CustomerLastName",
                  "CustomerStreetAddress",
                  "CustomerCity", "CustomerState", "CustomerZipCode",
                  "CustomerAreaCode", "CustomerPhoneNumber"]
        values = [firstName, lastName, street, 
                  city, state, zipCode, areaCode, phone]
        super().create(fields, values)
    
    def delete(self, recordID):
        super().delete({"CustomerID": recordID})
    
    def getRecordById(self, recordID):
        return super().getRecordById(recordID, "CustomerID")
