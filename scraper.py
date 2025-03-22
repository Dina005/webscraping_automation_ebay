from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless")  
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

# Rotate User-Agent to prevent detection
ua = UserAgent()
options.add_argument(f"user-agent={ua.random}")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Define the target website
URL = "https://www.ebay.com/globaldeals/tech"

# Scroll down the page to trigger lazy loading of all product listings
def scroll_page():
    try:
        print("Scrolling down to load more results...")
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)  # Wait for new results to load
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break  # Stop scrolling if no more content is loaded
            last_height = new_height
        print("Scrolling complete.")
    except Exception as e:
        print(f"Error during scrolling: {e}")

#Scrape Ebay Tech Deals Data
def scrape_ebay_data():
    
    driver.get(URL)
    time.sleep(10)  # Allow time for elements to load
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class= "dne-itemtile-detail"]'))
    )
    scroll_page()

    all_products_data = []
    
    try:
        
        product_elements = driver.find_elements(By.XPATH, '//div[@class= "dne-itemtile-detail"]')
        print("Number of Elements Found: ", len(product_elements))
        for product in product_elements:
        
        #Extract Title
            try:
                title = product.find_element(By.XPATH, './/span[@itemprop = "name"]').text
            except:
                title = "N/A"
        
        #Extract Price 
            try:
                price = product.find_element(By.XPATH, './/span[@class = "first"]').text
            except:
                price = "N/A"
        
        #Extract Original Price:
            try:
                original_price = product.find_element(By.XPATH, './/div[@class="dne-itemtile-original-price"]/span/span').text
            except:
                original_price = "N/A"
        
        #Extract Shipping Details:
             try:
                shipping_details= product.find_element(By.XPATH, ".//span[contains(@class, 'dne-itemtile-delivery')]").text
                print(shipping_details)
            except:
                shipping_details = "N/A"
        
        #Extract Item Url
            try:
                item_url = product.find_element(By.XPATH, './/a[@itemprop = "url"]').get_attribute("href")
            except:
                item_url = "N/A"
            
        #Extract timestamp of when the Product was Scraped
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        #Store the data in a dictionary
            ebay_data = ({
                    "timestamp": timestamp,
                    "title": title,
                    "price": price,
                    "original_price": original_price,
                    "shipping_details": shipping_details,
                    "item_url": item_url,
                })
            all_products_data.append(ebay_data)
        
    except Exception as e:
        print("Error occurred:", e)
    
    return all_products_data

#Save to CSV File
def save_to_csv(data):
    """Save scraped data to CSV."""
    file_name = "ebay_tech_deals.csv"
    try:
        df = pd.read_csv(file_name)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["timestamp", "title", "price", "original_price", "shipping_details", "item_url"])
    new_data = pd.DataFrame(data)
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(file_name, index=False)

if __name__ == "__main__":
    print("Scraping Ebay Data...")
    scraped_data = scrape_ebay_data()
    if scraped_data:
        save_to_csv(scraped_data)
        print("Data saved to ebay_tech_deals.csv")
        
    driver.quit()
