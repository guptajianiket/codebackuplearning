from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
startTime = time.time()
service = Service("C:\\Users\\aniket.gupta\\Desktop\\chromedriver_win32 (1)\\chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.implicitly_wait(6)
driver.get("https://interactivity-staging-viacom18.web.app/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "input[name=email]").click()
driver.find_element(By.CSS_SELECTOR, "input[name=email]").send_keys("vaibhav.sharma@webdunia.net")
driver.find_element(By.XPATH, "//*[@id='password']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='password']").send_keys("Admin@Viacom18")
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div/main/div/form/button/span[1]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div/div[2]/div[3]/p").click()
time.sleep(10)

sh = 0
def searc():
    page_number = driver.find_element(By.CSS_SELECTOR, "#call-for-entry > div:nth-child(3) > ul > li.active > a").text

    # 1st Row
    try:
        driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/table/tbody/tr[1]/td[2]").text
    except NoSuchElementException:
        print("No Such Element 1")
    else:
        L1 = driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/table/tbody/tr[1]/td[2]").text
        globals()['sh'] = globals()['sh'] + 1

    time.sleep(0.02)
    # 2nd Row
    try:
        driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/table/tbody/tr[2]/td[2]").text
    except NoSuchElementException:
        print("No Such Element 2")
    else:
        L2 = driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/table/tbody/tr[2]/td[2]").text
        globals()['sh'] = globals()['sh'] + 1

    time.sleep(0.02)
    # 3rd Row
    try:
        driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/table/tbody/tr[3]/td[2]").text
    except NoSuchElementException:
        print("No Such Element 3")
    else:
        L3 = driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/table/tbody/tr[3]/td[2]").text
        globals()['sh'] = globals()['sh'] + 1

    time.sleep(0.02)
    # 4th Row
    try:
        driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/table/tbody/tr[4]/td[2]").text
    except NoSuchElementException:
        print("No Such Element 4")
    else:
        L4 = driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/table/tbody/tr[4]/td[2]").text
        globals()['sh'] = globals()['sh'] + 1

    time.sleep(0.02)
    # 5th Row
    try:
        driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/table/tbody/tr[5]/td[2]").text
    except NoSuchElementException:
        print("No Such Element 5")
    else:
        L5 = driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/table/tbody/tr[5]/td[2]").text
        globals()['sh'] = globals()['sh'] + 1

    time.sleep(0.02)
    # 6th Row
    try:
        driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/table/tbody/tr[6]/td[2]").text
    except NoSuchElementException:
        print("No Such Element 6")
    else:
        L6 = driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/table/tbody/tr[6]/td[2]").text
        globals()['sh'] = globals()['sh'] + 1

    time.sleep(0.02)
    # 7th Row
    try:
        driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/table/tbody/tr[7]/td[2]").text
    except NoSuchElementException:
        print("No Such Element 7")
    else:
        L7 = driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/table/tbody/tr[7]/td[2]").text
        globals()['sh'] = globals()['sh'] + 1

    time.sleep(0.02)
    # 8th Row
    try:
        driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/table/tbody/tr[8]/td[2]").text
    except NoSuchElementException:
        print("No Such Element 8")
    else:
        L8 = driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/table/tbody/tr[8]/td[2]").text
        globals()['sh'] = globals()['sh'] + 1

    time.sleep(0.02)
    # 9th Row
    try:
        driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/table/tbody/tr[9]/td[2]").text
    except NoSuchElementException:
        print("No Such Element 9")
    else:
        L9 = driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/table/tbody/tr[9]/td[2]").text
        globals()['sh'] = globals()['sh'] + 1

    time.sleep(0.02)
    # 10th Row
    try:
        driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/table/tbody/tr[10]/td[2]").text
    except NoSuchElementException:
        print("No Such Element 10")
    else:
        L10 = driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/table/tbody/tr[10]/td[2]").text
        globals()['sh'] = globals()['sh'] + 1

    def list():
        expected = "1316check"
        if globals()['sh'] == 10:
            if L1 == expected:
                print(f"The expected CFE is in ninth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L2 == expected:
                print(f"The expected CFE is in second row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L3 == expected:
                print(f"The expected CFE is in third row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L4 == expected:
                print(f"The expected CFE is in fourth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L5 == expected:
                print(f"The expected CFE is in fifth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L6 == expected:
                print(f"The expected CFE is in sixth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L7 == expected:
                print(f"The expected CFE is in seventh row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L8 == expected:
                print(f"The expected CFE is in eighth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L9 == expected:
                print(f"The expected CFE is in ninth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L10 == expected:
                print(f"The expected CFE is in tenth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            else:
                next = driver.find_element(By.LINK_TEXT, "next")
                next.click()
                globals()['sh'] = 0
                searc()
        elif globals()['sh'] == 9:
            if L1 == expected:
                print(f"The expected CFE is in ninth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L2 == expected:
                print(f"The expected CFE is in second row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L3 == expected:
                print(f"The expected CFE is in third row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L4 == expected:
                print(f"The expected CFE is in fourth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L5 == expected:
                print(f"The expected CFE is in fifth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L6 == expected:
                print(f"The expected CFE is in sixth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L7 == expected:
                print(f"The expected CFE is in seventh row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L8 == expected:
                print(f"The expected CFE is in eighth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L9 == expected:
                print(f"The expected CFE is in ninth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            else:
                print("The seacrhed CFE name is not present")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
        elif globals()['sh'] == 8:
            if L1 == expected:
                print(f"The expected CFE is in ninth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L2 == expected:
                print(f"The expected CFE is in second row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L3 == expected:
                print(f"The expected CFE is in third row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L4 == expected:
                print(f"The expected CFE is in fourth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L5 == expected:
                print(f"The expected CFE is in fifth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L6 == expected:
                print(f"The expected CFE is in sixth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L7 == expected:
                print(f"The expected CFE is in seventh row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L8 == expected:
                print(f"The expected CFE is in eighth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            else:
                print("The seacrhed CFE name is not present")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()

        elif globals()['sh'] == 7:
            if L1 == expected:
                print(f"The expected CFE is in ninth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L2 == expected:
                print(f"The expected CFE is in second row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L3 == expected:
                print(f"The expected CFE is in third row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L4 == expected:
                print(f"The expected CFE is in fourth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L5 == expected:
                print(f"The expected CFE is in fifth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L6 == expected:
                print(f"The expected CFE is in sixth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L7 == expected:
                print(f"The expected CFE is in seventh row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            else:
                print("The seacrhed CFE name is not present")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()

        elif globals()['sh'] == 6:
            if L1 == expected:
                print(f"The expected CFE is in ninth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L2 == expected:
                print(f"The expected CFE is in second row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L3 == expected:
                print(f"The expected CFE is in third row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L4 == expected:
                print(f"The expected CFE is in fourth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L5 == expected:
                print(f"The expected CFE is in fifth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L6 == expected:
                print(f"The expected CFE is in sixth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            else:
                print("The seacrhed CFE name is not present")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()

        elif globals()['sh'] == 5:
            if L1 == expected:
                print(f"The expected CFE is in ninth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L2 == expected:
                print(f"The expected CFE is in second row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L3 == expected:
                print(f"The expected CFE is in third row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L4 == expected:
                print(f"The expected CFE is in fourth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L5 == expected:
                print(f"The expected CFE is in fifth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            else:
                print("The seacrhed CFE name is not present")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()

        elif globals()['sh'] == 4:
            if L1 == expected:
                print(f"The expected CFE is in ninth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L2 == expected:
                print(f"The expected CFE is in second row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L3 == expected:
                print(f"The expected CFE is in third row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L4 == expected:
                print(f"The expected CFE is in fourth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            else:
                print("The seacrhed CFE name is not present")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()

        elif globals()['sh'] == 3:
            if L1 == expected:
                print(f"The expected CFE is in ninth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L2 == expected:
                print(f"The expected CFE is in second row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L3 == expected:
                print(f"The expected CFE is in third row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            else:
                print("The seacrhed CFE name is not present")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()

        elif globals()['sh'] == 2:
            if L1 == expected:
                print(f"The expected CFE is in ninth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            elif L2 == expected:
                print(f"The expected CFE is in second row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            else:
                print("The seacrhed CFE name is not present")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()

        elif globals()['sh'] == 1:
            if L1 == expected:
                print(f"The expected CFE is in ninth row of page {page_number}")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()
            else:
                print("The seacrhed CFE name is not present")
                print('\nTask Completed!\n\nThe script took {0} seconds !'.format(time.time() - startTime))
                quit()


    list()


searc()


