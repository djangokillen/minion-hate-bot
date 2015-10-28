# Minion hate bot

## About
Minion hate bot is an angry bot that, every fifteen minutes, replies to 5 tweets containing the word "minions". You can find the Twitter account [here](https://twitter.com/minionsareevil). It is currently not active.

You can customize the reply count and time between the replies through the settings file, located in `custom/settings.txt`. However, keep in mind that it of course not should pass the Twitter API limit. The default is 5 replies every fifteen minutes (reply\_count=5, seconds\_between_replies=900).

## Requirements
This package uses [Tweepy](http://www.tweepy.org), the time module, the sys module and the random module to function. Built with Python 2.

## Installation

1. Register a Twitter application ([apps.twitter.com](https://apps.twitter.com)). In order for this to work you must have a Twitter account and a phone number associated with it.

2. Generate an ACCESS_KEY and ACCESS_SECRET under the tab "Keys and Access Tokens"

2. Install the code

    ```bash
    $ git clone https://github.com/djangokillen/minion-hate-bot.git
    ```

3. Adjust configuration
    
    Edit the file `settings.txt`, located in the custom folder with the configuration parameters below.

    `consumer_key` - consumer key of your Twitter application. Can be found in the tab "Keys and Access Tokens"

    `consumer_secret` - consumer secret of your Twitter application. Can be found in the tab "Keys and Access Tokens"

    `access_key` - access token of your Twitter application. To generate it; look at step 2

    `access_key_secret` - access token secret of your Twitter application. To generate it; look at step 2

    Read more about the rest of the parameters under "Customization".

## Running it

To run it, cd into the root of your downloaded project and write the following:

```bash
$ python src/main.py
```

### Running it in the background

The process can be ran in the background with the command [nohup](https://en.wikipedia.org/wiki/Nohup). With this command you can safely close down the command line without having to worry about it not working anymore.

To make the command work, open up your command line and type this: 

```bash
$ nohup /usr/bin/python /path/to/python/script &
```

The python script should now run every 15 minutes and be fully automated.

(Warning: this will stop working if you shut down your computer, or just close it down temporarily if you have a laptop. Not a good solution.)

## Customization
Customizing this project is very easy. All you have to do is find the settings file, located in `custom/answers/settings.txt` and change it however you want. These are the configuration parameters below that the main.py file takes into account:

`consumer_key` - See section "Adjust configuration" for more information.

`consumer_secret` - See section "Adjust configuration" for more information.

`access_key` - See section "Adjust configuration" for more information.

`access_key_secret` - See section "Adjust configuration" for more information.

`keyword_search` - What the bot will search for to reply to those tweets it will reply to. Default is "minion".

`answers_file` - Path to the file where the bot picks a random answer from. Default is "custom/answers/answers.txt".

`reply_count` - How many tweets the bot should reply to per session. Default is 5.

`seconds_between_replies` - How many seconds it should wait when it is finished with a session. Default is 900 seconds (15 minutes).

## Final result

You should see your bot tweeeting about how they fully DESPISE minions!

## License
This repository is released under the [MIT license](LICENSE).