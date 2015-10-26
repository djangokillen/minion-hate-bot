import tweepy, time, random

def main():
    CONSUMER_KEY = 'your_consumer_key'
    CONSUMER_SECRET = 'your_consumer_secret'
    ACCESS_KEY = 'your_access_key'
    ACCESS_SECRET = 'your_access_secret'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    while True:
        minion_tweets = api.search(q="minions")

        try:
            answers_file = open('custom/answers/answers.txt', 'r')
            minion_answers = answers_file.read().splitlines()
            answers_file.close()
        except IOError:
            print "Oops, something went wrong. Could not find answers.txt file."

        for minion_tweet in minion_tweets:
            sn = minion_tweet.user.screen_name
            minion_answer = "@%s %s" % (sn, random.choice(minion_answers))
            api.update_status(status=minion_answer, in_reply_to_status_id=minion_tweet.id)
        
        time.sleep(900)

if __name__ == '__main__':
    main()