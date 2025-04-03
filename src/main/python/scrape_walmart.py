from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import re
from fake_useragent import UserAgent
import logging
from datetime import datetime
import random

# Set up logging
logging.basicConfig(
    filename='price_scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_random_user_agent():
    ua = UserAgent()
    return ua.random

def setup_driver():
    try:
        # Configure Chrome options
        options = Options()
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-web-security')
        options.add_argument('--disable-webgl')
        options.add_argument('--disable-software-rasterizer')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-notifications')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--start-maximized')
        
        # Block location requests and configure other preferences
        options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.geolocation": 2,  # Block location requests
            "profile.managed_default_content_settings.images": 1,  # Load images
            "profile.managed_default_content_settings.javascript": 1,  # Enable JavaScript
            "profile.managed_default_content_settings.cookies": 1  # Enable cookies
        })
        
        # Add random user agent
        options.add_argument(f'user-agent={get_random_user_agent()}')
        
        # Initialize Chrome driver
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1920, 1080)
        
        return driver
    except Exception as e:
        logging.error(f"Error setting up Chrome driver: {str(e)}")
        raise

def set_location(driver):
    try:
        # Step 1: Click location button
        location_button = driver.find_element(By.CSS_SELECTOR, "button[data-tl-id='header-zip-code-button']")
        location_button.click()
        time.sleep(2)  # Wait for popup to open
        logging.info("Clicked location button")
    except Exception as e:
        logging.error(f"Location button not found: {str(e)}")
        return False

    try:
        # Step 2: Enter ZIP code
        zip_input = driver.find_element(By.CSS_SELECTOR, "input[data-tl-id='location-form-input']")
        zip_input.clear()
        zip_input.send_keys("19124")  # Enter ZIP Code
        zip_input.send_keys(Keys.RETURN)
        time.sleep(3)  # Wait for location update
        logging.info("Entered ZIP code 19124")
    except Exception as e:
        logging.error(f"ZIP code input field not found: {str(e)}")
        return False

    try:
        # Step 3: Select first store
        first_store = driver.find_element(By.CSS_SELECTOR, "button[data-tl-id='fulfillment-flyout-select-btn']")
        first_store.click()
        time.sleep(3)  # Wait for store selection
        logging.info("Selected first store")
        return True
    except Exception as e:
        logging.error(f"First store selection button not found: {str(e)}")
        return False

def get_walmart_products(items_to_scrape=None):
    if items_to_scrape is None:
        items_to_scrape = ["water"]  # Default item if none provided
    
    products = []
    driver = setup_driver()
    
    try:
        # First, set the location
        driver.get("https://www.walmart.com")
        if not set_location(driver):
            logging.error("Failed to set location")
            return products
        
        for item in items_to_scrape:
            try:
                print(f"Searching for: {item}")
                url = f"https://www.walmart.com/search?q={item}"
                driver.get(url)
                
                # Wait for the page to load
                time.sleep(5)
                
                # Extract product names and prices
                product_elements = driver.find_elements(By.CSS_SELECTOR, "div.mb1.ph1.pa0-xl.bb.b--near-white.w-25")
                
                for product in product_elements:
                    try:
                        title = product.find_element(By.CSS_SELECTOR, "span.lh-title").text.strip()
                        price_elem = product.find_element(By.CSS_SELECTOR, "span[data-automation-id='product-price']")
                        price = re.sub('[^0-9,.]', '', price_elem.text.strip())
                        
                        if title and price:
                            products.append((title, price, datetime.now().date(), "Walmart"))
                            print(f"Found: {title} - ${price}")
                    
                    except NoSuchElementException as e:
                        logging.warning(f"Could not find element for product: {str(e)}")
                        continue
                    except Exception as e:
                        logging.error(f"Error processing product: {str(e)}")
                        continue
                
                # Random delay between items
                delay = random.uniform(30, 60)
                print(f"Waiting {delay:.1f} seconds before next search...")
                time.sleep(delay)
                
                # Random user agent changes
                if random.random() < 0.3:  # 30% chance to change user agent
                    driver.quit()
                    driver = setup_driver()
                    # Set location again after driver restart
                    driver.get("https://www.walmart.com")
                    if not set_location(driver):
                        logging.error("Failed to set location after driver restart")
                        continue
                    time.sleep(random.uniform(10, 20))
                
            except Exception as e:
                logging.error(f"Error searching for {item}: {str(e)}")
                continue
    
    except Exception as e:
        logging.error(f"Error in main scraping loop: {str(e)}")
    finally:
        driver.quit()
    
    return products
