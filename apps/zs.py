from flask import Blueprint,render_template

zs = Blueprint('zs', __name__)

@zs.route('/')
def index():
    return render_template('/zs/index.html')
