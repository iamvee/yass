from typing import NamedTuple, Any, Dict

class HttpResult(NamedTuple):
    Status: int
    Body: Any
    Headers: Dict[str, str]
    