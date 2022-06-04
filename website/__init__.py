from flask import Flask 
 
def create_app(): 
    app = Flask(__name__) 
    app.config['SECRET_KEY'] = 'YOU_DO_NOT_KNIW'

    from .views import views

    app.register_blueprint(views, url_prefix='/') 

    return app
    
