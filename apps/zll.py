from flask import Blueprint,render_template

zll = Blueprint('zll',__name__)

@zll.route('/')
def index():
    return render_template('/zll/1.html')
