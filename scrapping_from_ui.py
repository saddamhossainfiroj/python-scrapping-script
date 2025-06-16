import requests
from bs4 import BeautifulSoup
import csv
import time
from random import randint

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def scrape_website(url, output_file):
    try:
        # Respectful scraping with delay
        time.sleep(randint(1, 3))
        
        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()  # Raises exception for 4XX/5XX errors
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Extract product data from e-commerce site
        products = soup.find_all('div', class_='durbar_shop_category_books_items')
        
        with open(output_file, 'w', newline='', encoding='utf-8-sig') as csvfile:
            fieldnames = ['name', 'price', 'rating', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for product in products:
                try:
                    name = product.find('div', class_='durbar_shop_product_title').find('h4').get_text(strip=True)
                    price = product.find('del').get_text(strip=True)
                    product_url = 'https://durbarshop.com' + product.find('img')['src']
                    
                    writer.writerow({
                        'name': name,
                        'price': price,
                        'rating': 3,
                        'url': product_url
                    })
                except AttributeError as e:
                    print(f"Skipping a product due to error: {e}")
                    continue
                
        print(f"Successfully scraped data to {output_file}")
        
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    

# Usage
scrape_website('https://durbarshop.com/book/category/1/Islami-boi/', 'products_data_from_ui.csv')