from flaskApp.config.dbmongo import db

class User:
    def __init__(self, data):
        self.id = data['_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']

    def __repr__(self) -> str:
        print(f"""
ID: {self.id}
First Name: {self.first_name}
Last Name: {self.last_name}

""")
    
    @classmethod
    def findUserByID(cls, data):
        result = db.users.find_one(data)
        print(result)
        if result:
            return cls(result)
        return None