import datetime
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)

default_image = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    first_name = db.Column(db.String,
                       nullable=False)

    last_name = db.Column(db.String,
                      nullable=False)

    image_url = db.Column(db.String,
                      nullable=False,
                      default= default_image)
    
    posts = db.relationship('Post', backref='user')

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}"


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"




class Post (db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String,
                      nullable=False)
    content = db.Column(db.String,
                        nullable=False)
    created_at = db.Column(db.DateTime,
                           default=datetime.datetime.now)
    
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                        nullable=False)
    
    


    def __repr__(self):
        return f"<Post {self.title} {self.content} {self.created_at} "

    
    






    
