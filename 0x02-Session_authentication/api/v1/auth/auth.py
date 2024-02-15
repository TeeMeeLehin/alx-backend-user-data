#!/usr/bin/env python3
"""authentication module"""
from flask import request
from typing import List, TypeVar


class Auth():
    """Authentication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        func to determine if a route requires authentication
        """
        if not excluded_paths or excluded_paths == []:
            return True
        if path:
            if path[-1] != "/":
                path += "/"
            if path in excluded_paths:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """auth header func"""
        if request and request.headers.get('Authorization', None) is not None:
            return request.headers.get('Authorization')
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current user func"""
        return None
