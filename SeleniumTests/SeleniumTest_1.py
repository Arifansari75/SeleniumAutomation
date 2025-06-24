import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opt)
driver.get("https://www.amazon.in")
driver.implicitly_wait(5)
driver.maximize_window()

# selecting search bar and send test
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Iphone 16")
time.sleep(2)

# taking list of all seggestions from search bar
l = driver.find_elements(By.XPATH,"//div[@class='left-pane-results-container']/div/div/div[1]")
# time.sleep(2)
print(len(l))
for i in l:
    # print(i.text,end='\n')
    # k = i.get_attribute("aria-label")
    print(i.text)
    if "256+gb" in i.text:
        i.click()
        break
# time.sleep(2)
driver.close()