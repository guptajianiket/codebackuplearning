import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

chrome_driver_path = "C:\\Users\\aniket.gupta\\Desktop\\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(10)

def tncpagecheck(driver):
    try:
        tnctxt = driver.find_element(By.XPATH, "//*[@id='main']/p[3]").text
        accptbutton = driver.find_element(By.XPATH, "//*[@id='main']/a/button").is_displayed()
        if tnctxt == "Do you accept the terms?" and accptbutton:
            return True
        else:
            return False
    except:
        return False

driver.get("https://fasb.org/archive/exposure-documents")  # Replace "url_of_the_page" with the actual URL of the page

row_number = 0  # Initialize row number counter

while True:
    # Iterate through each page
    while True:
        # Iterate through each row in the table
        rows = driver.find_elements(By.XPATH, "//table[@id='table-scroll']/tbody/tr")  # Replace "table_id" with actual ID of the table
        for row in rows:
            row_number += 1  # Increment row number counter

            # Check the link in the specific column (e.g., column index 2)
            try:
                link = row.find_element(By.XPATH, ".//td[2]//a[contains(text(),'Download')]")
                link_url = link.get_attribute("href")

                # Open the link in a new tab
                driver.execute_script("window.open('" + link_url + "', 'new_window')")
                driver.switch_to.window(driver.window_handles[1])

                # Verify if the page redirects correctly by checking the presence of accept button
                if tncpagecheck(driver):
                    print(f"Link from row {row_number} redirects to the correct page.")
                else:
                    print(f"Link from row {row_number} does not redirect to the correct page {link_url}.")

                # Close the new tab
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

            except Exception as e:
                print("Error occurred:", e)

        # Check if there's a next page
        next_button = driver.find_element(By.CLASS_NAME,'next-icon')
        if next_button.is_displayed():
            ActionChains(driver).move_to_element(next_button).click().perform()
            time.sleep(2)  # Adding a small delay to allow the page to load
        else:
            # If there is no "Next" button, exit the loop
            break

    # Close the WebDriver
    driver.quit()
