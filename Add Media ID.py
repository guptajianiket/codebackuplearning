from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
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
# click on the quiz
driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div/div[1]/div/div/ul/div[2]/div[2]").click()
time.sleep(0.5)
# click on quiz management
driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div/div[2]/div[4]").click()
# click on show drop down
driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/div/div/div/div/div/div/div").click()
time.sleep(0.5)
# click on the first show
driver.find_element(By.XPATH,"//*[@id='menu-']/div[3]/ul/li[2]").click()
# click on publish interactivity icon
driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/div[2]/div/table/tbody/tr[1]/td[4]/button[3]").click()

import openpyxl
vk1 = openpyxl.load_workbook("C:\\Users\\aniket.gupta\\Downloads\\k1223.xlsx")
sh1 = vk1.active
medialist = []
for cell in sh1['A']:
    medialist.append(cell.value)

for i in range (1,18):

    mediaid = medialist[i-1]

    # enter media id
    driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div[1]/div"
                                  "/div/div[1]/div[1]/div/div/div/div/input").send_keys(mediaid)

    # click on Add
    driver.find_element(By.XPATH,
                        "//*[@id='call-for-entry']/div[2]/div/div[1]/div/div/div[1]/div[1]/div/div/label").click()

    # check whether the media id is new or existing
    l1 = input("Enter 1 if want to add in db else enter 0: ")

    # if media id is not present in DB
    if l1 == 1:
        # click on Yes for adding media id
        driver.find_element(By.XPATH,
                            "//*[@id='call-for-entry']/div[2]/div/div[1]/div/div/div[1]/div[2]/div/label[1]").click()
        # enter media id
        driver.find_element(By.XPATH,
                            "//*[@id='call-for-entry']/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[1]").send_keys(
            mediaid)
        # enter seasion id
        driver.find_element(By.XPATH,
                            "//*[@id='call-for-entry']/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div").send_keys(
            mediaid)
        # click on add media
        driver.find_element(By.XPATH,
                            "//*[@id='call-for-entry']/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/label/span[2]").click()

        time.sleep(2)
        # enter media id
        driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div[1]/div"
                                      "/div/div[1]/div[1]/div/div/div/div/input").send_keys(mediaid)

        # click on Add
        driver.find_element(By.XPATH,
                            "//*[@id='call-for-entry']/div[2]/div/div[1]/div/div/div[1]/div[1]/div/div/label").click()

    else:
        print("The media id is present")
        pass

    # enter web image
    driver.find_element(By.XPATH,
                        "//*[@id='call-for-entry']/div[2]/div/div[1]/div/div/div[5]/div[1]/div/div/label/label").send_keys(
        "C:\\Users\\aniket.gupta\\Desktop\\icon_interactivity_quiz.png")
    time.sleep(3)
    # enter mobile image
    driver.find_element(By.XPATH,
                        "//*[@id='call-for-entry']/div[2]/div/div[1]/div/div/div[5]/div[2]/div/div/label/label").send_keys(
        "C:\\Users\\aniket.gupta\\Desktop\\icon_interactivity_quiz.png")

    time.sleep(3)
    # click on publish
    driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div[1]/div/div/div[6]/div/button").click()

    driver.refresh()







