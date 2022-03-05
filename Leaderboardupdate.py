from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
startTime = time.time()
service = Service("C:\\Users\\aniket.gupta\\Desktop\\chromedriver_win32 (1)\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.get("https://quiz.voot.com/leaderboard/3c0ba220-2e66-11ec-827d-c30720bd7756-1ab")
U1 = driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div/div/div[1]/div[2]/h3").text
U2 = driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div/div/div[2]/div[2]/h3").text
U3 = driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div/div/div[3]/div[2]/h3").text
U4 = driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div/div/div[4]/div[2]/h3").text
U5 = driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div/div/div[5]/div[2]/h3").text
U6 = driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div/div/div[6]/div[2]/h3").text
U7 = driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div/div/div[7]/div[2]/h3").text
U8 = driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div/div/div[8]/div[2]/h3").text
U9 = driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div/div/div[9]/div[2]/h3").text
U10 = driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div/div/div[10]/div[2]/h3").text
S1 = driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div/div/div[1]/div[3]").text
S2 = driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div/div/div[2]/div[3]").text
S3 = driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div/div/div[3]/div[3]").text
S4 = driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div/div/div[4]/div[3]").text
S5 = driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div/div/div[5]/div[3]").text
S6 = driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div/div/div[6]/div[3]").text
S7 = driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div/div/div[7]/div[3]").text
S8 = driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div/div/div[8]/div[3]").text
S9 = driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div/div/div[9]/div[3]").text
S10 = driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div/div/div[10]/div[3]").text

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

# Select Channel
driver.find_element(By.CSS_SELECTOR, "input[value=Colors]").click()

time.sleep(1)

# Click on show list
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/div[1]/div/div").click()
time.sleep(3)

# Click on the show
driver.find_element(By.XPATH, "//*[@id='menu-']/div[3]/ul/li[7]").click()


time.sleep(2)

# Save and Next
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/div[3]/button").click()
time.sleep(2)

# Locating the text columns:
driver.switch_to.frame(0)
UN1 = driver.find_element(By.XPATH, "//*[@id='i0sli']")
US1 = driver.find_element(By.XPATH, "//*[@id='ik368']")
UN2 = driver.find_element(By.XPATH, "//*[@id='if8vd']")
US2 = driver.find_element(By.XPATH, "//*[@id='it3yc']")
UN3 = driver.find_element(By.XPATH, "//*[@id='iqv2k']")
US3 = driver.find_element(By.XPATH, "//*[@id='ifqlb']")
UN4 = driver.find_element(By.XPATH, "//*[@id='ihxlv']")
US4 = driver.find_element(By.XPATH, "//*[@id='iwzr2']")
UN5 = driver.find_element(By.XPATH, "//*[@id='ihbi4']")
US5 = driver.find_element(By.XPATH, "//*[@id='iozi0y']")
UN6 = driver.find_element(By.XPATH, "//*[@id='ij0vl']")
US6 = driver.find_element(By.XPATH, "//*[@id='icxh9j']")
UN7 = driver.find_element(By.XPATH, "//*[@id='il3za']")
US7 = driver.find_element(By.XPATH, "//*[@id='ixwnj2']")
UN8 = driver.find_element(By.XPATH, "//*[@id='ih6y9']")
US8 = driver.find_element(By.XPATH, "//*[@id='ir3t35']")
UN9 = driver.find_element(By.XPATH, "//*[@id='iko6x']")
US9 = driver.find_element(By.XPATH, "//*[@id='in8yrc']")
UN10 = driver.find_element(By.XPATH, "//*[@id='is1b5']")
US10 = driver.find_element(By.XPATH, "//*[@id='ipx4c8']")

action = ActionChains(driver)

# Clear and enter text
action.double_click(UN1).perform()
UN1.clear()
UN1.send_keys(U1)

def updatenamescore(name,nametext,score,scoretext):
    action.double_click(name).perform()
    name.clear()
    name.send_keys(nametext)
    action.double_click(score).perform()
    score.clear()
    score.send_keys(scoretext)


updatenamescore(UN1,U1,US1,S1)
updatenamescore(UN2,U2,US2,S2)
updatenamescore(UN3,U3,US3,S3)

driver.switch_to.parent_frame()
# Since the page needs to be scrolled down
# click on Open Layer Manager icon
driver.find_element(By.XPATH, "//*[@id='uiMan']/div[1]/div[2]/div[3]/div/span[3]").click()
time.sleep(2)

# Click on the body drop down icon
#driver.find_element(By.XPATH, "//*[@id='uiMan']/div[1]/div[2]/div[5]/div[3]/div/div[1]/div/div/i").click()

# Click on container drop down
driver.find_element(By.XPATH,"//*[@id='uiMan']/div[1]/div[2]/div[5]/div[3]/div/div[3]/div/div/div[1]/div/div/i").click()
time.sleep(2)

# Click on 10th box to scroll down
driver.find_element(By.XPATH, "//*[@id='uiMan']/div[1]/div[2]/div[5]/div[3]/div/div[3]/div/div/div[4]/div/div[14]/div[1]/div/div/span").click()


driver.switch_to.frame(0)
time.sleep(2)
updatenamescore(UN4,U4,US4,S4)
updatenamescore(UN5,U5,US5,S5)
updatenamescore(UN6,U6,US6,S6)
updatenamescore(UN7,U7,US7,S7)
updatenamescore(UN8,U8,US8,S8)
updatenamescore(UN9,U9,US9,S9)
updatenamescore(UN10,U10,US10,S10)

driver.switch_to.parent_frame()
time.sleep(1)

input("Check the data before update: ", )
# Click on save
driver.find_element(By.XPATH, "//*[@id='uiMan']/div[1]/div[2]/div[2]/div/span[6]").click()

# Get the action message
message = driver.find_element(By.XPATH, "/html/body/div[3]").text
print(message)
if message == "Data Failed to Save. Please try again.":
    driver.save_screenshot("Failure_SS.png")
if message == "Data Saved Successfully!!!":
    driver.get("https://www.voot.com/shows/the-big-picture/309295")
    Alert(driver).accept()
    time.sleep(3)
    # Click on the leaders banner
    driver.find_element(By.PARTIAL_LINK_TEXT, "View Now").click()
    time.sleep(2)
    driver.find_elements(By.XPATH, "//*[@id='HybridRailId']/div[2]/div/div/div/div/div/a/div/div[2]/div/button")[2].click()
    time.sleep(2)
    # Log in Page appeared
    # Click on the mobile number
    driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div[3]/div[3]/p").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='mobile number']").click()
    driver.find_element(By.XPATH, "//*[@id='mobile number']").send_keys("7987142067")
    driver.find_element(By.XPATH, "//html/body/div[2]/div[2]/div/div/div[2]/div[2]/button").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='enter password']").click()
    driver.find_element(By.XPATH, "//*[@id='enter password']").send_keys("h@rrold95")
    driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div[2]/div[2]/button").click()
    time.sleep(5)
    header = driver.find_element(By.XPATH,"//*[@id='ifrd']").is_displayed()
    if header == True:
        driver.save_screenshot('Live_FE_SS.png')
        Element = driver.find_element(By.XPATH,"//*[@id='multi-url-link']")
        driver.execute_script("arguments[0].scrollIntoView();", Element)
        time.sleep(2)
        driver.save_screenshot('Live_FE_SS_2.png')
    else:
        print("Tale manual SS. The page didn't appeared")

else:
    print("Script didn't executed successfully, please check it manually")







