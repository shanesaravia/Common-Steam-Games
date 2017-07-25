import steamapi
import requests
from bs4 import BeautifulSoup
import yaml
import os
from functools import reduce

class Configs(object):


    def config(self):
        """ Returns Config File """
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        with open('steamConfig.yml', 'r') as config:
            return yaml.load(config)

    def steamConnect(self, api):
        """Returns validated steamapi instance."""
        steamapi.core.APIConnection(api, validate_key=True)
        return steamapi


class SteamGet(Configs):


    def __init__(self):
        pass

    def getGames(self, userName):
        """Returns games owned by specific Steam profile."""
        user = steamapi.user.SteamUser(userurl=userName)
        return user.games

    def masterList(self, users):
        """Return a single list of all user's games lists."""
        return [self.getGames(user) for user in users]

    def compareGames(self, games1, games2):
        """Returns common games between 2 users."""
        return set(games1).intersection(set(games2))

    def doReduce(self, config):
        """Compares games and returns a list of common games"""
        return list(reduce(self.compareGames, self.masterList(config['users'])))

class GameType(SteamGet):

    def __init__(self):
        self.session = requests.Session()
        self.types = ['Online Multi-Player',
                      'Online Multi-player',
                      'Multi-player',
                      'Multi-Player',
                      'Co-op']

    def getType(self, gameID):
        """Checks if game requires agecheck, continue, or none"""
        r = self.session.get('http://store.steampowered.com/app/{}/'.format(gameID))

        payload = {
            'snr':'1_agecheck_agecheck__age-gate',
            'ageDay':1,
            'ageMonth':'January',
            'ageYear':1902}

        cookie = {'mature_content':'1',
            'steamCountry':'CA%7Cc790e5063a5c52849a750642f2d1d096',
            'browserid':'1180357007006147168',
            'sessionid':'25c853b96c4eb64ad3059861',
            'timezoneOffset':'-14400,0'}

        if r.history:
            # Checks if r.history is blank. If not blank, implies redirect.
            # If redirected, must require age check or click continue.
            try:
                # Attempt age check.
                return self.ageCheck(gameID, payload, cookie, r)
            except IndexError:
                # Attempt click continue.
                return self.clickContinue(gameID, payload, cookie, r)
        else:
            # If r.history blank, no redirects, try regular page.
            return self.noCheck(gameID, payload, cookie, r)




    def ageCheck(self, gameID, payload, cookie, r):
        """Returns True for game that requires an age check."""
        resp = self.session.post('http://store.steampowered.com/agecheck/app/{}/'.format(gameID), data=payload, cookies=cookie)

        soup = BeautifulSoup(resp.content, 'html.parser')
        playTypes = soup.select('.name')
        return self.multiplayerCheck(playTypes)

    def clickContinue(self, gameID, payload, cookie, r):
        """Returns True for game that requires only a 'Click continue'."""
        resp = self.session.get('http://store.steampowered.com/app/{}/agecheck:605'.format(gameID), cookies=cookie)
        soup = BeautifulSoup(resp.content, 'html.parser')
        playTypes = soup.select('.name')
        return self.multiplayerCheck(playTypes)

    def noCheck(self, gameID, payload, cookie, r):
        """Returns True for game that doesnt require any checks'."""
        soup = BeautifulSoup(r.content, 'html.parser')
        playTypes = soup.select('.name')
        return self.multiplayerCheck(playTypes)

    def multiplayerCheck(self, playTypes):
        for i in playTypes:
            if i.text in self.types:
                return True

class Main(GameType):

    def run():
        app = Main()
        config = app.config()
        app.steamConnect(config['api_key'])

        masterList = app.doReduce(config)

        for item in masterList:
            if app.getType(item.id):
                print(item.name)

Main.run()
