#!/usr/bin/env python3
"""session authentication module"""
from api.v1.auth.auth import Auth
import uuid


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
