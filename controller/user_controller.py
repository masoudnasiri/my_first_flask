
from flask import Blueprint, render_template, request, redirect, url_for
from lib.helper import render_result, render_err_result, course_data_path, user_data_path
from model.course import Course
from model.user import User
from model.user_admin import Admin
from model.user_instructor import Instructor
from model.user_student import Student

login_aut_obj=User()

user_page = Blueprint("user_page", __name__)

model_user = User()
model_course = Course()
model_student = Student()
def generate_user(user_data):
    if user_data[4]=="admin":
        logined_user = Admin(int(user_data[0]), user_data[1],user_data[2], user_data[3],user_data[4].strip('\n'))
    elif user_data[4]=="instructor":
        logined_user=Instructor(int(user_data[0]),user_data[1],user_data[2],user_data[3],user_data[4].strip('\n'))
    else:
        logined_user=Student(int(user_data[0]),user_data[1],user_data[2],user_data[3],user_data[4].strip('\n'))
    return logined_user


@user_page.route("/login",methods=["GET"])
def login():
    return render_template("00login.html")


    return login_user
@user_page.route("/login",methods=["Post"])
def login_post():
    login_data=request.values
    username=login_data["username"]
    password=login_data["password"]
    if username!="" and password!="" and login_aut_obj.check_username_exist(username):
        login_result=login_aut_obj.authenticate_user(username,password)
    elif username=="" or password=="":
        return render_result(msg="Please input valid username or password!")
    else:
        return render_result(msg="login failed")

    if login_result[0]:
        user_data = login_result[1].split(";;;")
        User.current_login_user=generate_user(user_data)
        return render_result(msg="successfully login")
@user_page.route("/logout",methods=["GET"])
def logout():
    User.current_login_user = None
    return render_template("01index.html")



@user_page.route("/register",methods=["GET"])
def register():
    return render_template("00register.html")

@user_page.route("/register",methods=["POST"])
def register_post():
    all_data=request.values
    username=all_data["username"]
    password=all_data["password"]
    email=all_data["email"]
    role=all_data["role"]
    register_time=all_data["register_time"]
    validation=False
    if username and password and email:
        if login_aut_obj.validate_username(username) and login_aut_obj.validate_password(password) and login_aut_obj.validate_email(email):
            validation=True
    if validation and login_aut_obj.check_username_exist(username)==False:
        login_aut_obj.register_user(username,password,email,register_time,role)
        return render_result(msg="User Register Successfully")

    else:
        return render_err_result(msg="You Enter improper username,password or email address! ")
@user_page.route("/student-list",methods=["GET"])
def student_list():
    pass

