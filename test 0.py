
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
startTime = time.time()
service = Service("C:\\Users\\aniket.gupta\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.get("https://callforentry-stage.web.app/app?channelName=colors&showName=sumiti-13th-jan-cfe-form&region=in&project=2dt1ofbpfigbjx21xp2h")
time.sleep(3)
def upload():
    driver.find_element(By.XPATH, "//*[@id='10BA075B-5D15-46DE-8A24-5325B329B88E']").send_keys(
        "C:\\Users\\aniket.gupta\\Downloads\\big_buck_bunny_720p_1mb.mp4")
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//*[@id='26D964A3-686A-4935-AD8C-6F44FD2A955C']").send_keys(
        "C:\\Users\\aniket.gupta\\Downloads\\backwinner.PNG")
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//*[@id='158B6E93-EA97-4E80-AFF6-49633C2ADFCC']").send_keys(
        "C:\\Users\\aniket.gupta\\Downloads\\Aniket-test-OyGmu4LoWEycaGUN8DNOew.zip")
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//*[@id='6C8CD744-278A-4D12-BEBC-BDA9F39F4813']").send_keys(
        "C:\\Users\\aniket.gupta\\Downloads\\file_example_MP3_700KB.mp3")
    time.sleep(11)
    driver.find_element(By.XPATH, "//*[@id='submitForm']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='success']/div/a").click()

#ids2 = input("Enter the ID again ", )
def upcmt():
    driver.find_element(By.XPATH, "//*[@id='D807C906-489F-4B0B-B2D8-88A44D62F9F4']").click()
    time.sleep(2)
    #driver.find_element(By.XPATH, f"//*[@id='{ids2}']").send_keys("C:\\Users\\aniket.gupta\\Downloads\\AccurateScrawnyAnkole-mobile.mp4")
    driver.find_element(By.NAME, "camera_input_1001EE39-878D-4B6D-BAC6-5B39DEC39BB3").send_keys("C:\\Users\\aniket.gupta\\Downloads\\AccurateScrawnyAnkole-mobile.mp4")
    time.sleep(7)
    driver.find_element(By.XPATH, "//*[@id='submitForm']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='success']/div/a").click()
    time.sleep(2)

for i in range (1,112):
    upcmt()
    print("Uploaded and Submitted "+str(i))