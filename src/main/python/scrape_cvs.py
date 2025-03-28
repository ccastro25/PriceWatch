from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from grocery_list import grocery_list2
from datetime import datetime
from bs4 import BeautifulSoup
import time
import re
import pickle  
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import undetected_chromedriver as uc
from fake_useragent import UserAgent

def setup_driver():
    options = uc.ChromeOptions()
    ua = UserAgent()
    options.add_argument(f'user-agent={ua.random}')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-infobars')
    
    driver = uc.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5]})")
    driver.execute_script("Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']})")
    return driver

def human_like_delay():
    # Random delay between 5-10 seconds
    time.sleep(random.uniform(5, 10))

def simulate_human_behavior(driver):
    try:
        # Get the window size
        window_size = driver.get_window_size()
        max_x = window_size['width'] - 50  # Leave 100px margin
        max_y = window_size['height'] - 50  # Leave 100px margin
        
        # Random mouse movements within safe bounds
        action = ActionChains(driver)
        for _ in range(random.randint(2, 4)):
            x = random.randint(20, max_x)  # Start from 50px to avoid edges
            y = random.randint(20, max_y)  # Start from 50px to avoid edges
            action.move_by_offset(x, y)
            action.pause(random.uniform(0.5, 1.5))
        action.perform()
        
        # Random scrolling with smaller increments
        for _ in range(random.randint(2, 4)):
            scroll_amount = random.randint(50, 150)  # Smaller scroll amounts
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            time.sleep(random.uniform(1, 2))
    except Exception as e:
        print(f"Warning: Could not simulate human behavior: {str(e)}")
        # Continue execution even if mouse movement fails
        pass

def get_product(driver, item):
    try:
        # Add random delay before navigation
        human_like_delay()
        
        # Navigate to the search page
        driver.get(f"https://www.cvs.com/search?searchTerm={item}")
        
        # Wait for the page to load (wait for a common element)
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "css-901oao"))
        )
        
        # Add random delay after page load
        human_like_delay()
        
        # Simulate human-like behavior
        #simulate_human_behavior(driver)
        
        # Add another delay before parsing
        time.sleep(random.uniform(3, 5))
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')                 
        price = soup.find_all('div', class_="css-901oao r-1xaesmv r-ubezar r-majxgm r-wk8lta")
        title = soup.find_all('div', class_="css-901oao css-cens5h r-b0vftf r-1xaesmv r-ubezar r-majxgm r-29m4ib r-rjixqe r-1bymd8e r-fdjqy7 r-13qz1uu")

        products = []
        for i, v in enumerate(title):
            if i < len(price):  # Ensure we don't index out of bounds
                products.append((title[i].text, re.sub('[^0-9,.]', '', price[i].text), datetime.now().date(), "CVS"))
        
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
            
            # Add longer random delay between items (90-120 seconds)
            delay = random.uniform(90, 120)
            print(f"Waiting {delay:.1f} seconds before next search...")
            time.sleep(delay)
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()
    
    return products



