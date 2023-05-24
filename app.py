from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
import pymongo
from bson.objectid import ObjectId
from datetime import datetime
from bson import ObjectId

app = Flask(__name__)
CORS(app)

# Conexión a la base de datos MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['TicketMaster']
collection = db['users']
collection1 = db['usuario']
collection2 = db['events']
collection3 = db['tickets']


# Ruta para obtener un usuario por email y password
@app.route('/users', methods=['GET'])
def get_user():
    email = request.args.get('email')
    password = request.args.get('password')
    user = collection.find_one({'email': email, 'password': password})
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user)
    else:
        return jsonify({"error": "User not found."})

# Ruta para obtener un usuario por email 
@app.route('/user-by-email', methods=['GET'])
def get_user_by_email():
    email = request.args.get('email')
    user = collection.find_one({'email': email})
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user)
    else:
        return jsonify({"error": "User not found."})

# Ruta para obtener un usuario por email 
@app.route('/user-by-username', methods=['GET'])
def get_user_by_user():
    user = request.args.get('user')
    username = collection.find_one({'nombre_u': user})
    if username:
        username['_id'] = str(username['_id'])
        return jsonify(username)
    else:
        return jsonify({"error": "User not found."})

# Ruta para crear un nuevo usuario
@app.route('/create', methods=['POST'])
def create_user():
    email = request.json['email']
    password = request.json['password']
    role = request.json['role']
    last_user = collection.find_one(sort=[('_id', pymongo.DESCENDING)])
    new_id = last_user['id'] + 1
    new_user = {
        "email": email,
        "password": password,
        "id": new_id,
        "role": role
    }
    collection.insert_one(new_user)
    return jsonify({'message': 'User created successfully'})

# Ruta para crear datos usuario
@app.route('/createUs', methods=['POST'])
def create_usu():
    userID = request.json['userID']
    nombre_u = request.json['nombre_u']
    nombre_com = request.json['nombre_com']
    Fecha_N = request.json['Fecha_N']
    ci = request.json['ci']
    profilePic = request.json['profilePic']
    last_event = collection2.find_one(sort=[('_id', pymongo.DESCENDING)])
    if last_event:
        new_id = last_event['_id'] + 1
    else:
        new_id = 1
    new_user = {
        "_id":new_id,
        "userID":userID,
        "profilePic":profilePic,
        "nombre_u": nombre_u,
        "nombre_com": nombre_com,
        "Fecha_N": datetime.strptime(Fecha_N, '%Y-%m-%d').date(),
        "ci":ci
    }
    collection.insert_one(new_user)
    return jsonify({'message': 'User created successfully'})

# Ruta para crear un nuevo evento
@app.route('/create_event', methods=['POST'])
def create_event():
    nombre = request.json['nombre']
    fechaHora = request.json['fechaHora']
    pais = request.json['pais']
    ciudad = request.json['ciudad']
    categoria = request.json['categoria']
    lugar = request.json['lugar']
    last_event = collection2.find_one(sort=[('_id', pymongo.DESCENDING)])
    if last_event:
        new_id = last_event['cod_E'] + 1
    else:
        new_id = 1

    if categoria == 'Musica':
        artista = request.json['artista']
        new_event = {
            "cod_E": new_id,
            "nombre": nombre,
            "fechaHora": datetime.strptime(fechaHora, '%Y-%m-%dT%H:%M').isoformat(),
            "pais": pais,
            "ciudad": ciudad,
            "artista": artista,
            "categoria": categoria,
            "lugar":lugar
        }
    elif categoria == 'Deportes':
        equipo1 = request.json['equipo1']
        equipo2 = request.json['equipo2']
        new_event = {
            "cod_E": new_id,
            "nombre": nombre,
            "fechaHora":datetime.strptime(fechaHora, '%Y-%m-%dT%H:%M').isoformat(),
            "pais": pais,
            "ciudad": ciudad,
            "equipo1": equipo1,
            "equipo2": equipo2,
            "categoria": categoria,
            "lugar":lugar
        }
    elif categoria == 'Convencion':
        new_event = {
            "cod_E": new_id,
            "nombre": nombre,
            "fechaHora": datetime.strptime(fechaHora, '%Y-%m-%dT%H:%M').isoformat(),
            "pais": pais,
            "ciudad": ciudad,
            "categoria": categoria,
            "lugar":lugar
        }
    else:
        return jsonify({'error': 'Categoría inválida'}), 400

    collection2.insert_one(new_event)
    return jsonify({'message': 'Event created successfully'})


