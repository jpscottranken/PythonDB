# classes/tables/employee.py
import sqlite3

from classes.table  import Table

class Employee(Table):
    def __init__(self, db):
        super().__init__(db, "Employees")

    def create(self, firstName, lastName, street, 
               city, state, zipCode, areaCode, phone):
        fields = ["EmployeeFirstName", "EmployeeLastName",
                  "EmployeeStreetAddress",
                  "EmployeeCity", "EmployeeState", "EmployeeZipCode",
                  "EmployeeAreaCode", "EmployeePhoneNumber"]
        values = [firstName, lastName, street, 
                  city, state, zipCode, areaCode, phone]
        super().create(fields, values)
    
    def delete(self, recordID):
        super().delete({"EmployeeID": recordID})
    
    def getRecordById(self, recordID):
        return super().getRecordById(recordID, "EmployeeID")
