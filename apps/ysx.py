from flask import Blueprint,render_template

ysx = Blueprint('ysx',__name__)

@ysx.route('/')
def index():
    return render_template('/ysx/ysx.html')