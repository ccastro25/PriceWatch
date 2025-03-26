#!/usr/bin/env python3
import schedule
import time
from datetime import datetime
from scrape_cvs import get_cvs_products
import logging

# Set up logging
logging.basicConfig(
    filename='price_scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_scraper():
    try:
        logging.info("Starting CVS price scraping...")
        products = get_cvs_products()
        logging.info(f"Successfully scraped {len(products)} products from CVS")
        
        # Here you can add code to save the products to your database
        # For example, using your Spring Boot API endpoints
        
    except Exception as e:
        logging.error(f"Error during scraping: {str(e)}")

def main():
    # Schedule the scraper to run every Sunday at 1 AM
    schedule.every().sunday.at("01:00").do(run_scraper)
    
    logging.info("Price scraper scheduler started")
    print("Price scraper scheduler is running. Press Ctrl+C to exit.")
    
    while True:
        try:
            schedule.run_pending()
            time.sleep(604800)  # Check every minute
        except KeyboardInterrupt:
            logging.info("Scheduler stopped by user")
            break
        except Exception as e:
            logging.error(f"Error in scheduler: {str(e)}")
            time.sleep(60)  # Wait a minute before retrying

if __name__ == "__main__":
    main() 