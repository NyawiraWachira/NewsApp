from flask import Flask, render_template
import os 
from flask import send_from_directory  
from app import app

from newsapi import NewsApiClient


app = Flask(__name__)

   

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/favicon.icon')


@app.route('/')
def home():

    newsapi = NewsApiClient(api_key='d3afaf05f0a744be8752d41b2ad1d279')
    top_headlines = newsapi.get_top_headlines(sources = 'bbc-news, abc-news, al-jazeera-english, bbc-sport, the-verge')
    

    t_articles = top_headlines['articles']

     
    news = []
    desc = []
    img = []
    p_date = []
    url = []
    

    for i in range(len(t_articles)):
        main_article = t_articles[i]


        news.append (main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])
        

        contents = zip(news,desc,img,p_date,url)

    return render_template('home.html',contents=contents)

@app.route('/bbc')
def bbc():

    newsapi = NewsApiClient(api_key='d3afaf05f0a744be8752d41b2ad1d279')
    all_articles = newsapi.get_everything(sources = 'bbc-news')
    

    a_articles = all_articles['articles']

    news_all = []
    desc_all = []
    img_all = []
    p_date_all = []
    url_all = []

    for i in range(len(a_articles)):
        all_article = a_articles[i]

        news_all.append (all_article['title'])
        desc_all.append(all_article['description'])
        img_all.append(all_article['urlToImage'])
        p_date_all.append(all_article['publishedAt'])
        url_all.append(all_article['url'])

        contents = zip(news_all,desc_all,img_all,p_date_all,url_all)

    return render_template('bbc.html',contents=contents)


@app.route('/aljazeera')
def aljazeera():

    newsapi = NewsApiClient(api_key='d3afaf05f0a744be8752d41b2ad1d279')
    all_articles = newsapi.get_everything(sources = 'al-jazeera-english')

    a_articles = all_articles['articles']

    news_all = []
    desc_all = []
    img_all = []
    p_date_all = []
    url_all = []

    for i in range(len(a_articles)):
        all_article = a_articles[i]

        news_all.append (all_article['title'])
        desc_all.append(all_article['description'])
        img_all.append(all_article['urlToImage'])
        p_date_all.append(all_article['publishedAt'])
        url_all.append(all_article['url'])

        contents = zip(news_all,desc_all,img_all,p_date_all,url_all)


    return render_template('aljazeera.html',contents=contents)


@app.route('/cbs')
def cbs():

    newsapi = NewsApiClient(api_key='d3afaf05f0a744be8752d41b2ad1d279')
    all_articles = newsapi.get_everything(sources = 'cbs-news')

    a_articles = all_articles['articles']

    news_all = []
    desc_all = []
    img_all = []
    p_date_all = []
    url_all = []

    for i in range(len(a_articles)):
        all_article = a_articles[i]

        news_all.append (all_article['title'])
        desc_all.append(all_article['description'])
        img_all.append(all_article['urlToImage'])
        p_date_all.append(all_article['publishedAt'])
        url_all.append(all_article['url'])

        contents = zip(news_all,desc_all,img_all,p_date_all,url_all)


    return render_template('cbs.html',contents=contents)

@app.route('/insider')
def insider():

    newsapi = NewsApiClient(api_key='d3afaf05f0a744be8752d41b2ad1d279')
    all_articles = newsapi.get_everything(sources = 'business-insider')

    a_articles = all_articles['articles']

    news_all = []
    desc_all = []
    img_all = []
    p_date_all = []
    url_all = []

    for i in range(len(a_articles)):
        all_article = a_articles[i]

        news_all.append (all_article['title'])
        desc_all.append(all_article['description'])
        img_all.append(all_article['urlToImage'])
        p_date_all.append(all_article['publishedAt'])
        url_all.append(all_article['url'])

        contents = zip(news_all,desc_all,img_all,p_date_all,url_all)


    return render_template('insider.html',contents=contents)

@app.route('/verge')
def verge():

    newsapi = NewsApiClient(api_key='d3afaf05f0a744be8752d41b2ad1d279')
    all_articles = newsapi.get_everything(sources = 'the-verge')

    a_articles = all_articles['articles']

    news_all = []
    desc_all = []
    img_all = []
    p_date_all = []
    url_all = []

    for i in range(len(a_articles)):
        all_article = a_articles[i]

        news_all.append (all_article['title'])
        desc_all.append(all_article['description'])
        img_all.append(all_article['urlToImage'])
        p_date_all.append(all_article['publishedAt'])
        url_all.append(all_article['url'])

        contents = zip(news_all,desc_all,img_all,p_date_all,url_all)


    return render_template('verge.html',contents=contents)

