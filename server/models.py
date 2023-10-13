from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates, relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)

#/////////////////////////////////////////////////////////////
class Movie(db.Model, SerializerMixin):
    __tablename__='movie_table'

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String)
    title = db.Column(db.String)
    genre = db.Column(db.String)
    rating = db.Column(db.Integer)
    description = db.Column(db.String)

    credits = db.relationship("Credit", backref="movie")

    @validates('rating')
    def validate_age(self, key, rating):
        if rating < 1 or rating >10:
            return ValueError("Rating must be between 1 and 10")
        return rating
    
    @validates('genre')
    def validate_genre(self,key,genre):
        Genre = [ "Action", "Comedy", "Drama", "Horror", "Romance", "Thriller", "Science Fiction", "Fantasy", "Mystery", "Adventure", "Crime", "Family", "Animation", "Documentary", "War" ]
        if genre not in Genre:
            return ValueError(f"Genre most be one of the following: {Genre}")
        return genre
        
#/////////////////////////////////////////////////////////////

class Actor(db.Model, SerializerMixin):
    __tablename__='actor_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)

    credits = db.relationship("Credit", backref="actor")

    @validates('age')
    def validate_age(self, key, age):
        if age > 10:
            return age
        
#/////////////////////////////////////////////////////////////

class Credit(db.Model, SerializerMixin):
    __tablename__='credit_table'

    id = db.Column(db.Integer, primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey("actor_table.id"),nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie_table.id"),nullable=False)
    role = db.Column(db.String, nullable=False)

    serialize_rules=('-movie','-actor')

    @validates('role')
    def validate_role(self,key,role):
        Roles = ["Performer", "Director", "Producor", "Playwright", "Lighting Design", "Sound Design", "Set Design"]
        if role not in Roles:
            return ValueError(f"Role most be one of the following: {Roles}")
        return role

