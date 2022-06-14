from flask import render_template, Blueprint
from app.controllers.home import hello


bp = Blueprint("home", __name__, template_folder="templates", static_folder="static")

@bp.route("/")
def Index():
    return render_template('index.html')
