from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.google.com")
assert "Google" in driver.title
driver.close()
