from bs4 import BeautifulSoup
import requests
import json
import re
from scraper_api import ScraperAPIClient
from flask import Flask, request
import webScraper
import nltk
nltk.download('punkt') #NEED TO RUN THIS THE FIRST TIME YOU USE IT

app = Flask(__name__)

client = ScraperAPIClient('8a40568ad90a53e817126fb569a0cb5a')

from dbhelper import DBHelper
import vocabquery

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                   level=logging.INFO)

logger = logging.getLogger(__name__)


@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond(word):
    url = 'https://finance.yahoo.com/quote/{}/sustainability/'.format(word)
    response = requests.get(url, timeout=5)
    #response = client.get(url, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")
    print (content)

@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"
        
@app.route('/lol', methos=['GET'])
def respond_this():
    answer = respond(word)

@app.route('/')
def index():
    return '.'


if __name__ == '__main__':
    app.run(threaded=True)
