from google.appengine.ext import ndb
# from googleapiclient import discovery
from random import shuffle


class Ghost(ndb.Model):
    gmail = ndb.UserProperty()
    ghost_name = ndb.StringProperty()
    first_name = ndb.StringProperty()
    second_name = ndb.StringProperty()


class GhostrEngine:

    @classmethod
    def setup(cls):
        for name in SpreadsheetProcessor().results:
            if name not in [ghost.ghost_name for ghost in cls.list_all()]:
                ghost = Ghost()
                ghost.ghost_name = name
                ghost.put()

    @classmethod
    def set_form_text(cls, user):
        if cls.get_from_user(user):
            return "Change your current Phantom name"
        else:
            return "Get a Phantom name"

    @staticmethod
    def list_random_three():
        ghosts = Ghost.query()
        available_ghosts = [
            ghost.ghost_name for ghost in ghosts if not ghost.gmail]
        shuffle(available_ghosts)
        return available_ghosts[:3]

    @staticmethod
    def list_all():
        return Ghost.query()

    @staticmethod
    def get_from_user(user):
        if user:
            return Ghost.query(Ghost.gmail == user).get()

    @staticmethod
    def get_from_ghostname(name):
        return Ghost.query(Ghost.ghost_name == name).get()

    @staticmethod
    def clear_user_data(ghost):
        ghost.first_name = None
        ghost.second_name = None
        ghost.gmail = None
        ghost.put()


class SpreadsheetProcessor:

    def __init__(
            self,
            spreadsheet_id='1R-xulhVpfaXOfvx05mLK7G5WvpIRk6eJLi99UlvC8RM',
            range_='A2:A44'):
        """
        This code has been commented out due to an import error thrown by one of googleapiclient's dependencies 'six.moves'.
        You can see full details on the blocker here:
        https://stackoverflow.com/questions/54276516/google-api-python-client-from-six-moves-import-zip-importerror-no-module-name
        The results of the API call have been hardcoded temporarily whilst this issue is being fixed.
        """
        # service = discovery.build('sheets', 'v4')
        # request = service.spreadsheets().values().get(
        #     spreadsheetId=spreadsheet_id, range=range_)
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
