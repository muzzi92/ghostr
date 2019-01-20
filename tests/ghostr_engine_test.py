from src.ghostr_engine import GhostrEngine
from src.models import Ghost
import unittest
from google.appengine.api import users
from google.appengine.api import memcache
from google.appengine.ext import ndb
from google.appengine.ext import testbed
from random import shuffle

import os,sys
sys.path.append(os.getcwd())

class GhostrEngineTestCase(unittest.TestCase):

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        ndb.get_context().clear_cache()

    def tearDown(self):
        self.testbed.deactivate()

    def testSetup(self):
        test_names = ["Tom", "Dick", "Harry"]
        GhostrEngine.setup(test_names)

        stored_ghosts = Ghost.query()

        for ghost in stored_ghosts:
            assert ghost.ghost_name in test_names

    def testSetFormText(self):
        user_one = users.User("returning@example.com")
        user_two = users.User("new@example.com")

        ghost = Ghost(gmail=user_one).put()

        assert GhostrEngine.set_form_text(user_one) == "Change your current Phantom name"
        assert GhostrEngine.set_form_text(user_two) == "Get a Phantom name"

    def testListRandomThree(self):
        user = users.User("test@example.com")

        ghost_one = Ghost(ghost_name="Tom", gmail=user)
        ghost_two = Ghost(ghost_name="Dick")
        ghost_three = Ghost(ghost_name="Harry")

        ndb.put_multi([ghost_one, ghost_two, ghost_three])

        available_ghosts = GhostrEngine.list_random_three()

        assert "Harry" in available_ghosts
        assert "Dick" in available_ghosts
        assert "Tom" not in available_ghosts

    def testListAll(self):
        ghost_one = Ghost(ghost_name="Tom")
        ghost_two = Ghost(ghost_name="Dick")
        ghost_three = Ghost(ghost_name="Harry")

        ndb.put_multi([ghost_one, ghost_two, ghost_three])

        result = GhostrEngine.list_all()

        assert result.count() == 3

    def testGetFromUser(self):
        user = users.User("test@example.com")
        ghost = Ghost(gmail=user)

        ghost.put()

        assert GhostrEngine.get_from_user(user) == ghost
        assert GhostrEngine.get_from_user(None) == None

    def testGetFromGhostname(self):
        ghost = Ghost(ghost_name="Tom")
        ghost.put()

        assert GhostrEngine.get_from_ghostname("Tom") == ghost

    def testClearUserData(self):
        user = users.User("test@example.com")
        first_name = "Master"
        second_name = "Roshi"
        ghost_name = "Babadook"

        ghost = Ghost(gmail=user, first_name=first_name, second_name=second_name, ghost_name=ghost_name)
        ghost.put()

        stored_ghost = Ghost.query().get()

        assert stored_ghost.gmail == user
        assert stored_ghost.first_name == first_name
        assert stored_ghost.second_name == second_name
        assert stored_ghost.ghost_name == ghost_name

        GhostrEngine.clear_user_data(stored_ghost)

        updated_stored_ghost = Ghost.query().get()

        assert updated_stored_ghost.gmail == None
        assert updated_stored_ghost.first_name == None
        assert updated_stored_ghost.second_name == None
