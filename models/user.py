from datetime import date

class User():
    def __init__(self, id, first_name, last_name, email, password):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.bio = "No bio yet"
        self.profile_image_url = ""
        self.created_on = date.today()
        self.active = 1
        self.is_staff = 1