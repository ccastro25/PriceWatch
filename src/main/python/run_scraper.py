from scrape_cvs import get_cvs_products
from scrape_walmart import get_walmart_products
from grocery_list import  grocery_list2
from db_utils import DatabaseManager
import time
import logging

# Set up logging
logging.basicConfig(
    filename='price_scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    try:
        # Initialize database manager
        db_manager = DatabaseManager()
        
        print("\nScraping first grocery list...")
       # products_list1 = get_cvs_products(grocery_list1)
       # logging.info(f"Successfully scraped {len(products_list1)} products from first list")
        
        # Add delay between lists
        time.sleep(300)  # 5 minutes delay
        
        print("\nScraping second grocery list...")
        products_list2 = get_walmart_products(grocery_list2)
        logging.info(f"Successfully scraped {len(products_list2)} products from second list")
        
        # Store all products in database
        for product in  products_list2:
            db_manager.insert_product(product[0], product[1], product[2], product[3])
        
        print("\nScraping completed successfully!")
        
    except Exception as e:
        logging.error(f"Error in main execution: {str(e)}")
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main() 