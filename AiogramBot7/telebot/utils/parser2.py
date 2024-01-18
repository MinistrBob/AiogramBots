from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


def get_items():
    # Initialize Playwright
    with sync_playwright() as p:
        # Create a browser context
        browser = p.chromium.launch()
        # Create a new page
        page = browser.new_page()
        # Navigate to the website
        page.goto("https://www.avito.ru/all/telefony/mobilnye_telefony/apple/iphone_13_pro_max/512_gb-ASgBAgICBESywA3yvcgBtMANzqs5sMENiPw35uAN~sFc?cd=1&f=ASgBAgECBESywA3yvcgBtMANzqs5sMENiPw35uAN~sFcAUXGmgwaeyJmcm9tIjo1MDAwMCwidG8iOjUwMDAwMH0")
        # Get the page content
        page_text = page.content()
        # Close the browser
        browser.close()
    # Print or use the page content as needed
    # print(page_text)
    soup = BeautifulSoup(page_text, "lxml")
    # print(soup.prettify())
    catalog = soup.find('div', {'data-marker': 'catalog-serp'})
    # print(catalog)
    try:
        items = catalog.find_all('div', {'data-marker': 'item'})
        # print(items[0])
    except Exception as e:
        error_text = f"Error: {e}"
        print(error_text)
        return None
    result = ""
    for index, item in enumerate(items):
        if index < 3:
            description = item.find('meta', {'itemprop': 'description'})
            print(description)
            description_text = description.get('content')
            print(description_text)

            title = item.find('h3').text
            print(title)

            price = item.find('meta', {'itemprop': 'price'})
            print(price)
            price_value = price.get('content')
            print(price_value)
            result = f"{result}\n<b>{title}</b>\n<b>{price_value}</b>\n{description_text}\n\n"
        else:
            break  # Exit the loop after processing the first three elements
    return result


if __name__ == '__main__':
    get_items()
