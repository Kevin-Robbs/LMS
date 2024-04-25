from flaskApp.config.dbmongo import db

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.year = data['year']
        self.phone_number = data['phone_number']
        self.gender = data['gender']
        self.dob = data['dob']
        self.address = data['address']
        self.city = data['city']
        self.state = data['state']
        self.role_id = data['role_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        if 'student_id' in data:
            self.student_id = data['student_id']
    
    @classmethod
    def findUserByID(cls, data):
        result = db.users.find_one(data)
        print(result)
        if result:
            return cls(result)
        return None
    
    @classmethod
    def findUserByEmail(cls, email):
        result = db.users.find_one({'email': email})
        print(result)
        if result:
            return cls(result)
        return None
