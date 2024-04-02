import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class TestFooterLinks(unittest.TestCase):
    def setUp(self):
        # Specify the path to the ChromeDriver executable
        chrome_driver_path = "C:\\Users\\aniket.gupta\\Desktop\\chromedriver.exe"
        # Initialize Chrome WebDriver with the specified path
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.implicitly_wait(10)

    def test_home_link(self):
        self.click_link_and_compare_url("home", "https://gasb.org/")

    def test_about_us_link(self):
        self.click_link_and_compare_url("about_us", "https://gasb.org/about-us")

    def test_about_the_gasb_link(self):
        self.click_link_and_compare_url("about_the_gasb", "https://gasb.org/about-us/about-the-gasb")

    # Define other test methods for each link, following the same pattern as above

    def click_link_and_compare_url(self, var_name, expected_url):
        # Navigate to the URL
        self.driver.get("https://gasb.org/")

        # Scroll to the bottom of the page
        self.driver.find_element_by_tag_name('body').send_keys(Keys.END)
        time.sleep(2)  # Add some delay to ensure footer elements are loaded

        # Find footer element by class name
        footer = self.driver.find_element_by_class_name('footer')

        # Find the anchor tag within the footer with the specified href
        link = footer.find_element_by_xpath(f".//a[contains(@href, '{expected_url}')]")

        # Get the current URL before clicking the link
        current_url = self.driver.current_url

        # Perform click action on the link
        ActionChains(self.driver).move_to_element(link).click(link).perform()

        # Check if the link opens in a new window/tab
        if len(self.driver.window_handles) > 1:
            # Switch to the new window/tab
            self.driver.switch_to.window(self.driver.window_handles[1])

            # Get the URL of the new window/tab
            new_window_url = self.driver.current_url

            # Compare the new window/tab URL with expected URL
            self.assertEqual(new_window_url, expected_url)

            # Close the new window/tab
            self.driver.close()

            # Switch back to the original window/tab
            self.driver.switch_to.window(self.driver.window_handles[0])
        else:
            # Compare the current page URL with expected URL
            self.assertEqual(self.driver.current_url, expected_url)

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
