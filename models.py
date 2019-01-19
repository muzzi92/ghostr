from google.appengine.ext import db
from googleapiclient import discovery

class Ghost(db.Model):
    gmail = db.UserProperty()
    ghost_name = db.StringProperty()
    first_name = db.StringProperty()
    second_name = db.StringProperty()


class SpreadsheetProcessor:

    def __init__(self, spreadsheet_id='1R-xulhVpfaXOfvx05mLK7G5WvpIRk6eJLi99UlvC8RM', range_='A2:A44'):
        service = discovery.build('sheets', 'v4', credentials=None)
        request = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_)
        response = request.execute()
        self.results = [value[0] for value in response['values']]


class Database:

    def setup_ghosts(self):
         for name in SpreadsheetProcessor().results:
            ghost = Ghost()
            ghost.ghost_name = name
            ghost.put()
