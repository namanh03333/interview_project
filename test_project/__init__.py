from flask import Flask 
from flask_bootstrap import Bootstrap4
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()


def create_app():
    app = Flask(__name__,template_folder="templates-test")

    app.config['SECRET_KEY'] = 'Thisisasecretkey '
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    
    db.init_app(app)

    bootstrap = Bootstrap4(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    
    return app


    

