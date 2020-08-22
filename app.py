import requests
from flask import Flask
from flask import request
from flask import Response

from utils import fetch_reply
from get_MeetLink import Link

file = open('text.txt', 'r')
bot = file.readline()
file.close()

token = bot
app = Flask(__name__)

def parse_message(message):
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    
    return(chat_id, txt)

def send_message(chat_id, text='hello_world'):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=payload)
    return r

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        chat_id, txt = parse_message(msg)        
        
        if txt == '/start':
            first_chat_name = msg['message']['from']['first_name']
            send_message(chat_id, 'Welcome '+ first_chat_name)
        else:
            msg = fetch_reply(txt, chat_id)
            msg = Link(msg)               
            send_message(chat_id, msg)
        return Response('ok', status=200)    
    else:
        return 'Hurray!!!'

if __name__ == "__main__":
    app.run(debug=True)