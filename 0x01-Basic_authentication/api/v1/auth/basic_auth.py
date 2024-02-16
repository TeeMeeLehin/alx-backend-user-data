#!/usr/bin/env python3
"""basic authentication module"""
from api.v1.auth.auth import Auth
import base64
from typing import Union
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """Basic Authentication Class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extracting base64 H func"""
        if authorization_header:
            if isinstance(authorization_header, str):
                if authorization_header[:6] == "Basic ":
                    return authorization_header.split(' ')[1]
        return None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """decoding basic auth header func"""
        if base64_authorization_header:
            if isinstance(base64_authorization_header, str):
                try:
                    sub = base64.b64decode(base64_authorization_header)
                    return sub.decode('utf-8')
                except ValueError:
                    return None
        return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> Union[str, str]:
        """func to extract user deets"""
        if decoded_base64_authorization_header:
            if isinstance(decoded_base64_authorization_header, str):
                if ":" in decoded_base64_authorization_header:
                    email, pwd = decoded_base64_authorization_header.split(':', 1)
                    return (email, pwd)
        return (None, None)

    def user_object_from_credentials(self,
                                     user_email: str, user_pwd: str
                                     ) -> TypeVar('User'):
        """func to return user instance"""
        if user_email and isinstance(user_email, str):
            if user_pwd and isinstance(user_pwd, str):
                try:
                    users = User.search({"email": user_email})
                except Exception:
                    return None
                if len(users) > 0:
                    for user in users:
                        if user.is_valid_password(user_pwd):
                            return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """func to return current user"""
        auth_header = self.authorization_header(request)
        b64_auth_h = self.extract_base64_authorization_header(auth_header)
        decoded_auth = self.decode_base64_authorization_header(b64_auth_h)
        email, pwd = self.extract_user_credentials(decoded_auth)
        user = self.user_object_from_credentials(email, pwd)
        return user
