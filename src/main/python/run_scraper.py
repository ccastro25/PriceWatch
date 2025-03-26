#!/usr/bin/env python3
from scrape_cvs import get_cvs_products
from grocery_list import grocery_list2
import time
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    filename='price_scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_scraper_with_lists():
    try:
        logging.info("Starting CVS price scraping with both lists...")
        ''' 
        # First list
        print("\nScraping first grocery list...")
        logging.info("Starting first grocery list scraping")
        products_list1 = get_cvs_products(grocery_list)
        logging.info(f"Successfully scraped {len(products_list1)} products from first list")
        
        # Wait for 5 minutes before starting second list
        print("\nWaiting 5 minutes before starting second list...")
        time.sleep(300)  # 5 minutes = 300 seconds
        
        # Second list
        print("\nScraping second grocery list...")
        '''
        logging.info("Starting second grocery list scraping")
        products_list2 = get_cvs_products(grocery_list2)
        logging.info(f"Successfully scraped {len(products_list2)} products from second list")
        
        # Combine results
       # all_products = products_list1 + products_list2
        logging.info(f"Total products scraped: {len(products_list2)}")
        
        # Print summary
        print(f"\nScraping completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Total products scraped: {len(all_products)}")
        #print(f"Products from first list: {len(products_list1)}")
        print(f"Products from second list: {len(products_list2)}")
        
    except Exception as e:
        error_msg = f"Error during scraping: {str(e)}"
        logging.error(error_msg)
        print(f"\nError: {error_msg}")

if __name__ == "__main__":
    run_scraper_with_lists() 