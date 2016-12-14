import logging

from flask import Flask, request, session, redirect, render_template, url_for, flash
from flask_cors import CORS
from flask_restful import Api

from guppylist.config import settings
from guppylist.routes.main import routes
from guppylist.data.lists import lists

# Load Flask and Flask-RESTful.
app = Flask(__name__)
api = Api(app)
CORS(app)

# Load routes/endpoints.
# for route in routes:
#     # if route.get('arguments'):
#     #     for argument in route['arguments']:
#     #         print(argument)
#
#     api.add_resource(route['controller'], route['path'])

@app.route('/lists/gl/<slug>', methods=['GET'])
def list_details(slug):
    list = lists[slug]

    return render_template('list/details.html', list=list)

if __name__ == "__main__":
    app.logger.setLevel(logging.DEBUG)
    app.run(host=settings.HOST, port=settings.PORT, debug=settings.DEBUG)