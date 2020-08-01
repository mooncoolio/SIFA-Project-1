from application import db
from application.models import Songs, SetList

db.drop_all()
db.create_all()
