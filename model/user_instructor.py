from model.user import User
import os
import json
import codecs
import pandas
import matplotlib.pyplot as plt

class Instructor(User):
    def __init__(self, uid=-1, username="", password="", register_time="yyyy-MM-dd_HH:mm:ss.SSS", role="instructor" , email="" , display_name = "" ,job_title = "" , course_id_list = [] ):
        self.uid = uid
        self.username = username
        self.password = password
        self.register_time = register_time
        self.role = role
        self.email = email
        self.display_name = display_name
        self.job_title = job_title
        self.course_id_list = course_id_list



    def __str__(self):
        return f"{self.uid};;;{self.username};;;{self.password};;;{self.register_time};;;{self.role};;;{self.email};;;{self.job_title};;;{self.course_id_list}"


    def get_instructors(self):
        id_seen = set()
        user_dict = {}
        user_data = []
        path = os.path.dirname(__file__).replace("\\model", "") + "\\data\\source_course_files"
        user_file_path = os.path.dirname(__file__).replace("\\model", "") + "\\data\\user.txt"
        user_file = codecs.open(user_file_path, encoding="utf-8", mode="r+")
        current_data=user_file.readlines()
        for user in current_data:
            user_id=user.split(";;;")[0]
            id_seen.add(user_id)
            user_data.append(user)
            user_dict[user_id]=user_data.index(user)

        for root, dirs, files in os.walk(path):
            for file in files:
                with open(os.path.join(root, file), "r") as coursedata:
                    all_data = json.load(coursedata)
                    for data in all_data["unitinfo"]["items"]:
                        course_id=data["id"]

                        for instructor in data["visible_instructors"]:
                            instructor_id = instructor["id"]

                            username=instructor["display_name"].lower().replace(" ", "_" )
                            password = instructor_id
                            email = username + "@gmail.com"
                            display_name = instructor["display_name"]
                            job_title = instructor["job_title"]
                            role="instructor"
                            if instructor_id not in id_seen:
                                one_instructor=f"{instructor_id};;;{username};;;{self.encrypt_password(str(password))};;;{self.register_time};;;{role};;;{email};;;{display_name};;;{job_title};;;{course_id}\n"
                                user_data.append(one_instructor)
                                id_seen.add(instructor_id)
                                user_dict[instructor_id] = user_data.index(one_instructor)
                            else:
                                duplicate_index = user_dict[instructor_id]
                                duplicate_instructor = user_data[duplicate_index]
                                user_data[duplicate_index] = duplicate_instructor.replace("\n","") + "--" + str(course_id)+"\n"
        user_file.seek(0)
        for user in user_data:
            user_file.write(user)
        user_file.truncate()
        user_file.close()


    def get_instructors_by_page(self,page):
        path=os.path.dirname(__file__).replace("\\model", "") + "\\data\\user.txt"
        with codecs.open(path,encoding="utf-8",mode="r") as user_data:
            users=user_data.readlines()
            instructor_list=[]
            pages_dic={}
            for user in users:
                one_user=user.split(";;;")
                if one_user[4]=="instructor":
                    insructor=Instructor(one_user[0],one_user[1],one_user[2],one_user[3],one_user[4],one_user[5],
                                         one_user[6],one_user[7],one_user[8])
                    instructor_list.append(insructor)
        if len(instructor_list)%20!=0:
            total_pages=(len(instructor_list)//20)+1
        else:
            total_pages=len(instructor_list)//20
        for i in range(total_pages):
            pages_dic[i]=instructor_list[i:i+20]

        return (pages_dic[page],total_pages,len(instructor_list))


    def generate_instructor_figure1(self):
        path = os.path.dirname(__file__).replace("\\model", "") + "\\data\\user.txt"
        with codecs.open(path,encoding="utf-8",mode="r") as user_data:
            users=user_data.readlines()
            instructor_list=[]
            for user in users:
                one_user=user.split(";;;")
                if one_user[4]=="instructor":
                    insructor=Instructor(one_user[0],one_user[1],one_user[2],one_user[3],one_user[4],one_user[5],
                                         one_user[6],one_user[7],one_user[8])
                    course_list=one_user[8].split("--")
                    instructor_list.append([insructor,len(course_list)])

        sort_instructor=sorted(instructor_list,key=lambda x:x[1],reverse=True)
        instructor_name=[]
        num_of_course=[]
        for item in range(10):
            instructor_name.append(sort_instructor[item][0].display_name.split(" ")[:3])
            num_of_course.append(sort_instructor[item][1])
        data={"instructor_name":instructor_name,"number_of_course":num_of_course}
        df=pandas.DataFrame(data,columns=["instructor_name","number_of_course"])
        df.plot(x='instructor_name', y='number_of_course', kind='bar')
        plt.show()

