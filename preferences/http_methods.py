from enum import Enum


class HttpMethods(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    methods = [GET, POST, PUT, DELETE, PATCH]