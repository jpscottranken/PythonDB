# classes/Table.py
class Table:
    def __init__(self, db, tableName):
        self.db = db
        self.tableName = tableName

    def create(self, fields, values):
        placeholders = ", ".join("?" * len(values))
        query = f"INSERT INTO {self.tableName} ({', '.join(fields)}) VALUES ({placeholders})"
        self.db.cursor.execute(query, values)
        self.db.commit()

    def read(self):
        query = f"SELECT * FROM {self.tableName}"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()

    def update(self, primaryKeys, updateData):
        setClause = ", ".join([f"{k} = ?" for k in updateData.keys()])
        whereClause = " AND ".join([f"{pk} = ?" for pk in primaryKeys.keys()])
        query = f"UPDATE {self.tableName} SET {setClause} WHERE {whereClause}"
        self.db.cursor.execute(query, list(updateData.values()) + list(primaryKeys.values()))
        self.db.commit()

    def delete(self, primaryKeys):
        whereClause = " AND ".join([f"{pk} = ?" for pk in primaryKeys.keys()])
        query = f"DELETE FROM {self.tableName} WHERE {whereClause}"
        self.db.cursor.execute(query, list(primaryKeys.values()))
        self.db.commit()

    def getRecordById(self, recordID, id_column="id"):
        query = f"SELECT * FROM {self.tableName} WHERE {id_column} = ?"
        
        self.db.cursor.execute(query, (recordID,))

        record = self.db.cursor.fetchone()
        if record:
            # Map column names to values
            columns = [col[0] for col in self.db.cursor.description]
            return dict(zip(columns, record))
        
        return None