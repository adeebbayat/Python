from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self,db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.location = db_data['location']
        self.language = db_data['language']
        self.comment = db_data['comment']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

        self.dojos = []


    @staticmethod
    def validate_dojo(dojo):
        print(dojo)
        is_valid = True # we assume this is true
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(dojo['location']) < 3:
            flash("Location must be at least 3 characters.")
            is_valid = False
        if len(dojo['language']) < 3:
            flash("Language must be at least 3 characters.")
            is_valid = False
        if len(dojo['comment']) < 3:
            flash("Comment must be at least 3 characters.")
            is_valid = False
        return is_valid
