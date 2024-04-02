from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
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
print("Logged in IMS")

# Click on Quiz
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div/div[1]/div/div/ul/div[2]/div[2]").click()

# Click on Reporting
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div/div[2]/div[3]/p").click()
time.sleep(3)

# Click on show list
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/div[1]/div/div").click()
time.sleep(3)

# Click on the show
driver.find_element(By.XPATH, "//*[@id='menu-']/div[3]/ul/li[21]").click()
time.sleep(2)

# Click on the select report
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/div[2]/div/div/div").click()
time.sleep(2)

# Click on the detailed report
driver.find_element(By.XPATH,"//*[@id='menu-']/div[3]/ul/li[3]").click()
time.sleep(2)

# select lineup , enter email address and send report.

def customreportsend(endepisodenumber,text1,text2,text3,text4):
    for i in range(2, endepisodenumber):
        # Click on the select Line up
        driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/div[3]/div/div/div/div").click()
        time.sleep(2)

        # Select Episode
        lineuptext = driver.find_element(By.XPATH, f"//*[@id='menu-']/div[3]/ul/li[{i}]").text

        if lineuptext == text1 and text2 and text3 and text4:
            driver.find_element(By.XPATH, f"//*[@id='menu-']/div[3]/ul/li[{i}]").click()
        else:
            driver.find_element(By.XPATH, f"//*[@id='menu-']/div[3]/ul/li[{i}]").click()
            # Enter email address
            driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/input").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/input").send_keys(
                "aniket.gupta@rws.com")
            driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/input").send_keys(
                Keys.ENTER)
            time.sleep(2)

            # Click on send reports
            driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/button").click()
            print(f"Episode {i} report sent")
            time.sleep(180)


def reportsend(endepisodenumber):
    for i in range(2, endepisodenumber):
        # Click on the select Line up
        driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/div[3]/div/div/div/div").click()
        time.sleep(2)

        # Select Episode
        driver.find_element(By.XPATH, f"//*[@id='menu-']/div[3]/ul/li[{i}]").click()
        # Enter email address
        driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/input").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/input").send_keys(
            "aniket.gupta@rws.com")
        driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/input").send_keys(
            Keys.ENTER)
        time.sleep(2)

        # Click on send reports
        driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/button").click()
        print(f"Episode {i} report sent")
        time.sleep(30)

reportsend(30)


print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))


