

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no browser window)
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Set up Chrome driver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

try:
    # Navigate to Google homepage
    driver.get("https://www.google.com")

    # Find the search box and enter the search term
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Algeria news")
    search_box.submit()  # Submit the search form

    # Wait for the results to load
    time.sleep(2)

    # Extract the titles of the first 3 search results
    results = driver.find_elements(By.CSS_SELECTOR, 'h3')[:3]
    titles = [result.text for result in results]

    # Print the titles
    for idx, title in enumerate(titles, start=1):
        print(f"Title {idx}: {title}")

finally:
    # Clean up and close the browser
    driver.quit()
