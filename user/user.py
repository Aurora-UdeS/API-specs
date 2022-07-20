from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
app.config['SWAGGER'] = {
    'openapi': '3.0.0',
}
swagger = Swagger(app, template_file="user.yaml")

if __name__ == '__main__':
    app.run()
