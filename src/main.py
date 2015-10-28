import tweepy, time, random, sys

def main():
    CONSUMER_KEY = find_setting('consumer_key')
    CONSUMER_SECRET = find_setting('consumer_secret')
    ACCESS_KEY = find_setting('access_key')
    ACCESS_SECRET = find_setting('access_key_secret')

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    while True:
        minion_tweets = api.search(q=find_setting('keyword_search'), count=int(find_setting('reply_count')))

        try:
            answers_file = open(find_setting('answers_file'), 'r')
            minion_answers = answers_file.read().splitlines()
            answers_file.close()
        except IOError:
            print "Could not find answers file (%s)." % find_setting('answers_file')
            sys.exit(0)

        for minion_tweet in minion_tweets:
            sn = minion_tweet.user.screen_name
            minion_answer = "@%s %s" % (sn, random.choice(minion_answers))
            api.update_status(status=minion_answer, in_reply_to_status_id=minion_tweet.id)
            print "Posted reply to: %s" % minion_tweet.id
        
        print "Waiting %s seconds for next session" % find_setting('seconds_between_replies')
        time.sleep(int(find_setting('seconds_between_replies')))

# Thanks to this wonderful tutorial http://www.decalage.info/en/python/configparser, this was easy
def settings():
    settings = {}
    settings_file = open("custom/settings.txt")
    for line in settings_file:
        if "#" in line:
            line, comment = line.split("#", 1)
        if "=" in line:
            setting, value = line.split("=", 1)

            setting = setting.strip()
            value = value.strip()

            settings[setting] = value
    settings_file.close()
    return settings

def find_setting(key):
    try:
        return settings()[key]
    except KeyError:
        print "Key '%s' not found in settings file, please check again." % key
        sys.exit(0)

if __name__ == '__main__':
    main()