from flask import Flask 
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy 
from config import Config 


# flask app instance
app         = Flask(__name__)
# loading configuration
app.config.from_object(Config)
#db ORM instance
db          = SQLAlchemy(app)
migrate     = Migrate(app, db)


from app import views 
