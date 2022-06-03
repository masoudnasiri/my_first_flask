from model.user import User
import os

class Admin(User):
    def __init__(self , uid=-1, username="", password="", register_time="yyyy-MM-dd_HH:mm:ss.SSS", role="admin"):
        self.uid = uid
        self.username = username
        self.password = password
        self.register_time = register_time
        self.role = role


    def register_admin(self, username, password, email, register_time, role):
        if (self.check_username_exist(username)):
            return False
        user_id = self.generate_unique_user_id()
        register_time = self.date_conversion(register_time)
        if (self.validate_username(username) and self.validate_password(password) and self.validate_email(email)):

            path = os.path.dirname(__file__)
            path = path.replace("model", "")
            user_data = open(path + "\\data\\user.txt", 'a')

            user_data.write( f"\n{user_id};;;{username};;;{self.encrypt_password(password)};;;{register_time};;;{role};;;{email}")
            user_data.close()

    def __str__(self):
        return f"{self.uid};;;{self.username};;;{self.password};;;{self.rigester_time};;;{self.role}"




