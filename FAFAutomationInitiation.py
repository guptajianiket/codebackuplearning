from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Specify the URL of the webpage to crawl
url = "https://gasb.org/"

# Specify the path to the ChromeDriver executable
chrome_driver_path = "C:\\Users\\aniket.gupta\\Desktop\\chromedriver.exe"

# Initialize Chrome WebDriver with the specified path
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.implicitly_wait(10)

# Navigate to the URL
driver.get(url)

# Scroll to the bottom of the page
driver.find_element_by_tag_name('body').send_keys(Keys.END)

# Find footer element by class name
footer = driver.find_element_by_class_name('footer')

# Find all anchor tags within the footer
footer_links = footer.find_elements_by_tag_name('a')

# Dictionary to store URLs based on the last name in the URL path
url_dict = {}

# Extract URLs and assign them based on the last name in the path
for link in footer_links:
    href = link.get_attribute('href')
    if href:
        last_name = href.split('/')[-1]
        url_dict[last_name] = href

# Print the dictionary
print(url_dict)

# Close the WebDriver
driver.quit()
