"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)





#OJO: AQUÍ HACEMOS EL endpoint/ruta DE User
@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200




#OJO: AQUÍ HACEMOS EL endpoint/ruta DE TODOS LOS Planets
@app.route('/planets', methods=['GET'])
def get_planets():
    planets= Planets.query.all()
    
    results = list(map(lambda item: item.serialize(),planets))

    response_body = {
        "msg":"Todo creado con exito",
        "results": results
    }

    return jsonify(results), 200




#OJO: AQUÍ HACEMOS EL endpoint/ruta ESPECÍFICO DE CADA Planeta
@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_one_planet(planet_id):
    planet = Planets.query.filter_by(id=planet_id).first()
    print(planet.serialize()) #<Planet 1>
    # results = list(map(lambda item: item.serialize(),planets))

    response_body = {
        "msg":"Todo creado con exito",
        "planet": planet.serialize()
    }

    return jsonify(response_body), 200




#OJO: AQUÍ HACEMOS EL endpoint/ruta DE TODOS LOS People
@app.route('/people', methods=['GET'])
def get_people():
    people= People.query.all()

    results = list(map(lambda item: item.serialize(),people))

    response_body = {
        "msg":"Todo creado con exito",
        "results": results
    }

    return jsonify(results), 200



#OJO: AQUÍ HACEMOS EL endpoint/ruta ESPECÍFICO DE CADA People
@app.route('/people/<int:people>', methods=['GET'])
def get_one_people(people_id):
    people = People.query.filter_by(id=people_id).first()
    # print(people.serialize()) #<Planet 1>
    # results = list(map(lambda item: item.serialize(),planets))

    response_body = {
        "msg":"Todo creado con exito",
        "people": people.serialize()
    }

    return jsonify(response_body), 200


    #//////////////// AHORA VAMOS CON LOS POST ////////////////////////

#OJO: AQUÍ HACEMOS EL endpoint/ruta PARA POSTEAR UN People EN Favorites
@app.route('/favorites/people/<int:people_idd>/<int:user_idd>', methods=['POST'])
def post_one_people_fav(people_idd, user_idd):
    id_people = int(people_idd)
    id_user = int(user_idd)
    new_fav_people = Favorites(user_id=id_user, people_id= id_people, planet_id=None)
    db.session.add(new_fav_people) #AQUÍ GREGAMOS A LA db RESULTADO DE LA VARIABLE post_new_fav_people
    db.session.commit() #AQUÍ COMMITEAMOS/GUARDAMOS TODOS LOS CAMBIOS EN EL db

    response_body = {
        "msg":"Se ha agregado el personaje ",
        "query_people": new_fav_people.serialize()
    }

    return jsonify(response_body), 200















# #OJO: AQUÍ HACEMOS EL endpoint/ruta PARA POSTEAR UN People EN Favorites
# @app.route('/favorite/people/<int:people_id>/<int:user_id>', methods=['POST'])
# # def post_one_people_fav(people_id):
# #     query_people_fav = Favorites(people_id=body["people_id"], user_id=body["user_id"])
#     db.session.add(post_one_people_fav) #AQUÍ GREGAMOS A LA db RESULTADO DE LA VARIABLE post_new_fav_people
#     db.session.commit() #AQUÍ COMMITEAMOS/GUARDAMOS TODOS LOS CAMBIOS EN EL db

#     response_body = {
#         "msg":"Se ha agregado el personaje ",
#         "query_people": query_people_fav.serialize()
#     }

#     return jsonify(response_body), 200



# OPCIÓN CHILENA 

# #OJO: AQUÍ HACEMOS EL endpoint/ruta PARA POSTEAR UN People EN Favorites
# @app.route('/favorite/people/<int:people_id>', methods=['POST'])
# def post_one_people(people_id):
#     query_people = People.query.get(people_id) #AQUÍ CONSULTO EL PERSONAJE POR SU people_id
#     user = User.query.get(1)#AQUÍ CONSULTO EL USUARIO QUE ESTÁ GUARDANDO SUS FAVORITOS
#     if(query_people): #AQUÍ USO UNA CONDICIONAL PARA CONFIRMAR QUE DICHO PERSONAJE EXISTA Y ESTÉ REGISTRADO... SI ES ASÍ PASO A LAS SIGUIENTES LÍNEAS
#         post_new_fav_people = Fav_people() #AQUÍ CREO UNA NUEVA VARIABLE/ NUEVO REGISTRO PARA LA TABLA Fav_people()
#         post_new_fav_people.user.id = user.id #AQUÍ NOS BASAMOS EN LOS CAMPOS DE LA TABLA FAVORITOS Y LE INDICAMOS QUE EN LA PARTE DEL ID DEL USUARIO VA EL user.id
#         post_new_fav_people.people_id = people_id #AQUÍ NOS BASAMOS EN LOS CAMPOS DE LA TABLA FAVORITOS Y LE INDICAMOS QUE EN LA PARTE DEL ID DEL PERSONAJE VA EL people_id
#         db.session.add(post_new_fav_people) #AQUÍ GREGAMOS A LA db RESULTADO DE LA VARIABLE post_new_fav_people
#         db.session.commit() #AQUÍ COMMITEAMOS/GUARDAMOS TODOS LOS CAMBIOS EN EL db
#     return "Listo! se agregó el personaje"

#     response_body = {
#         "msg":"Se ha agregado el personaje ",
#         "query_people": query_people.serialize()
#     }

#     return jsonify(response_body), 200
