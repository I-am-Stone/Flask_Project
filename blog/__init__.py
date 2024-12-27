from flask import Blueprint

# Initialize blueprint for the blog
blog_bp = Blueprint('blog', __name__, template_folder='templates')

# Import routes from routes.py to connect to this blueprint
from blog import routes
