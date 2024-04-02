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


# Click on Vote
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div/div[1]/div/div/ul/div[3]/div[2]").click()

# CLick on Reporting
driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div/div[2]/div[3]/p").click()
time.sleep(2)

# Click on "Mail" icon of the required show
driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/div[1]/table/tbody/tr[3]/td[2]/a[1]").click()

# Click on the episode dropdown
driver.find_element(By.XPATH,f"//*[@id='call-for-entry']/div[2]/div/div[1]/div/div/div/div[3]/table/tbody/tr[1]/td[4]/div/label/span[1]/span[1]/input").click()

# enter email address
driver.find_element(By.XPATH,"//*[@id='standard-full-width']").send_keys("aniket.gupta@rws.com")

# Click on add
driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/div/div[1]/div/div/div/div[4]/div/div/div[2]/button").click()

time.sleep(1)
# Click on submit
driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[2]/div/div[2]/div/button").click()
print(f"Report 1 sent")
time.sleep(5)

for i in range (2,34):
    # Click on the episode dropdown
    driver.find_element(By.XPATH,
                        f"//*[@id='call-for-entry']/div[2]/div/div[1]/div/div/div/div[3]/table/tbody/tr[{i}]/td[4]/div/label/span[1]/span[1]/input").click()


    time.sleep(1)
    # Click on submit
    driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div[2]/div/button").click()
    print(f"Report {i} sent")
    time.sleep(5)



