#!/usr/bin/env python3
"""session authentication module"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """Session AUthentication Class"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """func to create new session"""
        if user_id and isinstance(user_id, str):
            sess_id = str(uuid.uuid4())
            self.user_id_by_session_id[sess_id] = user_id
            return sess_id
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """func to retrieve user id"""
        if session_id and isinstance(session_id, str):
            return self.user_id_by_session_id.get(session_id)
        return None

    def current_user(self, request=None):
        """returns current user"""
        cookee = self.session_cookie(request)
        uid = self.user_id_for_session_id(cookee)
        return User.get(uid)
