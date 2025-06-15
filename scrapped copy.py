import requests
from bs4 import BeautifulSoup
import csv
import time
from random import randint

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def scrape_website(url, output_file):
    # try:
    #     # Respectful scraping with delay
    #     time.sleep(randint(1, 3))
        
    #     response = requests.get(url, headers=headers, verify=False)
    #     response.raise_for_status()  # Raises exception for 4XX/5XX errors
        
    #     soup = BeautifulSoup(response.text, 'html.parser')
        
    #     # Example: Extract product data from e-commerce site
    #     products = soup.find_all('div', class_='product-cart-wrap')
    #     print('data: ',products)
        
    #     with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    #         fieldnames = ['name', 'price', 'rating', 'url']
    #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #         writer.writeheader()
            
    #         for product in products:
    #             try:
    #                 name = product.find('h2').get_text(strip=True)
    #                 price = product.find('span').get_text(strip=True)
    #                 product_url = product.find('a')['href']
                    
    #                 writer.writerow({
    #                     'name': name,
    #                     'price': price,
    #                     'rating': 3,
    #                     'url': product_url
    #                 })
    #             except AttributeError as e:
    #                 print(f"Skipping a product due to error: {e}")
    #                 continue
                
    #     print(f"Successfully scraped data to {output_file}")
        
    # except requests.exceptions.RequestException as e:
    #     print(f"Request failed: {e}")
    # except Exception as e:
    #     print(f"An error occurred: {e}")
    url = 'https://ultimateasiteapi.com/api/get-products'  # Replace with actual API endpoint
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
        'Accept': 'application/json',
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for product in data['data']['data']:  # Adjust based on actual structure
            print('product: ',product.keys())
            print(product['name'], '|', product['regular_price'])
    else:
        print("Failed to fetch data:", response.status_code)

# Usage
scrape_website('https://ultimateorganiclife.com/', 'products_data.csv')