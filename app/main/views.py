from flask import render_template, request, redirect,url_for
from . import main
from ..request import get_sources, get_articles

# Views
@main.route('/',methods=[ 'POST','GET'])
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    raw_data = ""
    articles= get_articles('creative')
    if request.method == 'POST':
        query_str = request.form.get("query")
        articles = get_articles(query_str)
        
    # if not (raw_data):
    # articles = get_articles('') 

    data = {
        "title":"Breaking News",
        "heading": "News", 
    }
    sources = get_sources()
    
    
    return render_template('index.html', context=data,sources= sources, article=articles)
