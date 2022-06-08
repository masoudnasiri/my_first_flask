from flask import render_template, Blueprint
from model.user import User
from model.user_admin import Admin
import time




index_page = Blueprint("index_page", __name__)

@index_page.route("/",methods=["GET"])
def index():
    admin = Admin()
    admin.register_admin("admin", "admin", time.time(), "admin")
    if User.current_login_user != None:
        return  render_template("01index.html",current_user_role=User.current_login_user.role )
    else:
        return render_template("01index.html")

