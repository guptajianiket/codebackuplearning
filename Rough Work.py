from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
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
print("Logged in IMS")
# Click on Quiz
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div/div[1]/div/div/ul/div[2]/div[2]").click()

# Click on Create Quiz
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div/div[2]/div[1]/p").click()
time.sleep(3)

# Select Channel
driver.find_element(By.CSS_SELECTOR, "input[value=Sonic]").click()

time.sleep(1)

# Click on show list
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/div[1]/div/div").click()
time.sleep(3)

# Click on the show
driver.find_element(By.XPATH, "//*[@id='menu-']/div[3]/ul/li[2]").click()
time.sleep(2)

# Save and Next
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/div[3]/button").click()
time.sleep(2)
input("press enter ", )

# Clikc on save main of page
driver.find_element(By.XPATH, "//*[@id='uiMan']/div[1]/div[2]/div[2]/div/span[6]").click()

msg = driver.find_element(By.XPATH,'/html/body/div[3]').text
expecectedmsg = "Data Saved Successfully!!!"
if msg==expecectedmsg:
    print("Page Saved")
else:
    print(msg)

# Click on the menu
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[1]/div/div/div").click()

# Click on the Create Line Up
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[1]/div/div/ul/li[6]").click()

# Click on add new episode icon
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div[2]/div[1]/div[2]/label").click()

# Insert the episode name
driver.find_element(By.XPATH, "//*[@id='lineup']").send_keys(f"{input('Please enter the episode name: ', )}")

# Click on add button
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div[2]/div[1]/div/div[2]/label[1]").click()

# Click on the Episode section
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div/div/div").click()

# Select the episode
driver.find_element(By.XPATH, "//*[@id='menu-']/div[3]/ul/li[2]").click()
# Haere above li[2] means second in the list, li[1] is for select and it goes on to li[3], li[4] so on. The latest will always be li[2].

# Click on the upload the questions button and upload
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div[2]/div[2]/div[2]/span[1]/label/span[1]/input").send_keys(f"C:\\Users\\aniket.gupta\\Downloads\\{input('Enter the File Name: ', )}.xlsx")
time.sleep(1)

# Click on Save The Questions
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div[2]/div[2]/div[2]/span[2]/label").click()

expecectedmsg2 = "Uploaded questions are saved"
if msg == expecectedmsg2:
    print(msg)
else:
    print(msg)
