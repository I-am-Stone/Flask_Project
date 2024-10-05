from flask import Flask
from blog import blog_bp  # Importing blueprint from the blog module

app = Flask(__name__)

# Register the blog blueprint
app.register_blueprint(blog_bp)

if __name__ == '__main__':
    app.run(debug=True)
