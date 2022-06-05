from model.user import User
from model.user_admin import Admin
from model.user_instructor import Instructor
from model.user_student import Student
import  time
from model.course import Course

"""from flask import Flask
from controller.index_controller import index_page
from controller.course_controller import course_page
from controller.instructor_controller import instructor_page
from controller.user_controller import user_page


app = Flask(__name__)

app.register_blueprint(index_page, url_prefix="/")
app.register_blueprint(course_page, url_prefix="/course")
app.register_blueprint(instructor_page, url_prefix="/instructor")
app.register_blueprint(user_page, url_prefix="/user")"""

if __name__ == "__main__":
    new_user =Course()
    #new_user.get_courses()
    #new_user.delete_course_by_id(5350676)
    #new_user.get_course_by_course_id(156173119)
    #for item in new_user.get_course_by_instructor_id(257585701)[0]:
    #   print(item.course_title)
    new_user.generate_course_figure4()



     #app.run(debug=True)



