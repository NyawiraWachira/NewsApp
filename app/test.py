import unittest
from models import article
from models import source

Article = article.Article
Source = source.Source

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('Roe v Wade: US Supreme Court may overturn abortion rights, leak suggests - BBC','Millions could lose legal rights to abortion this summer, a leaked Supreme Court document shows.',
        'https://ichef.bbci.co.uk/news/1024/branded_news/A0E5/production/_124398114_gettyimages-1395079914.jpg','2022-05-03T10:08:35Z','https://www.bbc.com/news/world-us-canada-61302740')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_article.title,"Roe v Wade: US Supreme Court may overturn abortion rights, leak suggests - BBC")
        self.assertEqual(self.new_article.description,"Millions could lose legal rights to abortion this summer, a leaked Supreme Court document shows.")
        self.assertEqual(self.new_article.urlToImage,"https://ichef.bbci.co.uk/news/1024/branded_news/A0E5/production/_124398114_gettyimages-1395079914.jpg")
        self.assertEqual(self.new_article.publishedAt,"2022-05-03T10:08:35Z")
        self.assertEqual(self.new_article.url,"https://www.bbc.com/news/world-us-canada-61302740")

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.sources = Source('abc-news','al-jazeera-english','bbc-news','buzzfeed','cbs-news')

    def test_instance(self):
        self.assertTrue(isinstance(self.sources,Source))

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.sources.source_1,"abc-news")
        self.assertEqual(self.sources.source_2,"al-jazeera-english")
        self.assertEqual(self.sources.source_3,"bbc-news")
        self.assertEqual(self.sources.source_4,"buzzfeed")
        self.assertEqual(self.sources.source_5,"cbs-news")



if __name__ == '__main__':
    unittest.main()
