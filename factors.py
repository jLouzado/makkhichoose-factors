import os

import cgi
import jinja2
import webapp2
import logging

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render())

class Factors(webapp2.RequestHandler):
    def post(self):
        num = int(cgi.escape(self.request.get('number')))
        factors = []
        for i in range(1, num):
            if num % i == 0:
                higherFactor = num / i;
                factors.extend([i, higherFactor])
            # at a certain point 'i' will start to cross over into factors we've already found, we need to stop before then.
            if (i + 1) >= factors[len(factors) - 1]:
                # The last elememt will always have the most recent higher factor to check against.
                break

        # sorting the list of factors
        factors.sort()

        template = JINJA_ENVIRONMENT.get_template('result_factors.html')
        self.response.write(template.render({"result" : factors}))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/result', Factors),
], debug=True)