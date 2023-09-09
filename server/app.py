from flask import Flask,render_template
from blog_api import blog

app = Flask(__name__)
app.register_blueprint(blog)

@app.route("/")
@app.route("/home")
def home():
    return render_template("main.html")

@app.route('/profile')
def profile():
    return render_template("copy.html")



if __name__ == "__main__":
    app.run(debug=True)