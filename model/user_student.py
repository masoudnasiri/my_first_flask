from model.user import User
import os,codecs
class Student(User):
    def __init__(self, uid=-1, username="", password="", register_time="yyyy-MM-dd_HH:mm:ss.SSS", role="student" , email = ""):
        self.uid = uid
        self.username = username
        self.password = password
        self.register_time = register_time
        self.role = role
        self.email = email



    def __str__(self):
        return f"{self.uid};;;{self.username};;;{self.password};;;{self.register_time};;;{self.role};;;{self.email}"



    def get_students_by_page(self,page):
        path = os.path.dirname(__file__).replace("\\model", "") + "\\data\\user.txt"
        with codecs.open(path, encoding="utf-8", mode="r") as user_data:
            users = user_data.readlines()
            student_list = []
            pages_dic={}
            for user in users:
                one_user = user.split(";;;")
                if one_user[4] == "student":
                    student = Student(one_user[0], one_user[1], one_user[2], one_user[3], one_user[4], one_user[5])
                    student_list.append(student)
        if len(student_list) % 20 != 0:
            total_pages = (len(student_list) // 20) + 1
        else:
            total_pages = len(student_list) // 20
        for i in range(total_pages):
            pages_dic[i]=student_list[i:i+20]
        return (pages_dic[page], total_pages, len(student_list))

    def get_student_by_id(self,id):
        id=str(id)

        path = os.path.dirname(__file__).replace("\\model", "") + "\\data\\user.txt"
        with codecs.open(path, encoding="utf-8", mode="r") as user_data:
            users = user_data.readlines()
            student_list = []
            for user in users:
                one_user = user.split(";;;")
                if (one_user[4] == "student") and (one_user[0]==id):
                    student = Student(one_user[0], one_user[1], one_user[2], one_user[3], one_user[4], one_user[5])
                    return student

    def delete_student_by_id(self,id):
        id=str(id)
        # list to store file lines
        lines = []
        # read file
        path = os.path.dirname(__file__).replace("\\model", "") + "\\data\\user.txt"
        with codecs.open(path,encoding="utf-8",mode="r") as fp:
            # read an store all lines into list
            lines = fp.readlines()

        # Write file
        with codecs.open(path,encoding="utf-8",mode="w") as fp:
            # iterate each line
            for item in lines:
                # delete line 5 and 8. or pass any Nth line you want to remove
                # note list index starts from 0
                if item.split(";;;")[0]!=id or item.split(";;;")[4]!="student":

                    fp.write(item)
