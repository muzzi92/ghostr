from spreadsheet_processor import SpreadsheetProcessor
from models import Ghost
from random import shuffle


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
