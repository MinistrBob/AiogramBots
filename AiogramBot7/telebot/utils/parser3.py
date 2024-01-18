from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import asyncio


async def get_items():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(
            "https://www.avito.ru/all/telefony/mobilnye_telefony/apple/iphone_13_pro_max/512_gb-ASgBAgICBESywA3yvcgBtMANzqs5sMENiPw35uAN~sFc?cd=1&f=ASgBAgECBESywA3yvcgBtMANzqs5sMENiPw35uAN~sFcAUXGmgwaeyJmcm9tIjo1MDAwMCwidG8iOjUwMDAwMH0")
        page_content = await page.content()
        await browser.close()

    soup = BeautifulSoup(page_content, "lxml")
    catalog = soup.find('div', {'data-marker': 'catalog-serp'})

    try:
        items = catalog.find_all('div', {'data-marker': 'item'})
    except Exception as e:
        error_text = f"Error: {e}"
        print(error_text)
        return None

    result = ""
    for index, item in enumerate(items):
        if index < 3:
            description = item.find('meta', {'itemprop': 'description'})
            description_text = description.get('content') if description else ""

            title_tag = item.find('h3')
            title = title_tag.text if title_tag else ""

            price = item.find('meta', {'itemprop': 'price'})
            price_value = price.get('content') if price else ""

            result = f"{result}\n<b>{title}</b>\n<b>{price_value}</b>\n{description_text}\n\n"
        else:
            break

    return result


async def main():
    result = await get_items()
    print(result)


if __name__ == '__main__':
    asyncio.run(main())
