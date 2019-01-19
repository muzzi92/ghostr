import os
from google.appengine.ext.webapp import template

from google.appengine.ext import db
from google.appengine.api import users
import webapp2

def get_current_ghost():
  """Constructs a datastore key for a Guestbook entity with guestbook_name."""
  user = users.get_current_user()
  query = db.GqlQuery("SELECT * FROM Ghost WHERE gmail = :gmail", gmail=user)
  return query[0]

class Ghost(db.Model):
    gmail = db.UserProperty()
    ghost_name = db.StringProperty()
    first_name = db.StringProperty()
    second_name = db.StringProperty()


class MainPage(webapp2.RequestHandler):
    def get(self):
        ghosts = db.GqlQuery("SELECT * FROM Ghost ")
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'ghosts': ghosts,
            'user': users.get_current_user(),
            'url': url,
            'url_linktext': url_linktext,
        }

        path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
        self.response.out.write(template.render(path, template_values))

class EntryPage(webapp2.RequestHandler):
    def get(self, template_values=dict()):
        path = os.path.join(os.path.dirname(__file__), 'templates/entry.html')
        self.response.out.write(template.render(path, template_values))

class SelectionPage(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        ghost = Ghost()
        ghost.gmail = user
        ghost.first_name = self.request.get('first_name')
        ghost.second_name = self.request.get('second_name')
        ghost.put()

        ghost_names = ["Tom", "Dick", "Roldy"]

        template_values = {
            'first_name': ghost.first_name,
            'second_name': ghost.second_name,
            'ghost_names': ghost_names,
        }

        path = os.path.join(os.path.dirname(__file__), 'templates/selection.html')
        self.response.out.write(template.render(path, template_values))

class CreatePage(webapp2.RequestHandler):
    def post(self):
        ghost = get_current_ghost()

        ghost.ghost_name = self.request.get('ghost_name')

        ghost.put()

        self.redirect('/?')


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/entry', EntryPage),
    ('/selection', SelectionPage),
    ('/create', CreatePage),
], debug=True)

def main():
    application.run()

if __name__ == "__main__":
    main()
