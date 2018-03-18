import urllib, urllib2, cookielib, webbrowser, os

url = "http://www.wsb.com/Assignment2/case06.php"

cookie_jar = cookielib.CookieJar()

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
urllib2.install_opener(opener)

request = urllib2.Request(url)
urllib2.urlopen(request)

tmp_url = "/tmp/tmp.html"
tmp_file = open(tmp_url, "w")
for cookie in cookie_jar:
    if cookie.name == "Flag":
        tmp_file.write("<script>alert(\"" + cookie.value + "\")</script>")
tmp_file.close()

webbrowser.open("file://" + os.path.realpath(tmp_url))