import time

from lxml import html

from .constants import *


def get_product_links(page, session, headers, cookies):
    response = session.get(page, headers=headers, cookies=cookies)
    page = html.fromstring(response.content)
    links = page.xpath(XPATHS["product-links"])
    return links


def extract_product_data(product_link, session, headers, cookies):
    time.sleep(4)
    response = session.get(product_link, headers=headers, cookies=cookies)
    page = html.fromstring(response.content)
    url = product_link
    prev_price = []
    images = []
    sizes = page.xpath(XPATHS["sizes"])
    name = page.xpath(XPATHS["product-name"])
    brand = name[0].split(" ")
    brand_name = brand[0]
    price = page.xpath(XPATHS["product-price-3"])

    if len(price) == 0:
        price = page.xpath(XPATHS["product-price-1"])
    else:
        price = page.xpath(XPATHS["product-price-3"])
        prev_price = page.xpath(XPATHS["product-prev-price"])

    for i in range(1, 5):
        img = page.xpath(XPATHS["product-img-url"].replace("__ITER__", str(i)))
        images.append(img[0])

    description = page.xpath(XPATHS["product-description"])

    print("\nUrl: ", url)
    print("\nSizes: ", sizes)
    print("\nName: ", name)
    print("\nBrand: ", brand_name)
    print("\nImages: ", images)
    print("\nPrice: ", price)
    print("\nPrevious Price: ", prev_price)
    print("\nDescription: ", description)

    return url, sizes, name, brand_name, images, price, prev_price, description
