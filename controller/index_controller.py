from flask import render_template, Blueprint
from model.user import User
from model.user_admin import Admin
import time




index_page = Blueprint("index_page", __name__)

@index_page.route("/")
def index():
    context = {}
    admin = Admin()
    admin.register_admin("admin", "admin", time.time(), "admin")
    if User.current_login_user != None:
        context["current_user_role"]=User.current_login_user.role

        return render_template("01index.html",**context)
    else:
        return render_template("01index.html")

