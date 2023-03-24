#!/usr/bin/python3
import os

from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
##postgress
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:12Ali..456@localhost:3306/hasnat"
app.config['SECRET_KEY'] = "random string"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)
class Room(db.Model):
    __tablename__ = "class"
    id = db.Column(db.Integer, primary_key=True)
    clss = db.Column(db.String(12), nullable=False)

class Teach(db.Model):
    __tablename__ = "teacher"
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(70), nullable=False)
    clss = db.Column(db.String(50), nullable=False)
    Qualification = db.Column(db.String(40))

class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(60), nullable=False)
    clss = db.Column(db.String(12), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(7))

@app.route("/", methods=['GET'])
def index():
    students = Student.query.all()
    return render_template("intro.html", students=students)

@app.route("/insert", methods=['GET', 'POST'])
def insert():
    if request.method == "POST":

        name = request.form.get("name")
        AGE = request.form.get("age")
        gend = request.form.get("gender")
        clss = request.form.get("Class")

        # Creat new record
        stud = Student(Name = name, age=AGE, gender=gend, clss=clss)
        db.session.add(stud)
        db.session.commit()

        students = Student.query.all()
        return render_template("intro.html", students=students)

    c = db.session.query(Room.clss).all()
    return render_template("insert_new_student.html", c=c)

@app.route("/class", methods=['GET', 'POST'])
def clss():
    if request.method == "POST":

        name = request.form.get("class")

        # Creat new record
        stud = Room(clss = name)
        db.session.add(stud)
        db.session.commit()

    cla = Room.query.all()
    return render_template("class.html", cla=cla)

@app.route("/teacher", methods=['GET', 'POST'])
def teach():
    if request.method == "POST":

        name = request.form.get("name")
        spe = request.form.get("spe")
        sub = request.form.get("sub")
        sls = request.form.get("Class")

        # Creat new record
        stud = Teach(Name = name, Qualification=spe, clss=sls)
        db.session.add(stud)
        db.session.commit()

    t = Teach.query.all()
    c = db.session.query(Room.clss).all()
    return render_template("teacher.html", t=t, c=c)

if __name__ == "__main__":
    app.run(debug=True)