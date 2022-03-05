from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import allure
startTime = time.time()
service = Service("C:\\Users\\aniket.gupta\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.implicitly_wait(10)
driver.get("https://www.pcf.org/")
time.sleep(2)

@allure.severity(allure.severity_level.CRITICAL)
def testcase01():
    # check the logo is appearing or not
    pop_up = driver.find_element(By.CLASS_NAME, "modal-body").is_displayed()
    time.sleep(5)
    if pop_up == True:
        print("testcase01 Passed")
        assert True
    else:
        driver.save_screenshot("Testcase01 error")
        print("testcase01 Failed")
        assert False


@allure.severity(allure.severity_level.MINOR)
def testcase02():
    # close the pop up
    driver.find_element(By.XPATH, "//*[@id='pcf-interstitial-model-1']/button").click()
    # check the pcf logo
    pcf_logo = driver.find_element(By.XPATH, "//*[@id='pcf-6']/img").is_displayed()
    time.sleep(2)
    if pcf_logo is True:
        print("testcase02 Passed")
        assert True
    else:
        driver.save_screenshot("testcase02 error")
        print("testcase02 Failed")
        assert False


@allure.severity(allure.severity_level.MINOR)
def testcase03():
    # To check the header drop down
    # click on the about prostate cancer
    driver.find_element(By.XPATH, "//*[@id='pcf-11']").click()
    time.sleep(2)
    # check the pop up of about prostate cancer
    apcdrop_down = driver.find_element(By.XPATH, "//*[@id='menu-item-24292']/div").is_displayed()
    if apcdrop_down == True:
        print("testcase03 Passed")
        assert True
    else:
        print("testcase03 Failed")
        assert False


@allure.severity(allure.severity_level.MINOR)
def testcase04():
    # check the pop up of patient resource
    # Click on the patient reousrce
    driver.find_element(By.XPATH, "//*[@id='pcf-57']").click()
    time.sleep(2)
    pr_popup = driver.find_element(By.XPATH, "//*[@id='menu-item-24452']/div").is_displayed()
    if pr_popup is True:
        print("testcase04 Passed")
        assert True
    else:
        print("testcase04 Failed")
        assert False


@allure.severity(allure.severity_level.MINOR)
def testcase05():
    # check the pop up of News
    # Click on the News
    driver.find_element(By.XPATH, "//*[@id='pcf-91']").click()
    time.sleep(2)
    news_popup = driver.find_element(By.XPATH, "//*[@id='menu-item-24108']/div").is_displayed()
    if news_popup is True:
        print("testcfase05 Passed")
        assert True
    else:
        print("testcase05 Failed")
        assert False


@allure.severity(allure.severity_level.MINOR)
def testcase06():
    # check the pop of science & impact
    # Click on the science & impact

    driver.find_element(By.XPATH, "//*[@id='pcf-98']").click()
    time.sleep(2)
    si_popup = driver.find_element(By.XPATH, "//*[@id='menu-item-24401']/div").is_displayed()
    if si_popup is True:
        print("testcase06 Passed")
        assert True
    else:
        print("testcase06 Failed")
        assert False


@allure.severity(allure.severity_level.MINOR)
def testcase07():
    # check the pop of Take Action
    # click on the Take & Action

    driver.find_element(By.XPATH, "//*[@id='pcf-123']").click()
    time.sleep(2)
    TA_popup = driver.find_element(By.XPATH, "//*[@id='menu-item-24489']/div").is_displayed()
    if TA_popup is True:
        print("testcase07 Passed")
        assert True
    else:
        print("testcase07 Failed")
        assert False


@allure.severity(allure.severity_level.MINOR)
def testcase08():
    # check the pop of About Us
    # click on the About Us

    driver.find_element(By.XPATH, "//*[@id='pcf-143']").click()
    time.sleep(2)
    Aboutus_popup = driver.find_element(By.XPATH, "//*[@id='menu-item-36872']/div").is_displayed()
    if Aboutus_popup is True:
        print("testcase08 Passed")
        assert True
    else:
        print("testcase08 Failed")
        assert False


@allure.severity(allure.severity_level.MINOR)
def testcase09():
    # check the privacy policy pop up
    pp_popup = driver.find_element(By.XPATH, "//*[@id='mm-0']/div/div").is_displayed()
    time.sleep(2)
    if pp_popup is True:
        print("testcase09 Passed")
        assert True
    else:
        print("testcase09 Failed")
        assert False


@allure.severity(allure.severity_level.BLOCKER)
def testcase10():
    # check the Top Donate button
    top_donate = driver.find_element(By.XPATH, "//*[@id='pcf-8']").is_displayed()
    time.sleep(2)
    if top_donate is True:
        print("testcase10 Passed")
        assert True
    else:
        print("testcase10 Failed")
        assert False


@allure.severity(allure.severity_level.BLOCKER)
def testcase11():
    # Check the Fundraiser Button
    fund_button = driver.find_element(By.XPATH, "//*[@id='pcf-9']").is_displayed()
    time.sleep(2)
    if fund_button is True:
        print("testcase11 Passed")
        assert True
    else:
        print("testcase11 Failed")
        assert False


@allure.severity(allure.severity_level.BLOCKER)
def testcase12():
    # check the choose donation amount page
    cda_section = driver.find_element(By.XPATH, "//*[@id='donation-module']/div/div/div/div[2]/div").is_displayed()
    time.sleep(2)
    if cda_section is True:
        print("testcase12  Passed")
        assert True
    else:
        print("testcase12 Failed")
        assert False


@allure.severity(allure.severity_level.BLOCKER)
def testcase13():
    # check the Accelerating Cures for all Families donate button
    acfd_section = driver.find_element(By.XPATH, "//*[@id='pcf-346']").is_displayed()
    time.sleep(2)
    if acfd_section is True:
        print("testcase13 Passed")
        assert True
    else:
        print("testcase13 Passed")
        assert False


@allure.severity(allure.severity_level.BLOCKER)
def testcase14():
    # check the bottom page donate button
    bp_button = driver.find_element(By.XPATH, "//*[@id='pcf-359']").is_displayed()
    time.sleep(2)
    if bp_button is True:
        print("testcase14 Passed")
        assert True
    else:
        print("testcase14 Failed")
        assert False


@allure.severity(allure.severity_level.MINOR)
def testcase15():
    # check the reCaptcha icon
    reC_section = driver.find_element(By.CLASS_NAME, "grecaptcha-badge").is_displayed()
    time.sleep(2)
    if reC_section is True:
        print("testcase15 Passed")
        assert True
    else:
        print("testcase15 Failed")
        assert False

@allure.severity(allure.severity_level.CRITICAL)
def testcase16():
    # Click on the "A Legacy Of Membership"
    driver.find_element(By.LINK_TEXT, "A Legacy of Leadership").click()
    time.sleep(2)
    # check the PCF Timeline heading
    timeline_text = driver.find_element(By.CLASS_NAME, "dropdown-toggle").is_displayed()
    if timeline_text is True:
        print("testcase16 Passed")
        assert True
    else:
        print("testcase16 Failed")
        assert False

@allure.severity(allure.severity_level.MINOR)
def testcase17():
    # check the first milestone
    fms_section = driver.find_element(By.XPATH, "//*[@id='1972-the-beginning-of-a-lifelong-search-for-medical-solutions']").is_displayed()
    if fms_section is True:
        print("testcase17 Passed")
        assert True
    else:
        print("testcase17 Failed")
        assert False

@allure.severity(allure.severity_level.MINOR)
def testcase18():
    # check the second milestone
    sms_section = driver.find_element(By.XPATH, "//*[@id='1976-cancer-strikes-the-family-again']").is_displayed()
    if sms_section is True:
        print("testcase18 Passed")
        assert True
    else:
        print("testcase18 Failed")
        assert False

@allure.severity(allure.severity_level.MINOR)
def testcase19():
    # chekc the the third milestone
    tms_section = driver.find_element(By.XPATH, "//*[@id='january-1982-the-milken-family-foundation-mff']").is_displayed()
    if tms_section is True:
        print("testcase19 Passed")
        assert True
    else:
        print("testcase19 Failed")
        assert False

@allure.severity(allure.severity_level.MINOR)
def testcase20():
    # chekc the the fourth milestone
    fms_section = driver.find_element(By.XPATH, "//*[@id='january-1993-those-three-words']").is_displayed()
    if fms_section is True:
        print("testcase20 Passed")
        assert True
    else:
        print("testcase20 Failed")
        assert False

@allure.severity(allure.severity_level.MINOR)
def testcase21():
    # chekc the the fifth milestone
    fims_section = driver.find_element(By.XPATH, "//*[@id='march-1993-a-new-hope-for-men-everywhere']").is_displayed()
    if fims_section is True:
        print("testcase21 Passed")
        assert True
    else:
        print("testcase21 Failed")
        assert False

@allure.severity(allure.severity_level.MINOR)
def testcase22():
    # chekc the the sixth milestone
    sms_section = driver.find_element(By.XPATH, "//*[@id='november-1993-you-focus-on-the-science-well-focus-on-the-fundraising']").is_displayed()
    if sms_section is True:
        print("testcase22 Passed")
        assert True
    else:
        print("testcase22 Failed")
        assert False

# To check the donate and fundraiser buttons of the Treatment centre page
@allure.severity(allure.severity_level.CRITICAL)
def testcase23():
    testcase10()
@allure.severity(allure.severity_level.CRITICAL)
def testcase24():
    testcase11()
@allure.severity(allure.severity_level.CRITICAL)
def testcase25():
    testcase14()