# Ruta para verificar si un email ya está registrado
@app.route('/users/exists', methods=['GET'])
def check_user():
    email = request.args.get('email')
    user = collection.find_one({'email': email})
    if user:
        return jsonify({"exists": True})
    else:
        return jsonify({"exists": False})

# Ruta para actualizar un usuario existente
@app.route('/usersUpdate', methods=['PUT'])
def update_user():
    id = int(request.args.get('id'))  # Convertir el id a entero
    email = request.json['email']
    password = request.json['password']
    role = request.json['role']
    if collection.find_one({"id": id}):
        collection.update_one({"id": id}, {"$set": {"email": email, "password": password, "role": role}})
        return jsonify({'message': 'Usuario actualizado correctamente'})
    else:
        return jsonify({'message': 'El usuario no existe'})

# Ruta para obtener un usuario por id 
@app.route('/usersget', methods=['GET'])
def get_userid():
    idu = request.args.get('idu')
    user = collection1.find_one({'userID': idu})
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user)
    else:
        return jsonify({"error": "User not found."})

# Ruta para eliminar un usuario existente
@app.route('/usersd', methods=['DELETE'])
def delete_user():
    id = int(request.args.get('id'))
    user_exists = False
    if collection1.find_one({"id": id}):
        collection1.delete_one({"id": id})
        user_exists = True
    # Verifica si el usuario existe en la colección collection
    if collection.find_one({"id": id}):
        collection.delete_one({"id": id})
        user_exists = True
    if user_exists:
        # Retorna la respuesta JSON indicando que el usuario ha sido eliminado correctamente
        return jsonify({'message': 'Usuario eliminado correctamente'})
    else:
        # El usuario no existe en ninguna de las colecciones, no se realiza ninguna acción
        return jsonify({'message': 'El usuario no tiene datos registrados'})


# Ruta para obtener usuarios por rol
@app.route('/usersr', methods=['GET'])
def get_users_by_role():
    role = request.args.get('role')  # Obtener el rol desde los parámetros de la solicitud
    users = collection.find({'role': role})  # Buscar usuarios con el rol especificado
    user_list = []
    for user in users:
        user['_id'] = str(user['_id'])
        user_list.append(user)
    if user_list:
        return jsonify(user_list)
    else:
        return jsonify({"error": "No users found for the specified role."})

# Ruta para obtener eventos
@app.route('/Events', methods=['GET'])
def get_events():
    events = list(collection2.find())
    # Excluir el campo _id de cada evento
    serialized_events = []
    for event in events:
        serialized_event = {k: v for k, v in event.items() if k != '_id'}
        serialized_events.append(serialized_event)
    return jsonify(serialized_events)


# Ruta para obtener tickets por disponibilidad
@app.route('/Tickets_Avalibity', methods=['GET'])
def get_tickets_by_availability():
    disponible = request.args.get('disponible')
    disponible = disponible.lower() == 'true'
    available_tickets = list(collection3.find({"disponible": disponible}))
    return jsonify(available_tickets)

# Ruta para crear tickets
@app.route('/Tickets_Create', methods=['POST'])
def create_ticket():
    id_event = request.json['id_event']
    precio = request.json['precio']
    tipo = request.json['tipo']
    disponible = request.json['disponible']

    # Verificar si el id_event existe en la colección collection2
    if collection2.find_one({"cod_E": id_event}):
        last_ticket = collection3.find_one(sort=[('_id', pymongo.DESCENDING)])
        if last_ticket:
            new_id = last_ticket['_id'] + 1
        else:
            new_id = 1
        new_ticket = {
            "_id": new_id,
            "id_event": id_event,
            "precio": precio,
            "tipo": tipo,
            "disponible": disponible
        }
        collection3.insert_one(new_ticket)
        return jsonify({'message': 'Ticket created successfully'})
    else:
        return jsonify({'message': 'Event does not exist'})

# Ruta para modificar tickets
@app.route('/Tickets_Ava', methods=['PUT'])
def update_ticket_availability():
    id_ticket = int(request.json['_id'])
    disponible = request.json['disponible']
    collection3.update_one({"_id": id_ticket}, {"$set": {"disponible": disponible}})
    return jsonify({'message': 'Ticket availability updated'})


if __name__ == '__main__':
    app.run(debug=True)