# quiz theme page
    # Click on the theme page
    driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[1]/div/div/ul/li[5]").click()
    time.sleep(2)

    # click on the color icon
    #driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[5]/div/div[1]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div/div/svg/path[1]").click()
    #time.sleep(1)

    # enter the color code
    #driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[5]/div/div[1]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/input").send_keys("#0D0620")

    # click on the question text color icon
    #driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[3]/div/div/div/div/div[1]/div[1]/div/div[1]/div/div/div").click()

    # enter the color code
    #driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[5]/div/div[1]/div/div/div[2]/div[3]/div/div/div[1]/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/input").send_keys()

    # select the Font family
    driver.find_element(By.XPATH,"//*[@id='select-questionfontFamily']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//*[@id='menu-questionfontFamily']/div[3]/ul/li[1]").click()

    # select the font style
    driver.find_element(By.XPATH,"//*[@id='select-questionfontStyle']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//*[@id='menu-questionfontStyle']/div[3]/ul/li[1]").click()

    # select the font weight
    driver.find_element(By.XPATH,"//*[@id='select-questionfontWeight']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//*[@id='menu-questionfontWeight']/div[3]/ul/li[2]").click()

    # select the font size
    driver.find_element(By.XPATH,"//*[@id='select-questionfontSize']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//*[@id='menu-questionfontSize']/div[3]/ul/li[5]").click()

    # select the Answer Display
    driver.find_element(By.XPATH,
                        "//*[@id='call-for-entry']/div[5]/div/div[1]/div/div/div[2]/div[4]/div/div[1]/div[1]/div/div/div/div/div/label/label").send_keys(
        "C:\\Users\\aniket.gupta\\Desktop\\Assets=\\BBOTT-CoinDCX-Assets\\Assets\\Mobile\\default-button-mobile.png")

    driver.find_element(By.XPATH,
                        "//*[@id='call-for-entry']/div[5]/div/div[1]/div/div/div[2]/div[4]/div/div[1]/div[2]/div/div/div/div/div/label/label").send_keys(
        "C:\\Users\\aniket.gupta\\Desktop\\Assets=\\BBOTT-CoinDCX-Assets\\Assets\\Mobile\\selection-button-mobile.png")

    driver.find_element(By.XPATH,
                        "//*[@id='call-for-entry']/div[5]/div/div[1]/div/div/div[2]/div[4]/div/div[1]/div[3]/div/div/div/div/div/label/label").send_keys(
        "C:\\Users\\aniket.gupta\\Desktop\\Assets=\\BBOTT-CoinDCX-Assets\\Assets\\Mobile\\correct-button-mobile.png")
    driver.find_element(By.XPATH,
                        "//*[@id='call-for-entry']/div[5]/div/div[1]/div/div/div[2]/div[4]/div/div[1]/div[4]/div/div/div/div/div/label/label").send_keys(
        "C:\\Users\\aniket.gupta\\Desktop\\Assets=\\BBOTT-CoinDCX-Assets\\Assets\\Mobile\\wrong-button-mobile.png")

    # select the font family
    driver.find_element(By.XPATH,"//*[@id='select-optionfontFamily']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//*[@id='menu-optionfontFamily']/div[3]/ul/li[1]").click()

    # select the font style
    driver.find_element(By.XPATH,"//*[@id='select-optionfontStyle']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//*[@id='menu-optionfontStyle']/div[3]/ul/li[1]").click()

    #select the font weight
    driver.find_element(By.XPATH,"//*[@id='select-optionfontWeight']").click()
    time.sleep(1)
    driver.find_element("//*[@id='menu-optionfontWeight']/div[3]/ul/li[2]").click()

    # upload photo for submit button
    driver.find_element(By.XPATH,
                        "//*[@id='call-for-entry']/div[5]/div/div[1]/div/div/div[2]/div[6]/div/div/div[2]/div/div/div/div/div/label/label").send_keys(
        "C:\\Users\\aniket.gupta\\Desktop\\Assets=\\BBOTT-CoinDCX-Assets\\Assets\\Mobile\\submit-button-mobile.png")

    # enter submit text
    driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[5]/div/div[1]/div/div/div[2]/div[6]/div/div/div[3]/div/input").send_keys("Submit")

    # select font family
    driver.find_element(By.XPATH,"//*[@id='select-buttonfontFamily']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//*[@id='select-buttonfontFamily']/div[3]/ul/li[1]").click()

    # select the font style
    driver.find_element(By.XPATH, "//*[@id='select-buttonfontStyle']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='select-buttonfontStyle']/div[3]/ul/li[1]").click()

    # select the font weight
    driver.find_element(By.XPATH, "//*[@id='select-buttonfontWeight']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='select-buttonfontWeight']/div[3]/ul/li[2]").click()

    # select the font size
    driver.find_element(By.XPATH, "//*[@id='select-buttonfontSize']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='menu-buttonfontSize']/div[3]/ul/li[5]").click()

    # select the save button
    driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[4]/div[1]/div/button").click()






    # CLICK ON WEB





    driver.find_element(By.XPATH,"//*[@id='call-for-entry']/div[5]/div/div[1]/div/div/div[1]/div/div/div/button[1]").click()

    # click on the color icon
    #driver.find_element(By.XPATH,
                        #"//*[@id='call-for-entry']/div[5]/div/div[1]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div/div/svg").click()
    #time.sleep(1)

    # enter the color code
    #driver.find_element(By.XPATH,
                        #"//*[@id='call-for-entry']/div[5]/div/div[1]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/input").send_keys(
        #"#0D0620")

    # click on the question text color icon
    #driver.find_element(By.XPATH,
                        #"//*[@id='call-for-entry']/div[3]/div/div/div/div/div[1]/div[1]/div/div[1]/div/div/div").click()

    # enter the color code
    #driver.find_element(By.XPATH,
                        #"//*[@id='call-for-entry']/div[5]/div/div[1]/div/div/div[2]/div[3]/div/div/div[1]/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/input").send_keys()

    # select the Font family
    driver.find_element(By.XPATH, "//*[@id='select-questionfontFamily']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='menu-questionfontFamily']/div[3]/ul/li[1]").click()

    # select the font style
    driver.find_element(By.XPATH, "//*[@id='select-questionfontStyle']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='menu-questionfontStyle']/div[3]/ul/li[1]").click()

    # select the font weight
    driver.find_element(By.XPATH, "//*[@id='select-questionfontWeight']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='menu-questionfontWeight']/div[3]/ul/li[2]").click()

    # select the font size
    driver.find_element(By.XPATH, "//*[@id='select-questionfontSize']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='menu-questionfontSize']/div[3]/ul/li[5]").click()

    # select the Answer Display
    driver.find_element(By.XPATH,
                        "//*[@id='call-for-entry']/div[5]/div/div[1]/div/div/div[2]/div[4]/div/div[1]/div[1]/div/div/div/div/div/label/label").send_keys(
        "C:\\Users\\aniket.gupta\\Desktop\\Assets=\\BBOTT-CoinDCX-Assets\\Assets\\Web\\default-button-web.png")

    driver.find_element(By.XPATH,
                        "//*[@id='call-for-entry']/div[5]/div/div[1]/div/div/div[2]/div[4]/div/div[1]/div[2]/div/div/div/div/div/label/label").send_keys(
        "C:\\Users\\aniket.gupta\\Desktop\\Assets=\\BBOTT-CoinDCX-Assets\\Assets\\Web\\selection-button-web.png")

    driver.find_element(By.XPATH,
                        "//*[@id='call-for-entry']/div[5]/div/div[1]/div/div/div[2]/div[4]/div/div[1]/div[3]/div/div/div/div/div/label/label").send_keys(
        "C:\\Users\\aniket.gupta\\Desktop\\Assets=\\BBOTT-CoinDCX-Assets\\Assets\\Web\\correct-button-web.png")
    driver.find_element(By.XPATH,
                        "//*[@id='call-for-entry']/div[5]/div/div[1]/div/div/div[2]/div[4]/div/div[1]/div[4]/div/div/div/div/div/label/label").send_keys(
        "C:\\Users\\aniket.gupta\\Desktop\\Assets=\\BBOTT-CoinDCX-Assets\\Assets\\Web\\wrong-button-web.png")

    # select the font family
    driver.find_element(By.XPATH, "//*[@id='select-optionfontFamily']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='menu-optionfontFamily']/div[3]/ul/li[1]").click()

    # select the font style
    driver.find_element(By.XPATH, "//*[@id='select-optionfontStyle']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='menu-optionfontStyle']/div[3]/ul/li[1]").click()

    # select the font weight
    driver.find_element(By.XPATH, "//*[@id='select-optionfontWeight']").click()
    time.sleep(1)
    driver.find_element("//*[@id='menu-optionfontWeight']/div[3]/ul/li[2]").click()

    # upload photo for submit button
    driver.find_element(By.XPATH,
                        "//*[@id='call-for-entry']/div[5]/div/div[1]/div/div/div[2]/div[6]/div/div/div[2]/div/div/div/div/div/label/label").send_keys(
        "C:\\Users\\aniket.gupta\\Desktop\\Assets=\\BBOTT-CoinDCX-Assets\\Assets\\Web\\submit-button-web.png")

    # enter submit text
    driver.find_element(By.XPATH,
                        "//*[@id='call-for-entry']/div[5]/div/div[1]/div/div/div[2]/div[6]/div/div/div[3]/div/input").send_keys(
        "Submit")

    # select font family
    driver.find_element(By.XPATH, "//*[@id='select-buttonfontFamily']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='select-buttonfontFamily']/div[3]/ul/li[1]").click()

    # select the font style
    driver.find_element(By.XPATH, "//*[@id='select-buttonfontStyle']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='select-buttonfontStyle']/div[3]/ul/li[1]").click()

    # select the font weight
    driver.find_element(By.XPATH, "//*[@id='select-buttonfontWeight']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='select-buttonfontWeight']/div[3]/ul/li[2]").click()

    # select the font size
    driver.find_element(By.XPATH, "//*[@id='select-buttonfontSize']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='menu-buttonfontSize']/div[3]/ul/li[5]").click()

    # select the Save button
    driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[4]/div[1]/div/button").click()