import unittest
from src.tweet_split import split_this


class TestTweetSplit(unittest.TestCase):

    def test_split_this_short(self):

        full_tweet = split_this('a short tweet!')

        self.assertEqual(full_tweet, 'a short tweet!')

    def test_split_this_in_two(self):

        text = 'This is a rather long tweet that will need splitting in two. I will do that adding numbering, ' \
               'so that people can follow the train of my thoughts, wherever it may lead.'

        full_tweet = split_this(text)

        self.assertListEqual(full_tweet,
                             ['This is a rather long tweet that will need splitting in two. I will do that adding '
                              'numbering, so that people can follow the train of (1/2)',
                              'my thoughts, wherever it may lead. (2/2)'])