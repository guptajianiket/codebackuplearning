import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Specify the URL of the webpage to crawl
url = "https://fasb-live.prd.faf.us.com/Page/PageContent?PageId=/news-media/inthenews.html#filterByYear_2021"

# Specify the path to the ChromeDriver executable
chrome_driver_path = "C:\\Users\\aniket.gupta\\Desktop\\chromedriver.exe"

# Initialize Chrome WebDriver with the specified path
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)
driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//*[@id='__next]/div/div/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[1]/a")
driver.find_element(By.XPATH,"//*[@id='__next']/div/div/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]")

for i in range (1,26):
    try:
         = driver.find_element(By.XPATH, f"//*[@id='__next]/div/div/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[{i}]/td[1]/a").text
        NewdDate = driver.find_element(By.XPATH, f"//*[@id='__next]/div/div/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[{i}]/td[2]/a").text

    except NoSuchElementException:
        print(f"Unable to find element {i}")
    else:



