from selenium import webdriver
import time
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

startTime = time.time()
service = Service("C:\\Users\\aniket.gupta\\Desktop\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(25)

# Open the website where the alert appears
driver.get("http://ec2-18-136-231-25.ap-southeast-1.compute.amazonaws.com/SDL/#app=wcm&entry=home")

original_window = driver.current_window_handle  # Store the original window handle

try:
    # Wait for the new window to appear
    WebDriverWait(driver, 10).until(lambda driver: len(driver.window_handles) > 1)

    # Switch to the new window
    driver.switch_to.window(driver.window_handles[1])  # Assuming the new window is the second window handle

    # Wait
    time.sleep(10)

    # Mimic keyboard actions using pyautogui
    email = "avyas"
    pyautogui.write(email)

    # Press Tab to move to the password field
    pyautogui.press('tab')

    password = "Tr1d10n"
    pyautogui.write(password)

    # Press Tab to move to the OK button and then press Enter
    pyautogui.press('tab')
    pyautogui.press('enter')

finally:
    # Close the browser window
    driver.switch_to.window(original_window)
    time.sleep(3)
    driver.find_element(By.XPATH,"//*[@id='main-view-target']/div/div[2]/div[1]").click()
    time.sleep(5)
    driver.quit()
