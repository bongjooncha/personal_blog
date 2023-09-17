from flask import Blueprint,render_template

blog = Blueprint("blog",__name__)

@blog.route('/blog')
def blog_main(): 
    return render_template("study.html")