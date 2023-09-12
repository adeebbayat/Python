from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self,db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

        self.ninjas = []


    
    @classmethod
    def get_all_no_data(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        print(len(results))
        return range(1,len(results)+1)
    
    @classmethod
    def get_one(cls,data):
        query= "SELECT * FROM ninjas JOIN dojos WHERE dojos.id = ninjas.dojo_id AND dojo_id = %(id)s;"
        # query  = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(result)
        return (result[0])
    
    @classmethod
    def get_all(cls,data):
        query = "SELECT * FROM ninjas JOIN dojos WHERE dojos.id = ninjas.dojo_id AND dojo_id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        ninjas = []
        print(results)
        for u in range(len(results)):
            ninjas.append(results[u])
        print(ninjas)
        return ninjas
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        # comes back as the new row id
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return result