from datetime import date

class User():
    def __init__(self, id, first_name, last_name, email, password):
        self.id = id
        self.firstName = first_name
        self.lastName = last_name
        self.email = email
        self.password = password
        self.bio = "No bio yet"
        self.profileImageUrl = ""
        self.createdOn = date.today()
        self.active = 1
        self.isStaff = 1


@property
def __password(self, password):
    self.__password = password


@__password.setter
def password(self, pswd):
    pass