'''
File: CS499NoSQLcrud.py
Author: Paul Stephan
Version: 1.0
Date: April 21, 2024

Description:
creation of CRUD class to use mongoDB
'''


from pymongo import MongoClient


# In[ ]:


class CRUD:
    def __init__(self, db_name, collection_name):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
    
    def create_document(self, document):
        """Inserts a new document into the collection."""
        result = self.collection.insert_one(document)
        return result.inserted_id
    
    def read_document(self, query):
        """Retrieves a document from the collection based on the query."""
        document = self.collection.find_one(query)
        return document
    
    def update_document(self, query, new_values):
        """Updates a document in the collection based on the query."""
        result = self.collection.update_one(query, {"$set": new_values})
        return result.modified_count
    
    def delete_document(self, query):
        """Deletes a document from the collection based on the query."""
        result = self.collection.delete_one(query)
        return result.deleted_count

