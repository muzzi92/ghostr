# from googleapiclient import discovery


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
