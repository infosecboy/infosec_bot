import tweepy

CONSUMER_KEY = ''
CONSUMER_SECRET=''
ACCESS_KEY=''
ACCESS_SECRET=''


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search,q=('#bugbounty OR #bugbountytip OR #BugBounty OR #hackerone  -filter:retweet'),lang='en').items(25):
    try:
        tweet.retweet()
    except tweepy.TweepError as e:
        print('Hi')
        print(e.reason)

    except StopInteration:
        break
