# classes/tables/category.py
import sqlite3

from classes.table import Table

class Category(Table):
    def __init__(self, db):
        super().__init__(db, "categories")

    def create(self, description):
        super().create(["CategoryDescription"], [description])
    
    def delete(self, recordID):
        super().delete({"CategoryID": recordID})
    
    def getRecordById(self, recordID):
        return super().getRecordById(recordID, "CategoryID")