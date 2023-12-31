from flask_app.config.mysqlconnection import connectToMySQL
class Ninja:
    def __init__(self,db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = """INSERT INTO ninjas (first_name,last_name,age,dojo_id)
        VALUES (%(first_name)s, %(last_name)s, %(age)s,%(dojo_id)s)"""
        print(query)
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return result
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = []
        for u in results:
            ninjas.append( cls(u) )
        return ninjas