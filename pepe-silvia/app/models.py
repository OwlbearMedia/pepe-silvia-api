class UserModel():
    is_authenticated = True
    is_active = True
    is_anonymous = False
    password = ''

    def __init__(self, dbUser):
        self.name = dbUser['name']
        self.email = dbUser['email']
        self.password = dbUser['password']

    def get_id(self):
        return self.email

    def authenticate(self):
        self.is_authenticated = True
        self.is_active = True
        self.is_anonymous = False
