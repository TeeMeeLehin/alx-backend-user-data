#!/usr/bin/env python3
"""basic authentication module"""
from api.v1.auth.auth import Auth


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
