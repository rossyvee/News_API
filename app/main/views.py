import json
import urllib.request

from flask import render_template
from config import API_KEY, NEWS_BASE_URL

from . import main


@main.route('/')
def index():
    # create the url endpoint        
    # url = NEWS_BASE_URL + "/top-headlines/sources?apiKey=" + API_KEY
    print("NEWS_BASE_URL",NEWS_BASE_URL)
    print("API_KEY",API_KEY)
    url = NEWS_BASE_URL + "/top-headlines/sources?apiKey=" + API_KEY
    data = make_external_api_call(url)
    return render_template('index.html', data=data['sources'])


@main.route('/source/<string:name>')
def news_source(name):
    # url = NEWS_BASE_URL + "/top-headlines?sources=" + name + "&apiKey=" + API_KEY
    url = NEWS_BASE_URL + "/top-headlines?sources=" + name + "&apiKey=" + API_KEY

    print(url)
    data = make_external_api_call(url)
    return render_template('news.html', data=data['articles'])


def make_external_api_call(url):
    response = urllib.request.urlopen(url).read()
    return json.loads(response)