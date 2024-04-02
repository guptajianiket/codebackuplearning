from selenium import webdriver

# Specify the URL of the webpage to crawl
url = "https://www.gasb.org"

# Specify the path to the ChromeDriver executable
chrome_driver_path = "C:\\Users\\aniket.gupta\\Desktop\\chromedriver.exe"

# Initialize Chrome WebDriver with the specified path
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.implicitly_wait(10)

# Navigate to the URL
driver.get(url)

# Find all URLs in the header menu
header_menu_items = driver.find_elements_by_xpath("//*[@id='__next']/div/div/header/div/div/div/div/ul//a")

# Define a dictionary to store URLs with variable names
url_variables = {}

# Function to extract variable names from URL paths
def extract_variable_name(url):
    # Split the URL path by "/"
    path_parts = url.split("/")
    # Remove empty parts
    path_parts = [part for part in path_parts if part]
    # Extract the last part as variable name
    variable_name = path_parts[-1].split(".")[0]  # Remove any file extension
    # Replace "-" with "_" in the variable name
    variable_name = variable_name.replace("-", "_")
    return variable_name

# Extract URLs and assign them to variables
for item in header_menu_items:
    href = item.get_attribute("href")
    if href:
        variable_name = extract_variable_name(href)
        url_variables[variable_name] = href

# Print the variables and their corresponding URLs
for name, link in url_variables.items():
    print(f"{name} = '{link}'")

# Close the WebDriver
driver.quit()
