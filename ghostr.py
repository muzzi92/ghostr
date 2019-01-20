import os
from google.appengine.ext.webapp import template
from models import GhostrEngine
from google.appengine.api import users
import webapp2

GhostrEngine.setup()

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        template_values = {
            'ghosts': GhostrEngine.list_all(),
            'user': user,
            'form_linktext': GhostrEngine.set_form_text(user),
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
        template_values = {
            'first_name': self.request.get('first_name'),
            'second_name': self.request.get('second_name'),
            'ghost_names': GhostrEngine.list_random_three(),
        }

        path = os.path.join(
            os.path.dirname(__file__),
            'templates/selection.html')
        self.response.out.write(template.render(path, template_values))


class CreatePage(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        previous_ghost = GhostrEngine.get_from_user(user)

        if previous_ghost:
            GhostrEngine.clear_user_data(previous_ghost)

        ghost = GhostrEngine.get_from_ghostname(self.request.get('ghost_name'))
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
