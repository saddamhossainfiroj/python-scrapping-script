import requests
from bs4 import BeautifulSoup
import csv
import time
from random import randint

def scrape_website(url, output_file):
    url = 'https://ultimateasiteapi.com/api/get-products'  # Replace with actual API endpoint
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
        'Accept': 'application/json',
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['name', 'price', 'rating', 'large_image_url', 'medium_image_url', 'small_image_url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            data = response.json()
            for product in data['data']['data']:  # Adjust based on actual structure
                print('product: ',product.keys())
                writer.writerow({
                    'name': product['name'],
                    'price': product['regular_price'],
                    'rating': 3,
                    'large_image_url': product['image']['large'],
                    'medium_image_url': product['image']['medium'],
                    'small_image_url': product['image']['small']
                })
    else:
        print("Failed to fetch data:", response.status_code)

# Usage
scrape_website('https://ultimateorganiclife.com/', 'products_data_from_api.csv')