import requests
from typing import Optional, Any, Dict
from yass.types import HttpResult, Operation

def get_url_for_operation_id(operation: Operation, api_schema: Dict[str, Any], host: str = '') -> str:
    """
    """
    scheme = "https"    # schemes = api_schema['schemes']
    scheme += r"://"
    if not host:
        host = api_schema.get('host', '/')
    base_path = api_schema.get('basePath', '')
    return f"{scheme}{host}{base_path}{operation.path}"


# TODO: use contextlib instead and evaluat whether if 
#       it's possible to embed this context inside the
#       Operation object 
def operation_session(operation: Operation, api_schema: Dict[str, Any], host: str = ''):
    with requests.Session() as s:
        method_name = f"{operation.method}"
        url = get_url_for_operation_id(operation, api_schema, host=host)
        return s.request(method_name, url) # need to re-write payload sect.


def invoke_service_operation(operation_id: str, 
                             *, 
                             payload: Optional[Any] = None,
                             **kwargs) -> HttpResult:
    pass