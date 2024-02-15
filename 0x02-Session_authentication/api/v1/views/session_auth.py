#!/usr/bin/env python3
""" Module of Users views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login() -> str:
    """func for session login"""
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or email == "":
        return jsonify({"error": "email missing"}), 400
    if not password or password == "":
        return jsonify({"error": "password missing"}), 400
    users = User.search({"email": email})
    if len(users) <= 0:
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    sess_id = auth.create_session(user.id)
    output = jsonify(user.to_json())
    cookee_name = getenv('SESSION_NAME', '_my_session_id')
    output.set_cookie(cookee_name, sess_id)
    return output
