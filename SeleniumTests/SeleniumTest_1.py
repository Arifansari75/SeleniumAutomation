import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()
time.sleep(2)