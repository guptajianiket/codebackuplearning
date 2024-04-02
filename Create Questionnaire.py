from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
startTime = time.time()
service = Service("C:\\Users\\aniket.gupta\\Desktop\\chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.implicitly_wait(10)
driver.get("https://moraviait-my.sharepoint.com/:x:/r/personal/anigupta_moravia_com/_layouts/15/Doc.aspx?sou"
           "rcedoc=%7BB6B9168E-48E8-4915-8619-EE0C506D8A91%7D&file=Diwali%20Dhamaka.xlsx&action=d"
           "efault&mobileredirect=true")

time.sleep(1)

# enter email address
driver.find_element(By.XPATH,"//*[@id='i0116']").send_keys("Anigupta@moravia.com")

driver.find_element(By.XPATH,"//*[@id='idSIButton9']").click()
time.sleep(2)

# enter password
driver.find_element(By.XPATH,"//*[@id='i0118']").send_keys("Jholameansbag@95")
time.sleep(0.5)
driver.find_element(By.XPATH,"//*[@id='idSIButton9']").click()
time.sleep(0.5)

# click on no
driver.find_element(By.XPATH,"//*[@id='idBtn_Back']").click()
time.sleep(2)

# enter question:
driver.find_element(By.XPATH,"//*[@id='m_excelWebRenderer_ewaCtl_sheetContentDiv']/div[4]").send_Keys("Who are Ash, Iris and Cilan in this movie?")

