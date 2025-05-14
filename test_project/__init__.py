from flask import Flask 
from flask_bootstrap import Bootstrap4
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 

db = SQLAlchemy()


def create_app():
    app = Flask(__name__,template_folder="templates-test")

    app.config['SECRET_KEY'] = 'Thisisasecretkey '
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    
    db.init_app(app)

    bootstrap = Bootstrap4(app)

    login_manager = LoginManager(app)
    login_manager.login_view = 'auth.login'
    @login_manager.user_loader
    def load_user(user_id):
        from test_project.models import User
        return User.query.get(int(user_id))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    
    return app


    

