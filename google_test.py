from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_google_search():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start browser maximized
    
    # Initialize the Chrome driver with automatic driver management
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    
    try:
        # Navigate to Google
        driver.get("https://www.google.com")
        
        # Wait for 3 seconds to see the page (you can adjust or remove this)
        time.sleep(3)
        
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_google_search()
