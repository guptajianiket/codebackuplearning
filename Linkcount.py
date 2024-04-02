from selenium import webdriver
from selenium.webdriver.common.by import By

# Specify the URL of the webpage to crawl
url = "https://fasb-live.prd.faf.us.com/Page/PageContent?PageId=/news-media/inthenews.html#filterByYear_2022"

# Specify the path to the ChromeDriver executable
chrome_driver_path = "C:\\Users\\aniket.gupta\\Desktop\\chromedriver.exe"

# Initialize Chrome WebDriver with the specified path
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.implicitly_wait(10)

# Navigate to the URL
driver.get(url)

# Find the specified element
element = driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div[1]/div[3]/div[1]/div/div[2]/div[3]")

# Find all anchor elements within the element
links = element.find_elements(By.TAG_NAME, "a")

# Count the number of links
link_count = len(links)

# Print the count of links
print(f"Number of links inside the specified element: {link_count}")

# Close the WebDriver
driver.quit()
