from model.user import User
from model.user_admin import Admin
from model.user_instructor import Instructor
import  time
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
    new_user =Instructor()
    new_user.generate_instructor_figure1()


     #app.run(debug=True)



