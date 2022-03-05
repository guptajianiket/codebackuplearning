from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
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



def createpages(channel,shownum, page_name_1,page_name_2,filelocation,supagenum):

    # Select Channel
    driver.find_element(By.CSS_SELECTOR, f"input[value={channel}]").click()

    time.sleep(1)

    # Click on show list
    driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/div[1]/div/div").click()
    time.sleep(3)

    # Click on the show
    driver.find_element(By.XPATH, f"//*[@id='menu-']/div[3]/ul/li[{shownum}]").click()
    time.sleep(2)

    # Save and Next
    driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/div[3]/button").click()
    time.sleep(2)

    # Click on the menu
    driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[1]/div/div/div").click()

    # Click on the supplementary page
    driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[1]/div/div/ul/li[3]").click()
    time.sleep(3)

    # Click on add icon
    driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[3]/div/div/div/div/div[1]/div[1]/div/div[2]/button").click()
    time.sleep(1)

    # Enter the sup page name
    driver.find_element(By.XPATH, "//*[@id='standard-basic']").send_keys(page_name_1)
    time.sleep(1)

    # Click on the Add button
    driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[3]/div/div/div/div/div[1]/div[1]/div/button[1]").click()
    time.sleep(1)

    # Click on add icon
    driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[3]/div/div/div/div/div[1]/div[1]/div/div[2]/button").click()
    time.sleep(1)

    # Enter the sup page name
    driver.find_element(By.XPATH, "//*[@id='standard-basic']").send_keys(page_name_2)
    time.sleep(1)

    # Click on the Add button
    driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[3]/div/div/div/div/div[1]/div[1]/div/button[1]").click()
    time.sleep(1)

    # Click on pages section
    driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[3]/div/div/div/div/div[1]/div[1]/div/div[1]/div/div/div").click()

    # Click on the supplementary page background not user detail
    driver.find_element(By.XPATH, f"//*[@id='menu-']/div[3]/ul/li[{supagenum}]").click()

    # Click on design space
    wrapper = driver.find_element(By.XPATH, "//*[@id='uiMan']/div[1]/div[1]/div[1]/iframe")
    wrapper.click()

    # Clikc on style manager icon
    driver.find_element(By.XPATH, "//*[@id='uiMan']/div[1]/div[2]/div[3]/div/span[1]").click()

    # Click on + icon of the background
    driver.find_element(By.XPATH, "//*[@id='gjs-sm-add']").click()
    time.sleep(1)

    # Click on the Images button
    driver.find_element(By.XPATH, "//*[@id='gjs-sm-images']").click()
    time.sleep(2)

    # Uplaod the image
    driver.find_element(By.XPATH,"//*[@id='gjs-am-uploadFile']").send_keys(filelocation)
    time.sleep(3)

    # Click on save icon
    driver.find_element(By.XPATH, "//*[@id='uiMan']/div[1]/div[2]/div[2]/div/span[6]").click()

createpages("MTV",3,"existinguser","userdetail","C:\\Users\\aniket.gupta\\Desktop\\Assets=\\Assets\\Assets\\sfjsf.png",1)
