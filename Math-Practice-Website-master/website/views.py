from flask import Blueprint, render_template

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
     
@views.route('/simple_algebra')
def simple_algebra():
    return render_template("simple_algebra.html")  
 
@views.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html") 
#these are all of the chideren