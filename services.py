from typing import Optional, Any
from .types import HttpResult

def invoke_service_operation(operation_id: str, 
                             *, 
                             payload: Optional[Any] = None,
                             **kwargs) -> HttpResult
    pass