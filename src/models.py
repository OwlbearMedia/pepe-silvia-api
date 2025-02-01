# models.py


from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, dbUser):
        self.name = dbUser['name']
        self.email = dbUser['email']
        self.password = dbUser['password']

    def get_id(self):
        return self.email
