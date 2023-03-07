from ..config.api import api

from ..controllers.hello_world import HelloWorld

api.add_resource(HelloWorld, '/')