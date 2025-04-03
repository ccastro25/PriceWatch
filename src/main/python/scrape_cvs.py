from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import re
import pickle
from fake_useragent import UserAgent
import logging
from datetime import datetime
from db_utils import DatabaseManager
from webdriver_manager.firefox import GeckoDriverManager
import random
from grocery_list import grocery_list2

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
        # Set up Firefox options
        options = Options()
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        # Add random user agent
        user_agent = get_random_user_agent()
        print(f"Using User-Agent: {user_agent}")
        options.set_preference("general.useragent.override", user_agent)
        
        # Additional Firefox preferences to make it look more like a real browser
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference('useAutomationExtension', False)
        options.set_preference("privacy.trackingprotection.enabled", False)
        options.set_preference("browser.cache.disk.enable", True)
        options.set_preference("browser.cache.memory.enable", True)
        options.set_preference("browser.cache.offline.enable", True)
        options.set_preference("network.http.use-cache", True)
        
        # Initialize the Firefox driver with webdriver-manager
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        
        # Set window size to a common resolution
        driver.set_window_size(1920, 1080)
        
        # Additional JavaScript to mask automation
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5]})")
        driver.execute_script("Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']})")
        
        return driver
    except Exception as e:
        logging.error(f"Error setting up Firefox driver: {str(e)}")
        raise

def human_like_delay():
    # Longer random delay between 8-15 seconds
    time.sleep(random.uniform(8, 15))

def simulate_human_behavior(driver):
    # More natural mouse movements
    action = ActionChains(driver)
    for _ in range(random.randint(3, 7)):
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        action.move_by_offset(x, y)
        # Longer pauses between movements
        action.pause(random.uniform(0.5, 1.5))
    action.perform()
    
    # More natural scrolling behavior
    for _ in range(random.randint(2, 4)):
        scroll_amount = random.randint(50, 200)
        driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
        # Longer pauses between scrolls
        time.sleep(random.uniform(1.5, 3.0))
    
    # Sometimes scroll back up a bit
    if random.random() < 0.3:
        driver.execute_script(f"window.scrollBy(0, -{random.randint(50, 150)});")
        time.sleep(random.uniform(1.0, 2.0))

def get_product(driver, item):
    try:
        # Add longer random delay before navigation
        human_like_delay()
        
        # Navigate to the search page
        driver.get(f"https://www.cvs.com/search?searchTerm={item}")
        
        # Wait for the page to load (wait for a common element)
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "css-901oao"))
        )
        
        # Add longer random delay after page load
        human_like_delay()
        
        # Simulate human-like behavior
        simulate_human_behavior(driver)
        
        # Add longer random delay before parsing
        time.sleep(random.uniform(3, 5))
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        price = soup.find_all('div', class_="css-901oao r-1xaesmv r-ubezar r-majxgm r-wk8lta")
        title = soup.find_all('div', class_="css-901oao css-cens5h r-b0vftf r-1xaesmv r-ubezar r-majxgm r-29m4ib r-rjixqe r-1mnahxq r-fdjqy7 r-13qz1uu")

        products = []
        for i, v in enumerate(title):
            if i < len(price):  # Ensure we don't index out of bounds
                products.append((title[i].text, re.sub('[^0-9,.]', '', price[i].text), datetime.now().date(), "CVS"))
                print(f"Product: {title[i].text}")
                print(f"Price: {re.sub('[^0-9,.]', '', price[i].text)}")
                
        return products
    
    except TimeoutException:
        print(f"Timeout while searching for {item}")
        return []
    except Exception as e:
        print(f"Error while searching for {item}: {str(e)}")
        return []

def get_cvs_products(items_to_scrape=None):
    if items_to_scrape is None:
        items_to_scrape = grocery_list2
    
    products = []
    driver = setup_driver()
    
    try:
        for item in items_to_scrape:
            print(f"Searching for: {item}")
            products.extend(get_product(driver, item))
            
            # Much longer random delay between items (2-4 minutes)
            delay = random.uniform(120, 240)
            print(f"Waiting {delay:.1f} seconds before next search...")
            time.sleep(delay)
            
            # More frequent user agent changes
            if random.random() < 0.5:  # 50% chance to change user agent
                driver.quit()
                driver = setup_driver()
                # Add extra delay after changing user agent
                time.sleep(random.uniform(30, 60))
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()
    
    return products



