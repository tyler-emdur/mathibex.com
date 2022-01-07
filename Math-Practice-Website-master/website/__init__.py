from flask import Flask 
 
def create_app(): 
    app = Flask(__name__) 
    app.config['SECRET_KEY'] = 'SSn7RftwbH6pCYZeJwDujcylPwtQBrsG4AN7V4IQ'

    from .views import views

    app.register_blueprint(views, url_prefix='/') 

    return app
    
    