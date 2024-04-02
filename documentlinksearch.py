import csv  # Import the csv module

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import requests
from io import BytesIO
import fitz  # PyMuPDF library for handling PDFs

# URL of the webpage containing links to PDFs
webpage_url = "https://fasb.org/archive/superseded-standards"

# Specify the path to the ChromeDriver executable
chrome_driver_path = "C:\\Users\\aniket.gupta\\Desktop\\chromedriver.exe"

# Setup Chrome options
chrome_options = Options()
# chrome_options.add_argument('--headless')  # Run Chrome in headless mode

# Start Chrome WebDriver
chrome_service = Service(chrome_driver_path)
chrome_service.start()
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.implicitly_wait(10)

# Navigate to the webpage
driver.get(webpage_url)

# Find all links on the webpage
links = driver.find_elements(By.TAG_NAME, 'a')

# Filter out only the PDF links based on their href attribute
pdf_links = [link.get_attribute('href') for link in links if 'pdf=' in link.get_attribute('href')]


# Function to handle TNC page
def handle_tnc_page():
    try:
        accept_button = driver.find_element(By.XPATH, "//*[@id='main']/a/button")
        accept_button.click()
        time.sleep(2)  # Adjust delay if necessary
    except NoSuchElementException:
        # TNC page not found or already accepted
        pass


# Function to extract URLs from PDF
def extract_urls_from_pdf(pdf_link):
    # Open the PDF link
    driver.execute_script("window.open('" + pdf_link + "','_blank');")
    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[-1])
    # Handle TNC page
    handle_tnc_page()
    # Get the current URL after accepting TNC (if applicable)
    current_url = driver.current_url
    # Close the tab
    driver.close()
    # Switch back to the main tab
    driver.switch_to.window(driver.window_handles[0])
    # Extract URLs from the PDF
    pdf_urls = []
    if current_url:
        try:
            response = requests.get(current_url)
            if response.status_code == 200:
                pdf_content = BytesIO(response.content)
                pdf_document = fitz.open(stream=pdf_content, filetype="pdf")
                for page_num in reversed(range(pdf_document.page_count)):  # Iterate from bottom to top
                    page = pdf_document.load_page(page_num)
                    page_urls = page.get_links()
                    for url_dict in page_urls:
                        pdf_urls.append(url_dict['url'])
                pdf_document.close()
        except Exception as e:
            print("Error extracting URLs from PDF:", e)
    return pdf_urls


# Counter for PDFs checked
pdfs_checked = 0
# Store URLs resulting in 404 errors
error_urls = []

# Start time
start_time = time.time()

# Iterate over each PDF link
for pdf_link in pdf_links:
    pdfs_checked += 1
    print(f"Checking PDF {pdfs_checked}/{len(pdf_links)}: {pdf_link}")

    # Extract URLs from the PDF
    extracted_urls = extract_urls_from_pdf(pdf_link)

    # Check if any URLs were extracted
    if extracted_urls:
        # Check each extracted URL for a 404 error
        for url in extracted_urls:
            response = requests.head(url)
            if response.status_code == 404:
                print("404 Error found in PDF:", pdf_link, "Link:", url)
                error_urls.append((pdf_link, url))
    else:
        print("No URLs found or error occurred while extracting URLs from PDF:", pdf_link)

# End time
end_time = time.time()
# Calculate script execution time
execution_time = end_time - start_time

# Save error URLs to CSV
csv_file = "error_urls.csv"
with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['PDF', 'URL'])
    writer.writerows(error_urls)

# Close the browser
driver.quit()

print("Script execution time:", execution_time, "seconds")
print("Error URLs saved to:", csv_file)
