import kakaoi

client = kakaoi.Client()

def main(message):
    if message.request.utterance == "ping":
        return kakaoi.SimpleText("Pong!")
    elif message.request.utterance == "pong":
        return kakaoi.SimpleText("Ping!")

client.run(main, host='0.0.0.0')
