from google.appengine.ext import db
from apiclient import discovery
from random import shuffle


class Ghost(db.Model):
    gmail = db.UserProperty()
    ghost_name = db.StringProperty()
    first_name = db.StringProperty()
    second_name = db.StringProperty()


class SpreadsheetProcessor:

    def __init__(
            self,
            spreadsheet_id='1R-xulhVpfaXOfvx05mLK7G5WvpIRk6eJLi99UlvC8RM',
            range_='A2:A44'):
        service = discovery.build('sheets', 'v4')
        request = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id, range=range_)
        # response = request.execute()
        # self.results = [value[0] for value in response['values']]

        self.results = [
            u'Betelgeuse',
            u'Bhoot',
            u'Bloody Mary',
            u'Bogle',
            u'Casper',
            u'Chindi',
            u'Cihuateteo',
            u'Clytemnestra',
            u'Draugr',
            u'Dybbuk',
            u'Gjenganger',
            u'Gu\u012d',
            u'Ibbur',
            u'Jima',
            u'Jinn',
            u'La Llorona',
            u'Moaning Myrtle',
            u'Mr. Boogedy',
            u'Nachzehrer',
            u'Blinky',
            u'Pinky',
            u'Inky',
            u'Clyde',
            u'Patrick Swayze',
            u'Phi Tai Hong',
            u'Pishacha',
            u'Poltergeist',
            u'Revenant',
            u'Ringwraith',
            u'Slender Man',
            u'Slimer',
            u'Space Ghost',
            u'Strigoi',
            u'Candyman',
            u'The Crypt Keeper',
            u'Headless Horseman',
            u'Tom\xe1s',
            u'Vetala',
            u'Wiederg\xe4nger',
            u'Xunantunich',
            u'Y\u016brei',
            u'Zhong Kui',
            u'Zuul']


class GhostDatabase:

    def setup(self):
        for name in SpreadsheetProcessor().results:
            if name not in [ghost.ghost_name for ghost in self.list_all()]:
                ghost = Ghost()
                ghost.ghost_name = name
                ghost.put()

    def list_random_three(self):
        ghosts = db.GqlQuery("SELECT * FROM Ghost")
        available_ghosts = [ghost.ghost_name for ghost in ghosts if not ghost.gmail]
        shuffle(available_ghosts)
        return available_ghosts[:3]

    def list_all(self):
        return db.GqlQuery("SELECT * FROM Ghost")

    def get_from_user(self, user):
        if user:
            matches = db.GqlQuery("SELECT * FROM Ghost WHERE gmail = :value", value=user)
            try:
                return matches[0]
            except IndexError:
                print("No Ghost Identity found for User {}".format(user))

    def get_from_ghostname(self, name):
        matches = db.GqlQuery("SELECT * FROM Ghost WHERE ghost_name = :value", value=name)
        return matches[0]

    def clear_user_data(self, ghost):
        ghost.first_name = None
        ghost.second_name = None
        ghost.gmail = None
        ghost.put()
