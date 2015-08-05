# Minion hate bot

## About
Minion hate bot is an angry bot that, every fifteen minutes, replies to 15 tweets containing the word "minions". You can find the Twitter account [here](https://twitter.com/minionsareevil).

## Installation

1. Register a Twitter application ([apps.twitter.com](https://apps.twitter.com)). In order for this to work you must have a Twitter account and a phone number associated with it

2. Generate an ACCESS_KEY and ACCESS_SECRET under the tab "Keys and Access Tokens"

2. Install the code

    ```bash
    $ git clone https://github.com/djangokillen/minion-hate-bot.git
    ```

3. Adjust configuration
    
    Edit the file minions.py with the configuration parameters below

    Configuration parameters:
    `Consumer key` consumer key of your Twitter application. Can be found in the tab "Keys and Access Tokens"
    `Consumer secret` consumer secret of your Twitter application. Can be found in the tab "Keys and Access Tokens"
    `Access token` access token of your Twitter application. To generate it; look at step 2
    `Access token secret` access token secret of your Twitter application. To generate it; look at step 2

4. Running it in the background

    The process can be ran in the background with the command [nohup](https://en.wikipedia.org/wiki/Nohup). With this command you can safely close down the command line without having to worry about it not working anymore.

    To make the command work, open up your command line and type this: 

        ```bash
        $ nohup /usr/bin/python /path/to/python/script &
        ```

    The python script should now run every 15 minutes and be fully automated.

5. You should see your bot tweeeting about how they fully DESPISE minions!

## License
This repository is released under the [MIT license](LICENSE.md).