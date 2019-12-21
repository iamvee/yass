import requests
from typing import Optional, Any
from yass.types import HttpResult, Operation

def get_url_for_operation_id(operation: Operation, api_schcema: Dict[str, Any]) -> str:
    """
    """
    scheme = "https"    # schemes = api_schcema['schemes']
    return f"{scheme}://{api_schcema['host']}{api_schcema['basePath']}{operation.path}"


# TODO: use contextlib instead and evaluat whether if 
#       it's possible to embed this context inside the
#       Operation object 
def operation_session(operation: Operation, api_schcema: Dict[str, Any]):
    with requests.Session() as s:
        method_name = f"{operation.method}"
        url = get_url_for_operation_id(operation, api_schcema)
        s.request(method_name, url) # need to re-write payload sect.


def invoke_service_operation(operation_id: str, 
                             *, 
                             payload: Optional[Any] = None,
                             **kwargs) -> HttpResult
    pass