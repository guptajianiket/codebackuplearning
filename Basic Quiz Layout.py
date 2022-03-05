from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
startTime = time.time()
service = Service("C:\\Users\\aniket.gupta\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
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
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div/div[1]/div/div/ul/div[3]/div[2]").click()


# Click on Quiz
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div/div[1]/div/div/ul/div[2]/div[2]").click()

# Click on Create Quiz
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div/div[2]/div[1]/p").click()
time.sleep(3)

# Select Channel
#driver.find_element(By.CSS_SELECTOR, f"input[value={input('Enter the channel name properly: ', )}]").click()
driver.find_element(By.CSS_SELECTOR, "input[value=Colors]").click()

time.sleep(1)

# Click on new
#driver.find_element(By.CSS_SELECTOR, "input[value=New]").click()

# Enter New Show Name
#driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/div[1]/div/input").send_keys(f"{input('Enter the show name properly: ', )}")

# Click on Show Type
#driver.find_element(By.CSS_SELECTOR, f"input[value={input('Enter the show type properly', )}]").click()

# Click on show list
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/div[1]/div/div").click()
time.sleep(2)

# Click on the show
driver.find_element(By.XPATH, "//*[@id='menu-']/div[3]/ul/li[2]").click()
time.sleep(2)

# Save and Next
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/div[3]/button").click()
time.sleep(2)

# Click on design space
wrapper = driver.find_element(By.XPATH, "//*[@id='uiMan']/div[1]/div[1]/div[1]/iframe")
wrapper.click()

# Clikc on style manager icon
driver.find_element(By.XPATH, "//*[@id='uiMan']/div[1]/div[2]/div[3]/div/span[1]").click()

# Click on decoration of the background
driver.find_element(By.XPATH, "//*[@id='gjs-sm-decorations']/div[1]").click()

# Clear and Enter Background Color
driver.find_element(By.XPATH, "//*[@id='gjs-sm-background-color']/div[2]/div/div[1]/input").clear()
driver.find_element(By.XPATH, "//*[@id='gjs-sm-background-color']/div[2]/div/div[1]/input").send_keys("#0d0620")

# Click on save icon
driver.find_element(By.XPATH, "//*[@id='uiMan']/div[1]/div[2]/div[2]/div/span[6]").click()


