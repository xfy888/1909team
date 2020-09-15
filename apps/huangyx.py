from flask import Blueprint,render_template

huangyx = Blueprint('huangyx',__name__)

@huangyx.route('/')
def index():
    return render_template('/hyx/index.html')
