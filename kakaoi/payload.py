import json

class SkillPayload:
    def __init__(self, data : dict):
        self.request = UserRequest(data["userRequest"])
        self.bot = Bot(data["bot"])
        self.action = Action(data["action"])

    def __str__(self):
        return self.request.utterance

    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<SkillPayload {resolved}>"

class UserRequest:
    def __init__(self, data : dict):
        self.timezone = data["timezone"]
        self.block = Block(data["block"])
        self.utterance = data["utterance"]
        self.lang = data["lang"]
        self.user = User(data["user"])

    def __str__(self):
        return self.utterance

    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<UserRequest {resolved}>"

class User:
    def __init__(self, data : dict):
        self.id = data["id"]
        self.type = data["type"]
        self.channel_id = data["properties"].get("plusfriendUserKey")
        self.app_id = data["properties"].get("appUserId")
        self.is_friend = data["properties"].get("isFriend")

    def __str__(self):
        return self.id

    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<User {resolved}>"

class Bot:
    def __init__(self, data : dict):
        self.id = data["id"]
        self.name = data["name"]

    def __str__(self):
        return self.name

    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<Bot {resolved}>"

class Block:
    def __init__(self, data : dict):
        self.id = data["id"]
        self.name = data["name"]

    def __str__(self):
        return self.name

    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<Block {resolved}>"

class Action:
    def __init__(self, data : dict):
        self.name = data["name"]
        self.client_extra = data.get("clientExtra")
        self.id = data["id"]
        self.parameter = [Parameter(param[0], param[1]) for param in data["detailParams"].items()]

    def __str__(self):
        return self.name

    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<Action {resolved}>"

class Parameter:
    def __init__(self, _type: str, data : dict):
        self.type = _type
        self.origin = data["origin"]
        try:
            self.value = json.loads(data["value"])
        except:
            self.value = data["value"]
        self.group_name = data["groupName"]

    def __str__(self):
        return self.value

    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<Parameter {resolved}>"
