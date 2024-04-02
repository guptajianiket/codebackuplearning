from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
startTime = time.time()
service = Service("C:\\Users\\aniket.gupta\\Desktop\\chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.implicitly_wait(10)
driver.get("https://interactivity-prod-viacom18.web.app/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "input[name=email]").click()
driver.find_element(By.CSS_SELECTOR, "input[name=email]").send_keys("aniket.gupta@rws.com")
driver.find_element(By.XPATH, "//*[@id='password']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='password']").send_keys("Viacom@123")
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div/main/div/form/button/span[1]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div/div[1]/div/div/ul/div[3]/div[2]").click()
print("Logged in IMS")

# Click on Voting
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div/div[1]/div/div/ul/div[3]/div[2]").click()

# Click on Reporting
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div/div[2]/div[3]/p").click()
time.sleep(3)

# click on the on demand report icon
driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/div[1]/table/tbody/tr[2]/td[2]/a[1]").click()
time.sleep(3)

# Click on the 1st episode icon
driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/div/div[1]/div/div/div/div[3]/table/tbody/tr[1]/td[4]/div/label/span[1]/span[1]/input").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='standard-full-width']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='standard-full-width']").send_keys("aniket.gupta@rws.com")
driver.find_element(By.XPATH,
                    "//*[@id='call-for-entry']/div[2]/div/div[1]/div/div/div/div[4]/div/div/div[2]/button").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div[2]/div/button").click()
print("1 report sent.")
time.sleep(15)

for i in range (2,14):
    driver.find_element(By.XPATH,f"//*[@id='call-for-entry']/div[2]/div/div[1]/div/div/div/div[3]/table/tbody/tr[{i}]/td[4]/div/label/span[1]/span[1]/input").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/div/div[2]/div/button").click()
    print(f"{i} report sent.")
    time.sleep(15)