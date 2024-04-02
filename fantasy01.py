from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
startTime = time.time()
service = Service("C:\\Users\\aniket.gupta\\Desktop\\chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.implicitly_wait(6)
leagueurl = "https://fantasyapp.voot.com/kkk-12/10/kkk12/12"
token = "?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVSUQiOiJheVI3QnVLRkNhUldSb3NFcnNyc1haZ3IzQ0" \
        "9KIiwidXNlck5hbWUiOiJOZXcgVXNlciBUaHJlZSIsImxvZ2luUHJvdmlkZXIiOiJUcmFkaXRpb25hbCIsImdlbmRlc" \
        "iI6Ik0iLCJhZ2UiOiIzMS0wMy0xOTk1IiwibmFtZSI6Ik5ldyBVc2VyIFRocmVlIiwiZW1haWwiOiJuZXd1c2VyMDA0Q" \
        "HZvb3QuY29tIiwiVURJRCI6ImF5UjdCdUtGQ2FSV1Jvc0Vyc3JzWFpncjNDT0oiLCJzZXgiOiJNIiwiZXh0cmFEYXRhIjoidm" \
        "9vdCIsImlhdCI6MTY2MDY0MzU1MCwiZXhwIjoxNjkyMjAxMTUwfQ.Xbvv6QM6qi3aNYdmHYZVjNo_XXuEzD88sJIpt-szfdc"

driver.get(leagueurl+token)
driver.maximize_window()
# CHeck for coach card section
print(driver.find_element(By.XPATH,"//*[@id='wrapper']/div/app-guide/section/div/div/div[1]/div").is_displayed())

# Click on continue
driver.find_element(By.XPATH,"//*[@id='wrapper']/div/app-guide/section/div/div/div[2]/a").click()

print(driver.find_element(By.XPATH,"//*[@id='wrapper']/div/app-header/header/div/div/div[1]").get_attribute("alt"))

time.sleep(2)
# Click on league rules
driver.find_element(By.XPATH,"//*[@id='wrapper']/div/app-create-team/section[2]/div/div/div[2]/table/tbody/tr[1]/td[2]/a/span").click()

time.sleep(2)
# check for league rule page
print(driver.find_element(By.XPATH,"/html/body/modal-container/div").is_displayed())

# Close league rule page
driver.find_element(By.XPATH,"/html/body/modal-container/div/div/div[1]/img").click()

for i in range(2,7):
    # Select contestant first 5 contestants
    driver.find_element(By.XPATH,f"//*[@id='wrapper']/div/app-create-team/section[2]/div/div/div[2]/table/tbody/tr[{i}]/td[3]/div/div/a").click()

# Click on Create Team
driver.find_element(By.XPATH,"//*[@id='wrapper']/div/app-create-team/section[2]/div/div/div[3]/a").click()

time.sleep(2)

# Select 3rd contestant as captain
driver.find_element(By.XPATH,"//*[@id='wrapper']/div/app-create-team/section[2]/div/div/div[3]/table/tbody/tr[4]/td[3]/a").click()

# Click on Submit
driver.find_element(By.XPATH,"//*[@id='wrapper']/div/app-create-team/section[2]/div/div/div[4]/a[2]").click()

# Enter Team name
driver.find_element(By.XPATH,"/html/body/modal-container/div/div/div/div/form/div/input").send_keys("Test Team")

# Click on Start Playing button
driver.find_element(By.XPATH,"/html/body/modal-container/div/div/div/div/div/button").click()

# Click on Submit button
driver.find_element(By.XPATH,"/html/body/modal-container/div/div/div/div[2]/button").click()

# click on ok button of team creation confirmation pop up
driver.find_element(By.XPATH,"/html/body/modal-container[2]/div/div/div/div/div[2]/a").click()

# click on continue to my league button
driver.find_element(By.XPATH,"//*[@id='wrapper']/div/app-your-team/section/div[2]/div/div[2]/a[1]").click()

# Click on edit button from team preview page
driver.find_element(By.XPATH,"//*[@id='wrapper']/div/app-your-team/section/div[2]/div/div[2]/a[2]").click()

# click on my league
driver.find_element(By.XPATH,"//*[@id='wrapper']/div/app-header/header/div/div/div[2]/ul/li[2]/a").click()
time.sleep(2)

# close the details required pop up
driver.find_element(By.XPATH,"//*[@id='user-contact-info-popup']/button/span").click()

# click on the 1st league drop down icon
driver.find_element(By.XPATH,"//*[@id='wrapper']/div/app-my-league/section/div/div/div[2]/div/div[2]/div[1]/div[1]/div[3]/span[2]/svg/use").click()
# Go to leaderboard page
driver.find_element(By.XPATH,"//*[@id='wrapper']/div/app-header/header/div/div/div[2]/ul/li[3]/a").click()

# Go to bonus point page
driver.find_element(By.XPATH,"//*[@id='wrapper']/div/app-header/header/div/div/div[2]/ul/li[4]/a").click()

# Go to profile page
driver.find_element(By.XPATH,"//*[@id='wrapper']/div/app-header/header/div/div/div[2]/ul/li[5]/a").click()

# Go to terms and conditions
driver.find_element(By.XPATH,"//*[@id='wrapper']/app-footer/footer/div/div/div[1]/ul/li/a").click()

# click on back button of tnc page
driver.find_element(By.XPATH,"//*[@id='wrapper']/div/app-terms-and-condition/section/div[2]/div/div[2]/a").click()

# click on Voot Fantasy league icon
driver.find_element(By.XPATH,"//*[@id='wrapper']/div/app-header/header/div/div/div[1]/a").click()