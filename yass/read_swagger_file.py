#!/usr/bin/env python3.7
import yaml
import urllib.request
from typing import Dict, Any
from yass.types import Operation, RestMethod


def read_yaml(url: str) -> Dict[str, Operation]:
    """
    docs
    """
    request = urllib.request.urlopen(url)
    text = request.read()
    return yaml.load(text)

def operation_from_path_info(api_schema: Dict[str, Any], path: str, method_name: str) -> Operation:
    """
    docs
    """
    p = api_schema['paths'][path][method_name]

    method = RestMethod.from_value(method_name)
    out = Operation(
        operations_id = p['operationId'], 
        path = path,
        method = method, 
        consumes = p['consumes'],
        produces = p["produces"],
        parameters = p["parameters"],   # it's a bit nested gonna use better type hints and so on 
        responses = p["responses"],
        security = p["security"]
    )
    return out


