import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt = Options()
opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opt)
driver.get("https://www.amazon.in")
driver.implicitly_wait(5)
driver.maximize_window()
# e = driver.find_element(By.XPATH, "//button[@type='submit']")
wait = WebDriverWait(driver,10)
# e = wait.until(EC.presence_of_element_located((By.XPATH,"//button[@type='submit']")))
# if e is not None:
#     e.click()

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

l = driver.find_elements(By.XPATH,"//div[@data-cy='title-recipe']/a")
print(len(l))
for i in l:
    print(i.text)
time.sleep(2)
l[1].click()
# wait.until(EC.visibility_of(l[1])).click()

# time.sleep(2)
# driver.execute_script("window.open();")
# driver.switch_to.window(driver.window_handles[1])
# driver.get("https://google.com")
# driver.close()
# driver.switch_to.window(driver.window_handles[0])
# print(driver.title)