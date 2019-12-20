#!/usr/bin/env python3.7
import yaml
import urllib.request
from typing import Dict, Any
from types_local import Operation, RestMethod


def read_yaml(url: str) -> Dict[str, Operation]:
    """
    >>> url = "https://raw.githubusercontent.com/swagger-api/swagger-samples/master/java/inflector-dropwizard-guice/src/main/swagger/swagger.yaml"
    >>> api_schema = read_yaml(url)
    >>> type(api_schema)
    <class 'dict'>
    >>> len(api_schema['paths'])
    14
    >>> api_schema['paths']['/pet'].keys()
    dict_keys(['post', 'put'])
    >>> api_schema['paths']['/pet']['post']['operationId']
    'addPet'
    """
    request = urllib.request.urlopen(url)
    text = request.read()
    return yaml.load(text)

def operation_from_path_info(api_schema: Dict[str, Any], path: str, method_name: str) -> Operation:
    """
    >>> from read_swagger_file import *
    >>> url = "https://raw.githubusercontent.com/swagger-api/swagger-samples/master/java/inflector-dropwizard-guice/src/main/swagger/swagger.yaml"
    >>> path = "/pet"
    >>> method = "post"
    >>> api_schema = read_yaml(url)
    >>> operation = operation_from_path_info(api_schema, path, method)
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

if __name__ == "__main__":
    import doctest
    doctest.testmod()
