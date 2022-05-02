# api_key = 'd3afaf05f0a744be8752d41b2ad1d279'
# d3afaf05f0a744be8752d41b2ad1d279
# https://newsapi.org/v2/everything?q=Apple&from=2022-05-02&sortBy=popularity&apiKey=API_KEY
#url = ('https://newsapi.org/v2/everything?'
    #    'q=Apple&'
    #    'from=2022-05-02&'
    #    'sortBy=popularity&'
    #    'apiKey=d3afaf05f0a744be8752d41b2ad1d279')
# https://newsapi.org/v2/top-headlines/sources?apiKey=API_KEY

from flask import Flask, render_template
# from app import app

from newsapi import NewsApiClient



app = Flask(__name__)



@app.route('/')
def index():

    newsapi = NewsApiClient(api_key='d3afaf05f0a744be8752d41b2ad1d279')
    top_headlines = newsapi.get_top_headlines(sources = 'bbc-news, buzzfeed, al-jazeera-english, bbc-sport, the-verge')
    

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

    return render_template('index.html',contents=contents)




if __name__ == '__main__':
    app.run(debug=True)