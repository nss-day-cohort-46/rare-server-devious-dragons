from datetime import date

class User():
    def __init__(self,
                 id,
                 first_name,
                 last_name,
                 username,
                 email,
                 password,
                 created_on,
                 bio = "No bio yet",
                 profile_image_url = "",
                 ):
        self.id = id
        self.firstName = first_name
        self.lastName = last_name
        self.userName = username
        self.email = email
        self.password = password
        self.bio = bio
        self.profileImageUrl = profile_image_url
        self.createdOn = created_on
        self.active = 1
        self.isStaff = 1


@property
def __password(self, password):
    self.__password = password


@__password.setter
def password(self, pswd):
    pass