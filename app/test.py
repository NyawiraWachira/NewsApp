import unittest

from models import source


Source = source.Source



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
