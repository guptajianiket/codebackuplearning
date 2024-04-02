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
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div/div[1]/div/div/ul/div[3]/div[2]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div/div[2]/div[2]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/div[1]/table/tbody/tr[1]/td[3]/a[1]").click()
time.sleep(2)
Contestanr_1 = driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div/label").text
time.sleep(0.5)
Contestanr_2 = driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div/label").text
time.sleep(0.5)
Contestanr_3 = driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/div/div[2]/div/div/div[2]/div[3]/div/div/label").text
time.sleep(0.5)
Contestanr_4 = driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/div/div[2]/div/div/div[2]/div[4]/div/div/label").text
time.sleep(0.5)
Contestanr_5 = driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/div/div[2]/div/div/div[2]/div[5]/div/div/label").text
time.sleep(0.5)
Contestanr_6 = driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/div/div[2]/div/div/div[2]/div[6]/div/div/label").text
time.sleep(0.5)
Contestanr_7 = driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/div/div[2]/div/div/div[2]/div[7]/div/div/label").text
time.sleep(0.5)
Contestanr_8 = driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/div/div[2]/div/div/div[2]/div[8]/div/div/label").text
time.sleep(0.5)
Contestanr_9 = driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/div/div[2]/div/div/div[2]/div[9]/div/div/label").text
time.sleep(0.5)
Contestanr_10 = driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/div/div[2]/div/div/div[2]/div[10]/div/div/label").text
time.sleep(0.5)
Contestanr_11 = driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/div/div[2]/div/div/div[2]/div[11]/div/div/label").text
time.sleep(0.5)
Contestanr_12 = driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/div/div[2]/div/div/div[2]/div[12]/div/div/label").text
time.sleep(0.5)
Contestanr_13 = driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/div/div[2]/div/div/div[2]/div[13]/div/div/label").text
time.sleep(0.5)
Contestanr_14 = driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/div/div[2]/div/div/div[2]/div[14]/div/div/label").text
time.sleep(0.5)
Contestanr_15 = driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/div/div[2]/div/div/div[2]/div[15]/div/div/label").text
time.sleep(0.5)
Contestanr_16 = driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/div/div[2]/div/div/div[2]/div[16]/div/div/label").text
time.sleep(0.5)
driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[1]/header/div/div/div[1]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div/div[2]/div[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/table/tbody/tr[1]/td[6]/button[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='next-button']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='panel1d-content']/div/div/div/div/div[2]/div[2]/div[2]/span[4]/div/div/div[1]/div/div/div[1]").click()
time.sleep(0.5)
def entername():
    driver.find_element(By.XPATH,
                        "//*[@id='panel1d-content']/div/div/div/div/div[2]/div[2]/div[1]/div/div[5]/ul/li[2]/div/div[1]/input").send_keys(
        Contestanr_1)
    time.sleep(0.5)
    driver.find_element(By.XPATH,
                        "//*[@id='panel1d-content']/div/div/div/div/div[2]/div[2]/div[1]/div/div[5]/ul/li[3]/div/div[1]/input").send_keys(
        Contestanr_2)
    time.sleep(0.5)
    driver.find_element(By.XPATH,
                        "//*[@id='panel1d-content']/div/div/div/div/div[2]/div[2]/div[1]/div/div[5]/ul/li[4]/div/div[1]/input").send_keys(
        Contestanr_3)
    time.sleep(0.5)
    driver.find_element(By.XPATH,
                        "//*[@id='panel1d-content']/div/div/div/div/div[2]/div[2]/div[1]/div/div[5]/ul/li[5]/div/div[1]/input").send_keys(
        Contestanr_4)
    time.sleep(0.5)
    driver.find_element(By.XPATH,
                        "//*[@id='panel1d-content']/div/div/div/div/div[2]/div[2]/div[1]/div/div[5]/ul/li[6]/div/div[1]/input").send_keys(
        Contestanr_5)
    time.sleep(0.5)
    driver.find_element(By.XPATH,
                        "//*[@id='panel1d-content']/div/div/div/div/div[2]/div[2]/div[1]/div/div[5]/ul/li[7]/div/div[1]/input").send_keys(
        Contestanr_6)
    time.sleep(0.5)
    driver.find_element(By.XPATH,
                        "//*[@id='panel1d-content']/div/div/div/div/div[2]/div[2]/div[1]/div/div[5]/ul/li[8]/div/div[1]/input").send_keys(
        Contestanr_7)
    time.sleep(0.5)
    driver.find_element(By.XPATH,
                        "//*[@id='panel1d-content']/div/div/div/div/div[2]/div[2]/div[1]/div/div[5]/ul/li[9]/div/div[1]/input").send_keys(
        Contestanr_8)
    time.sleep(0.5)
    driver.find_element(By.XPATH,
                        "//*[@id='panel1d-content']/div/div/div/div/div[2]/div[2]/div[1]/div/div[5]/ul/li[10]/div/div[1]/input").send_keys(
        Contestanr_9)
    time.sleep(0.5)
    driver.find_element(By.XPATH,
                        "//*[@id='panel1d-content']/div/div/div/div/div[2]/div[2]/div[1]/div/div[5]/ul/li[11]/div/div[1]/input").send_keys(
        Contestanr_10)
    time.sleep(0.5)
    driver.find_element(By.XPATH,
                        "//*[@id='panel1d-content']/div/div/div/div/div[2]/div[2]/div[1]/div/div[5]/ul/li[12]/div/div[1]/input").send_keys(
        Contestanr_11)
    time.sleep(0.5)
    driver.find_element(By.XPATH,
                        "//*[@id='panel1d-content']/div/div/div/div/div[2]/div[2]/div[1]/div/div[5]/ul/li[13]/div/div[1]/input").send_keys(
        Contestanr_12)
    time.sleep(0.5)
    driver.find_element(By.XPATH,
                        "//*[@id='panel1d-content']/div/div/div/div/div[2]/div[2]/div[1]/div/div[5]/ul/li[14]/div/div[1]/input").send_keys(
        Contestanr_13)
    time.sleep(0.5)
    driver.find_element(By.XPATH,
                        "//*[@id='panel1d-content']/div/div/div/div/div[2]/div[2]/div[1]/div/div[5]/ul/li[15]/div/div[1]/input").send_keys(
        Contestanr_14)
    time.sleep(0.5)
    driver.find_element(By.XPATH,
                        "//*[@id='panel1d-content']/div/div/div/div/div[2]/div[2]/div[1]/div/div[5]/ul/li[16]/div/div[1]/input").send_keys(
        Contestanr_15)
    time.sleep(0.5)
    driver.find_element(By.XPATH,
                        "//*[@id='panel1d-content']/div/div/div/div/div[2]/div[2]/div[1]/div/div[5]/ul/li[17]/div/div[1]/input").send_keys(
        Contestanr_16)
    time.sleep(0.5)

entername()
driver.find_element(By.XPATH,"//*[@id='panel1d-content']/div/div/div/div/div[2]/div[1]/button[2]").click()

