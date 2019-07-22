import os

from flask import send_from_directory

from application.api.login import (Login, LogOut, AddUser)
from application.model.models import db
from index import (app, api, static_folder)

db


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(
            static_folder + path):  # for UI path ex: /login, /register
        return send_from_directory(static_folder, path)
    elif not (os.path.exists(static_folder + path) or (
            str(path).startswith(
                "api/"))):  # for Backend Path ex: /api/register
        return send_from_directory(static_folder, 'index.html')
    elif path == "":
        return send_from_directory(static_folder, 'index.html')


api.add_resource(Login, '/api/login')
api.add_resource(LogOut, '/api/loginout')
api.add_resource(AddUser, '/api/adduser/<string:email>')