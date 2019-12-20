from enum import Enum, auto
from typing import NamedTuple, Any, Dict
import enum


class StrOptions(str, Enum):
    def __str__(self):
        return self.value.lower()
    
    def _generate_next_value_(name, *_):
        return name

    @classmethod
    def from_value(cls, value):
        return cls._value2member_map_[value]

class RestMethod(StrOptions):
    GET = auto()
    POST = auto()
    PUT = auto()
    DELETE = auto()
    CONNECT = auto()
    OPTIONS = auto()
    TRACE = auto()
    PATCH = auto()
    

class HttpResult(NamedTuple):
    Status: int
    Body: Any
    Headers: Dict[str, str]


class Operation(NamedTuple):
    operations_id: str
    path: str
    method: RestMethod
    consumes: Any
    produces: Any
    parameters: Any  # it's a bit nested gonna use better type hints and so on 
    responses: Any
    security: Any

