# amazon-scraper

Scrapes Amazon search results and saves product titles and prices to a CSV file.

## Features
- Search any product by keyword
- Choose how many pages to scrape
- Exports results to a CSV file
- Handles request errors gracefully

## Requirements
- Python 3
- requests
- beautifulsoup4
- lxml

## Installation

pip install -r requirements.txt

## Usage

python amazon_scraper.py

You'll be asked for:
- Product keyword
- Starting page number
- Ending page number

Output file will be named `amazon_[keyword].csv`

## Sample Output

| Sr No. | Title | Price |
|--------|-------|-------|
| 1 | HP Laptop 15s | ₹52,990 |
| 2 | Lenovo IdeaPad Slim 3 | ₹41,990 |

## Note
Built while learning Python web scraping using Requests and BeautifulSoup.
