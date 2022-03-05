from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
startTime = time.time()
service = Service("C:\\Users\\aniket.gupta\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
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


# Click on Quiz
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div/div[1]/div/div/ul/div[2]/div[2]").click()

# Click on Create Quiz
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div/div[2]/div[1]/p").click()
time.sleep(3)

# Select Channel
driver.find_element(By.CSS_SELECTOR, "input[value=Colors]").click()

time.sleep(1)

# Click on show list
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/div[1]/div/div").click()
time.sleep(3)

# Click on the show
driver.find_element(By.XPATH, "//*[@id='menu-']/div[3]/ul/li[12]").click()
input("Wait")
# Save and Next
#driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/div[3]/button").click()
driver.find_element(By.CLASS_NAME, "MuiButton-label").click()
time.sleep(2)

# click on Open Layer Manager icon
driver.find_element(By.XPATH, "//*[@id='uiMan']/div[1]/div[2]/div[3]/div/span[3]").click()
time.sleep(2)

# Click on the body drop down
driver.find_element(By.XPATH, "//*[@id='uiMan']/div[1]/div[2]/div[5]/div[3]/div/div[1]/div/div/i").click()

# Click on container drop down
driver.find_element(By.XPATH,"//*[@id='uiMan']/div[1]/div[2]/div[5]/div[3]/div/div[3]/div/div/div[1]/div/div/i").click()
time.sleep(2)

# Click on the video element
driver.find_element(By.XPATH, "//*[@id='uiMan']/div[1]/div[2]/div[5]/div[3]/div/div[3]/div/div/div[4]/div/div[3]/div[1]/div/div/span").click()

# click on the setting icons
driver.find_element(By.XPATH, "//*[@id='uiMan']/div[1]/div[2]/div[3]/div/span[2]").click()

# Click on the source url box and remove the text and enter a new URL
driver.find_element(By.XPATH, "//*[@id='uiMan']/div[1]/div[2]/div[5]/div[4]/div[1]/div[2]/div[2]/div/div[2]/div/input").clear()
driver.find_element(By.XPATH, "//*[@id='uiMan']/div[1]/div[2]/div[5]/div[4]/div[1]/div[2]/div[2]/div/div[2]/div/input").send_keys("https://v3img.voot.com/tbp/Videos/WEEK_12_TBP_TUESDAY_QUIZ.mp4")


