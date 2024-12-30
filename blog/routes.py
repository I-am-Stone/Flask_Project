from flask import render_template
from blog import blog_bp


@blog_bp.route('/')
def home():
    return render_template('all_section.html', title='Home')
