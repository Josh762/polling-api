from enum import Enum

class ResponsePolicy(str, Enum):
    ip = "IP"
    cookie = "COOKIE"
    none = "NONE"
