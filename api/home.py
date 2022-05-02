import json
import urllib.request

from flask import render_template, Blueprint
from config import API_KEY, NEWS_BASE_URL

home_blueprint = Blueprint("home", __name__)


@home_blueprint.route('/')
def index():
    # create the url endpoint
    url = NEWS_BASE_URL + "/top-headlines/sources?apiKey=" + API_KEY

    print(url)
    response = urllib.request.urlopen(url).read()

    data = json.loads(response)

    return render_template('index.html', data=data['sources'])


@home_blueprint.route('/source/<string:name>')
def news_source(name):
    url = NEWS_BASE_URL + "/top-headlines?sources="+name+"&apiKey=" + API_KEY
    print(url)
    return render_template('news.html', source=name)
