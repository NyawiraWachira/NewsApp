class Article:
    '''
    Article class to define article objects for each news source.
    '''

    def __init__(self,title,description,urlToImage,publishedAt,url):
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.url= url