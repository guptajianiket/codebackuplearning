from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import difflib


def get_page_data1(url1):
    driver = None
    try:
        driver = webdriver.Chrome()  # Change this line based on your browser driver
        driver.get(url1)
        # Assuming the data is within a specific element, adjust as needed
        data = driver.find_element(By.CSS_SELECTOR,'main-content-bar pb-50px').text
        return data
    except Exception as e:
        print(f"Error fetching {url1}: {e}")
        return None
    finally:
        driver.quit()

def get_page_data2(url2):
    try:
        driver = webdriver.Chrome()  # Change this line based on your browser driver
        driver.get(url2)
        # Assuming the data is within a specific element, adjust as needed
        data = driver.find_element(By.CSS_SELECTOR,'table-responsive').text
        return data
    except Exception as e:
        print(f"Error fetching {url2}: {e}")
        return None
    finally:
        driver.quit()


def perform_regression_test(url_baseline, url_updated):
    # Fetch data from the baseline and updated URLs
    data_baseline = get_page_data1(url_baseline)
    data_updated = get_page_data2(url_updated)

    if data_baseline is not None and data_updated is not None:
        # Compare the data
        if data_baseline == data_updated:
            print("Regression test passed. Data is consistent.")
        else:
            print("Regression test failed. Data has changed.")

            # Display the differences
            lines1 = data_baseline.splitlines()
            lines2 = data_updated.splitlines()
            for line in difflib.unified_diff(lines1, lines2):
                print(line)


if __name__ == "__main__":
    # Replace these URLs with the baseline and updated versions of your data page
    url_baseline = "https://fasb.org/page/pageContent?pageId=/reference-library/ballots.html"
    url_updated = "https://uat-live.fasb.rws.fafus.org/archive/ballots"

    # Perform regression testing using Selenium
    perform_regression_test(url_baseline, url_updated)
