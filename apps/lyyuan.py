from flask import Blueprint,render_template

lyyuan = Blueprint('lyyuan',__name__)

@lyyuan.route('/')
def index():
    return render_template('/lyyuan/index.html')
