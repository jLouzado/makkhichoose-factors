import cgi
import webapp2
import logging

MAIN_PAGE_HTML = """\
<html>
  <body>
    <form action="/result" method="post">
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

        self.response.write('<html><body>The factors are: ')
        self.response.write(factors)
        self.response.write('</body></html>')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/result', Factors),
], debug=True)