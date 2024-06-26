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

# Initialize a dictionary to store URLs assigned to variables
url_variables = {}

# Extract URLs and assign them based on the last name in the path
for link in footer_links:
    href = link.get_attribute('href')
    if href:
        last_name = href.split('/')[-1].split('.')[0]  # Extracting last part of the URL without extension
        # Creating variable name by removing special characters and replacing hyphens with underscores
        var_name = last_name.replace('-', '_').replace('?', '').replace('=', '')
        url_variables[var_name] = href

# Print the dictionary with variable assignments
for var_name, url in url_variables.items():
    print(f"{var_name} = '{url}'")

# Close the WebDriver
driver.quit()
