import sys
from collections import defaultdict


def split_this(tweet):

    if len(tweet.encode('utf-8')) <= 140:

        return tweet

    else:

        tweet_broken = str.split(tweet)

        number_of_tweets = 1

        tweet_dict = defaultdict()

        tweet_dict[1] = ''

        for word in tweet_broken:

            if len((tweet_dict[number_of_tweets] + ' ' + word).encode('utf')) > 134:

                number_of_tweets += 1

                tweet_dict[number_of_tweets] = word

            else:

                tweet_dict[number_of_tweets] += ' ' + word

        for num_tweet in tweet_dict.keys():
            tweet_dict[num_tweet] = tweet_dict[num_tweet].lstrip() + ' ({}/{})'.format(num_tweet, number_of_tweets)

        return list(tweet_dict.values())


if __name__ == '__main__':

    tweet = sys.argv[1]

    for line in split_this(tweet):

        print(line)
