from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
startTime = time.time()
service = Service("C:\\Users\\aniket.gupta\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.implicitly_wait(10)
driver.get("https://interactivity-staging-viacom18.web.app/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "input[name=email]").click()
driver.find_element(By.CSS_SELECTOR, "input[name=email]").send_keys("vaibhav.sharma@webdunia.net")
driver.find_element(By.XPATH, "//*[@id='password']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='password']").send_keys("Admin@Viacom18")
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div/main/div/form/button/span[1]").click()
time.sleep(1)
print("Logged in IMS")