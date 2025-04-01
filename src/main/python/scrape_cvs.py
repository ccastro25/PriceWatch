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

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver

def human_like_delay():
    # Random delay between 3-7 seconds
    time.sleep(random.uniform(3, 7))

def get_product(driver, item):
    try:
        # Add random delay before navigation
        human_like_delay()
        
        # Navigate to the search page
        driver.get(f"https://www.cvs.com/search?searchTerm={item}")
        
        # Wait for the page to load (wait for a common element)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "css-901oao"))
        )
        
        # Add random delay after page load
        human_like_delay()
        
        # Scroll the page randomly to simulate human behavior
        scroll_amount = random.randint(100, 500)
        driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
        time.sleep(random.uniform(1, 3))
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        price = soup.find_all('div', class_="css-901oao r-1xaesmv r-ubezar r-majxgm r-wk8lta")
        title = soup.find_all('div', class_="css-901oao css-cens5h r-b0vftf r-1xaesmv r-ubezar r-majxgm r-29m4ib r-rjixqe r-1mnahxq r-fdjqy7 r-13qz1uu")

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
            
            # Add longer random delay between items (30-60 seconds)
            delay = random.uniform(30, 60)
            print(f"Waiting {delay:.1f} seconds before next search...")
            time.sleep(delay)
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()
    
    return products



