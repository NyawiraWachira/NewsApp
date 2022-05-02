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



# 
if __name__ == '__main__':
    app.run(debug=True)