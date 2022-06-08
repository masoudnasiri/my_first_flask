
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




# use @user_page.route("") for each page url

