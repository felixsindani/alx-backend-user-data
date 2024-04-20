#!/usr/bin/env python3
"""
Auth class
"""

from typing import TypeVar, List
from tabnanny import check
from flask import request
User = TypeVar('User')


class Auth:
    """
    class managing API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Define which routes don't need authentication
        """
        check = path
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            check += "/"
        if check in excluded_paths or path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        validate all requests to secure the API
        """
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> User:
        """
        returns None - request
        """
        return None
    
    def session_cookie(self, request=None):
        """
        returns a cookie value from a request
        """
        if request:
            session_name = getenv("SESSION_NAME")
            return request.cookie.get(session_name, None)
