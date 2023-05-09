"""Convenience imports for views module"""
from .address import AddressViewSet
from .person import PersonViewSet
from .user import UserViewSet

__all__ = ["PersonViewSet", "UserViewSet", "AddressViewSet"]
