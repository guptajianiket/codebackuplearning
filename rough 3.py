from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
startTime = time.time()
service = Service("C:\\Users\\aniket.gupta\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.get("https://www.voot.com/shows/the-big-picture/309295")
time.sleep(3)
# Click on the leaders banner
driver.find_element(By.PARTIAL_LINK_TEXT, "View Now").click()
time.sleep(2)
driver.find_elements(By.XPATH, "//*[@id='HybridRailId']/div[2]/div/div/div/div/div/a/div/div[2]/div/button")[2].click()
time.sleep(2)
# Log in Page appeared
# Click on the mobile number
#driver.switch_to.frame(0)\
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div[3]/div[3]/p").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='mobile number']").click()
driver.find_element(By.XPATH, "//*[@id='mobile number']").send_keys("7987142067")
driver.find_element(By.XPATH, "//html/body/div[2]/div[2]/div/div/div[2]/div[2]/button").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='enter password']").click()
driver.find_element(By.XPATH, "//*[@id='enter password']").send_keys("h@rrold95")
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div[2]/div[2]/button").click()
time.sleep(2)
#driver.switch_to.default_content()
driver.get_screenshot_as_png()