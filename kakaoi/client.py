from flask import Flask, request
from .payload import *

class Client:
    def __init__(self):
        self.server = Flask(__name__)

    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<Client {resolved}>"

    def run(self, func, *, host, port = None, debug = None):
        @self.server.route("/", methods=["POST"])
        def message():
            response = func(SkillPayload(request.get_json()))
            return response.__dict__()
        
        self.server.run(host=host, port=port, debug=debug)
