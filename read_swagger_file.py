#!/usr/bin/env python3.7
import yaml
import urllib.request

def read_yaml(url: str) -> dict:
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
