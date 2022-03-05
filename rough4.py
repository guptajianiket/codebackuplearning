from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
startTime = time.time()
service = Service("C:\\Users\\aniket.gupta\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.implicitly_wait(10)
Action = ActionChains(driver)
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
print("Logged in IMS")
# Click on Quiz
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div/div[1]/div/div/ul/div[2]/div[2]").click()

# Click on Create Quiz
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div/div[2]/div[1]/p").click()
time.sleep(1)

# Select Channel
driver.find_element(By.CSS_SELECTOR, "input[value=Sonic]").click()

time.sleep(1)

# Click on show list
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/div[1]/div/div").click()
time.sleep(2)

# Click on the show
driver.find_element(By.XPATH, "//*[@id='menu-']/div[3]/ul/li[2]").click()
time.sleep(1)

# Save and Next
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/div[3]/button").click()
time.sleep(2)

# Click on save
driver.find_element(By.XPATH, "//*[@id='uiMan']/div[1]/div[2]/div[2]/div/span[6]").click()

# Get the action message
message = driver.find_element(By.XPATH, "/html/body/div[3]").text
print(message)
if message == "Data Failed to Save. Please try again.":
    driver.save_screenshot("Failure_SS.png")
if message == "Data Saved Successfully!!!":
    driver.get("https://www.voot.com/shows/the-big-picture/309295")
    Alert(driver).accept()
    time.sleep(3)
    # Click on the leaders banner
    driver.find_element(By.PARTIAL_LINK_TEXT, "View Now").click()
    time.sleep(2)
    driver.find_elements(By.XPATH, "//*[@id='HybridRailId']/div[2]/div/div/div/div/div/a/div/div[2]/div/button")[
        2].click()
    time.sleep(2)
    # Log in Page appeared
    # Click on the mobile number
    driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div[3]/div[3]/p").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='mobile number']").click()
    driver.find_element(By.XPATH, "//*[@id='mobile number']").send_keys("7987142067")
    driver.find_element(By.XPATH, "//html/body/div[2]/div[2]/div/div/div[2]/div[2]/button").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='enter password']").click()
    driver.find_element(By.XPATH, "//*[@id='enter password']").send_keys("h@rrold95")
    driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div[2]/div[2]/button").click()
    time.sleep(5)
    header = driver.find_element(By.XPATH,"//*[@id='ifrd']").is_displayed()
    if header == True:
        driver.save_screenshot('Live_FE_SS_1.png')
        Element = driver.find_element(By.XPATH,"//*[@id='multi-url-link']")
        driver.execute_script("arguments[0].scrollIntoView();", Element)
        time.sleep(2)
        driver.save_screenshot('Live_FE_SS_2.png')
    else:
        print("Tale manual SS. The page didn't appeared")

else:
    print("Script didn't executed successfully, please check it manually")