from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from flask import Flask, render_template

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable = False)
    age = db.Column(db.Integer, nullable = False)

    def __init__(self,name,age):
        self.name = name
        self.age = age

        import pymysql

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:devpass@127.0.0.1:3306/elice_flask_board"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db.init_app(app)


@app.route("/")
def home():
    # Elice, Dodo, Cheshire, Queen 데이터를 추가하세요.
    member = Member("Elice",15)
    db.session.add(member)
    member1 = Member("Dodo",16)
    db.session.add(member1)
    member2 = Member("Cheshire",17)
    db.session.add(member2)
    member3 = Member("Queen",18)
    db.session.add(member3)  
    # 추가한 데이터를 DB에 저장하세요.
    db.session.commit()

    return "good"


@app.route("/check")
def check():
    data = db.session.query(Member).all()
        
    return render_template('member_list.html',member_list=data)

if __name__ == '__main__':
    app.run(debug=True)