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
        return False

    def authorization_header(self, request=None) -> str:
        """auth header func"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current user func"""
        return None
