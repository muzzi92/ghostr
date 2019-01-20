import os
from google.appengine.ext.webapp import template
from models import GhostDatabase
from google.appengine.api import users
import webapp2

GhostDatabase().setup()


class MainPage(webapp2.RequestHandler):
    def get(self):
        gdb = GhostDatabase()

        user = users.get_current_user()

        if gdb.get_from_user(user):
            form_linktext = "Change your current Phantom name"
        else:
            form_linktext = "Get a Phantom name"

        template_values = {
            'ghosts': gdb.list_all(),
            'user': user,
            'form_linktext': form_linktext,
        }

        path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
        self.response.out.write(template.render(path, template_values))


class EntryPage(webapp2.RequestHandler):
    def get(self, template_values=dict()):
        if users.get_current_user():
            auth_url = users.create_logout_url(self.request.uri)
            auth_linktext = 'Logout'
        else:
            auth_url = users.create_login_url(self.request.uri)
            auth_linktext = 'Login'

        template_values = {
            'user': users.get_current_user(),
            'auth_url': auth_url,
            'auth_linktext': auth_linktext,
        }

        path = os.path.join(os.path.dirname(__file__), 'templates/entry.html')
        self.response.out.write(template.render(path, template_values))


class SelectionPage(webapp2.RequestHandler):
    def post(self):
        ghost_names = GhostDatabase().list_random_three()

        template_values = {
            'first_name': self.request.get('first_name'),
            'second_name': self.request.get('second_name'),
            'ghost_names': ghost_names,
        }

        path = os.path.join(
            os.path.dirname(__file__),
            'templates/selection.html')
        self.response.out.write(template.render(path, template_values))


class CreatePage(webapp2.RequestHandler):
    def post(self):
        gdb = GhostDatabase()
        user = users.get_current_user()
        previous_ghost = gdb.get_from_user(user)

        if previous_ghost:
            gdb.clear_user_data(previous_ghost)

        ghost = gdb.get_from_ghostname(self.request.get('ghost_name'))
        ghost.first_name = self.request.get('first_name')
        ghost.second_name = self.request.get('second_name')
        ghost.gmail = user
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
