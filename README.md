# Common-Steam-Games
The purpose of this app is to help steam users detect which multiplayer games they have in common. This app works with any number of users and will only return the multiplayer games which all the users have in common.

## Getting Started
Following these instructions will get the code up and running on your local machine.

## Quick Guide
1. Download Common-Steam-Games and extract the zip file to where you want to store the software.
2. Navigate to https://steamcommunity.com/dev/apikey and login. You must follow the steps to receive your API key. (The app will not work without this API key)
3. Open steamConfig.yml and replace the API key with the one you received in the previous step.
4. Replace users with you and your friends Steam ID's.
5. Run steamApp.py and it will print out your common mulitplayer steam games. Enjoy!

## Dependencies
[Python 3](https://www.python.org/)  
[SteamApi](https://github.com/smiley/steamapi)  
[Requests 2.18.4](http://docs.python-requests.org/en/master/)  
[BeautifulSoup4 4.6.0](https://pypi.python.org/pypi/beautifulsoup4)  
[Yaml 3.12](http://www.yaml.org/start.html)