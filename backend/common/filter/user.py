import contextvars
from typing import Optional

_current_user: contextvars.ContextVar[Optional[dict]] = contextvars.ContextVar("_current_user", default=None)

def get_current_user():
    return _current_user.get()

def set_current_user(user: dict):
    _current_user.set(user)

def clear_current_user():
    _current_user.set(None)
