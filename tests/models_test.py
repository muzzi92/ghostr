import unittest

from google.appengine.api import users
from google.appengine.api import memcache
from google.appengine.ext import ndb
from google.appengine.ext import testbed

from src.models import Ghost

import os,sys
sys.path.append(os.getcwd())

class GhostTestCase(unittest.TestCase):

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        ndb.get_context().clear_cache()

    def tearDown(self):
        self.testbed.deactivate()

    def testInsertEntity(self):
        Ghost().put()
        self.assertEqual(1, len(Ghost.query().fetch(2)))

    def testGhostProperties(self):
        user = users.User("test@example.com")
        first_name = "Master"
        second_name = "Roshi"
        ghost_name = "Babadook"

        ghost = Ghost(gmail=user, first_name=first_name, second_name=second_name, ghost_name=ghost_name)
        ghost.put()

        stored_ghost = Ghost.query().get()

        self.assertEqual(user, stored_ghost.gmail)
        self.assertEqual(first_name, stored_ghost.first_name)
        self.assertEqual(second_name, stored_ghost.second_name)
        self.assertEqual(ghost_name, stored_ghost.ghost_name)



if __name__ == '__main__':
    unittest.main()
