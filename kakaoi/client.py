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
            if type(response) == tuple:
                return {"version": "2.0","template": {"outputs":[res.to_dict() for res in response[0]] if type(response[0]) == list else [response[0].to_dict()],"quickReplies":[res.to_dict() for res in response[1]] if type(response[1]) == list else [response[1].to_dict()]}}
            else:
                return {"version": "2.0","template": {"outputs":[res.to_dict() for res in response] if type(response) == list else [response.to_dict()]}}
        
        self.server.run(host=host, port=port, debug=debug)
