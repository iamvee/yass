# yass

yet another swagger stuff

## Structure of swagger file

```yml
swagger: "2.0"
info:
  description: 
  title: 
  termsOfService: 
  contact:
    email: 
  license:
    name:
    url:
host:
basePath:
tags:
  - name: "tag1"
  - name: "tag2"
schemes:
  - "https"
  - "http"
paths:  
  # gonna discuss this one a bit later 
  # multiple
  /some/api/path:
securityDefinitions:
  petstore_auth:
  api_key:
definitions:
  # multiple 
  SomeDefenition:
    type: "object"
    properties:
      id:
      name:
    xml:
externalDocs:
  description: "Find out more about Swagger"
  url: "http://swagger.io"
```

### `path` structure


a sample path look like this:

```yaml
 /pet:
    post:   # method
      tags:
      - "pet"
      summary: 
      description: 
      operationId: "addPet"    # we're gonna use this part of file in function
      consumes:
      produces:
      parameters:
      - in: 
        name: 
        description: 
        required:
        schema:
          $ref: "#/definitions/Pet"
      responses:
        405:
          description:
      security:
      - petstore_auth:
```


```python
from read_swagger_file import *
url = "https://raw.githubusercontent.com/swagger-api/swagger-samples/master/java/inflector-dropwizard-guice/src/main/swagger/swagger.yaml"
path = "/pet"
method = "post"
api_schema = read_yaml(url)
operation = operation_from_path_info(api_schema, path, method)
```