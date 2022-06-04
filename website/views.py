from flask import Blueprint, render_template
from flask import request
import json
import os

def open_file(name, mode="r", data=None):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, name)

    if mode == "r":
        with open(file_path, mode, encoding='utf-8') as f:
            data = json.load(f)
            return data

    elif mode == "w":
        with open(file_path, mode, encoding='utf-8') as f:
            json.dump(data, f)

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html") 
#Tyler and Ian were here

@views.route('/coming_soon')
def comingSoon():
    return render_template("coming_soon.html")  
 
@views.route('/addition')
def addition():
    return render_template("addition.html")

@views.route('/subtraction')
def subtraction():
    return render_template("subtraction.html") 

@views.route('/multiplication')
def multiplication():
    return render_template("multiplication.html") 
     
@views.route('/division')
def division():
    return render_template("division.html")  
     
@views.route('/mental_math')
def mental_math():
    return render_template("mental_math.html")
    
     
@views.route('/two_step_equations')
def two_step_equations():
    return render_template("two_step_equations.html")  
 
@views.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html")  

@views.route('/login')
def login():
    return render_template("coming_soon.html")

#these are all of the chideren