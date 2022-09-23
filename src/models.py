from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    favorites = db.relationship('Favorites', backref='user', lazy=True)

    def _repr_(self):
        return '<User %r>' % self.id

    def serialize(self): #MUCHO OJO LA FUNCIÓN serialize TRANSFORMÁS LA ETIQUETA ILEGIBLE CON QUE TE RESPONDE PYTHON EN UN OBJETO LEGIBLE
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }





#OJO: AQUÍ HACEMOS LA TABLA DE Favorites (IMPORTANTE: ESTE TIENE RELACIÓN 1 A MUCHOS -en favortiros pueden haber muchos usuarios, planetas y personajes)
class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))

    def _repr_(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "people_id": self.people_id,
            # do not serialize the password, its a security breach
        }





#OJO: AQUÍ HACEMOS LA TABLA DE DE Planets
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    favorites = db.relationship('Favorites', backref='planets', lazy=True)


    def _repr_(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }





#OJO: AQUÍ HACEMOS LA TABLA DE DE People
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)
    favorites = db.relationship('Favorites', backref='people', lazy=True)


    def _repr_(self):
        return '<People %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            # do not serialize the password, its a security breach
        }