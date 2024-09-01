import os
from flask import Flask
from .models import db
from flask_login import LoginManager

def create_app():
    
    app=Flask(__name__)
    app.config['DEBUG']= True
    app.config['SECRET_KEY'] ='secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    print(os.path.abspath('db.sqlite'))

    db.init_app(app)
    
    with app.app_context():
       db.create_all()
        
    login_manager= LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)
    
    from .models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    #accessing the main file to run the home page of application
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    #accessing the auth file to run the authentication of the users in the application
    from.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    return app