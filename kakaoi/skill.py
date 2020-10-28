class SimpleText():
    def __init__(self, text : str):
        self.text = text
        
    def __repr__(self):
        return f"<SimpleText text={self.text}>"

    def __dict__(self):
        return {"version": "2.0","template": {"outputs": [{"simpleText": {"text": self.text}}]}}
