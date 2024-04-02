

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

startTime = time.time()
service = Service("C:\\Users\\aniket.gupta\\Desktop\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://fasb.org/page/PageContent?pageId=/projects/recentlycompleted.html")
#driver.get("https://test.fasb.rws.fafus.org/projects/recently-completed-projects")
time.sleep(2)
for i in range(1,52):
    print(driver.find_element(By.XPATH,f"/html/body/div/div[1]/main/div[1]/div[3]/div[1]/div/div/ul/li[{i}]").text)

'''for i in range(1,21):
    b = driver.find_element(By.XPATH,f"//*[@id='table-scroll']/tbody/tr[{i}]").text
    print(b)

input("enter",)

for i in range(1,21):
    b = driver.find_element(By.XPATH,f"//*[@id='table-scroll']/tbody/tr[{i}]").text
    print(b)

input("enter",)
for i in range(1,12):
    b = driver.find_element(By.XPATH,f"//*[@id='table-scroll']/tbody/tr[{i}]").text
    print(b)'''