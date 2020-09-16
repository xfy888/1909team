from flask import Blueprint,render_template

wangyi = Blueprint('wangyi',__name__)

@wangyi.route('/')
def index():
    return render_template('/wangyi/index.html/')