
class Student:
    def __init__(self, uid=-1, username="", password="", register_time="yyyy-MM-dd_HH:mm:ss.SSS", role="student" , email = ""):
        self.uid = uid
        self.username = username
        self.password = password
        self.register_time = register_time
        self.role = role
        self.email = email



    def __str__(self):
        return f"{self.uid};;;{self.username};;;{self.password};;;{self.rigester_time};;;{self.role};;;{self.email}"



    def get_students_by_page(self):
        pass

    def get_student_by_id(self):
        pass

    def delete_student_by_id(self):
        pass
