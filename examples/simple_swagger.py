from yass import read_swagger_file as rsf 
from yass import services 

BASE_URL = "https://raw.githubusercontent.com/swagger-api/swagger-samples/"
PATH_TO_FILE = "/master/java/inflector-dropwizard-guice/src/main/swagger/swagger.yaml"

url = f"{BASE_URL}{PATH_TO_FILE}"
path = "/pet"
method = "post"

api_schema = rsf.read_yaml(url)
operation = rsf.operation_from_path_info(api_schema, path, method)


res = services.operation_session(operation, api_schema, host="petstore.swagger.io")