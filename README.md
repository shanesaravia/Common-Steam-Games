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
[Beautiful Soup 4.6.0](https://pypi.python.org/pypi/beautifulsoup4)  
[Yaml 3.12](http://www.yaml.org/start.html)

## Retrieving Steam API Key
1. Navigate to https://steamcommunity.com/dev/apikey and login with steam credentials.
2. Input a domain name and check the "I agree" box.
3. Click Register. Your API key should now appear.

## Example Config File
```
api_key: 123abc123abc123abc123abc
users:
	- steamID1
	- steamID2
	- steamID3
```

## Author
**Shane Saravia**

##License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/shanesaravia/Common-Steam-Games/blob/master/LICENSE) file for details