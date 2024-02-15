#!/usr/bin/env python3
"""basic authentication module"""
from api.v1.auth.auth import Auth
import base64
from typing import Union


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
                    email, pwd = decoded_base64_authorization_header.split(':')
                    return (email, pwd)
        return (None, None)
