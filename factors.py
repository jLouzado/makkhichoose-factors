import cgi
import webapp2

MAIN_PAGE_HTML = """\
<html>
  <body>
    <form action="/factors" method="post">
      <div><input type="text" name="number"><br></div>
      <div><input type="submit" value="Find Factors"></div>
    </form>
  </body>
</html>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)

class Factors(webapp2.RequestHandler):
    def post(self):
        self.response.write('<html><body>Your number is: ')
        self.response.write(cgi.escape(self.request.get('number')))
        self.response.write('</body></html>')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/factors', Factors),
], debug=True)