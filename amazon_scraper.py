import requests
from bs4 import BeautifulSoup
import csv
import time

def scrape():
    keyword1 = input("Enter product to search: ")
    keyword2 = keyword1.replace(" ", "+")
    keyword3 = keyword1.replace(" ", "_")

    page_start = input("Enter the starting page number: ")
    page_end = input("Enter the ending page number: ")
    page1 = int(page_start)
    page2 = int(page_end)

    if page1 > page2:
        print("Starting page cannot be greater than ending page.")
        return

    base_url = f'https://www.amazon.in/s?k={keyword2}'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }

    session = requests.Session()
    session.headers.update(headers)

    with open(f"amazon_{keyword3}.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Sr No.","Title","Price"])
        count = 0
        for page in range(page1, page2 + 1):
            url = f"{base_url}&page={page}"
            try:
                response = session.get(url, timeout=10)
                soup = BeautifulSoup(response.text, "lxml")
                products = soup.find_all("div", {"data-component-type": "s-search-result"})
                for product in products:
                    count += 1
                    title = product.find("h2")
                    price = product.find("span", class_="a-offscreen")

                    if title and price:
                        writer.writerow([count, title.text.strip(), price.text.strip()])
            except requests.RequestException as e:
                print(f"Something went wrong {e}")
            time.sleep(3)

if __name__ == "__main__":
    scrape()
