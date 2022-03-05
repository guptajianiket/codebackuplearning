from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
service = Service("C:\\Users\\aniket.gupta\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.get("https://callforentry-stage.web.app/app?channelName=colors&showName=sumiti-13th-jan-cfe-form&region=in&project=2dt1ofbpfigbjx21xp2h")
time.sleep(3)
def uplaodcamera():
    driver.find_element(By.XPATH, "//*[@id='D807C906-489F-4B0B-B2D8-88A44D62F9F4']").click()
    input("Allow Camera Permission: ", )
    driver.find_element(By.XPATH, "//*[@id='myVideo']/div[7]/button[1]").click()
    time.sleep(6)
    driver.find_element(By.XPATH, "//*[@id='myVideo']/div[7]/button[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='ok']").click()
    #ids = input("Enter the ID ", )
    #driver.find_element(By.XPATH, f"//*[@id='{ids}']").send_keys("C:\\Users\\aniket.gupta\\Downloads\\AccurateScrawnyAnkole-mobile.mp4")
    time.sleep(9)
    driver.find_element(By.XPATH, "//*[@id='submitForm']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='success']/div/a").click()
    time.sleep(2)

def uplaodcamera2():
    driver.find_element(By.XPATH, "//*[@id='D807C906-489F-4B0B-B2D8-88A44D62F9F4']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='myVideo']/div[7]/button[1]").click()
    time.sleep(6)
    driver.find_element(By.XPATH, "//*[@id='myVideo']/div[7]/button[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='ok']").click()
    #ids = input("Enter the ID ", )
    #driver.find_element(By.XPATH, f"//*[@id='{ids}']").send_keys("C:\\Users\\aniket.gupta\\Downloads\\AccurateScrawnyAnkole-mobile.mp4")
    time.sleep(9)
    driver.find_element(By.XPATH, "//*[@id='submitForm']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='success']/div/a").click()
    time.sleep(2)

for i in range(2,110):
    uplaodcamera2()
    print("Recorder & Submitted " + str(i))


