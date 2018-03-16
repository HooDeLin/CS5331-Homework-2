import urllib, urllib2
from HTMLParser import HTMLParser

csrf = ""

class HTML_Parser(HTMLParser):
  def handle_startendtag(self, tag, attrs):
    if tag == 'input':
      attribute_dict = dict(attrs)
      if attribute_dict['name'] == 'csrf_token':
        global csrf
        csrf = attribute_dict['value']

# Scrape original page
url = 'http://www.wsb.com/Assignment2/case09.php'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
content = response.read()

# Pass the content to the HTML_Parser to parse the content to find the csrf value
parser = HTML_Parser()
parser.feed(content)

# Create new request with the required info
post_values = dict(data='Test Data', csrf_token=csrf)
data = urllib.urlencode(post_values)
post_request = urllib2.Request(url, data)
post_response = urllib2.urlopen(post_request)

with open('results.html', 'w') as file:
  file.write(post_response.read())

import webbrowser
new = 2
webbrowser.open('results.html', new=new)
