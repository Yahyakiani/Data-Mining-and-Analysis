# this is the product link from which the data will be scrapped
MISCS = {
    "Product-page-link": "https://www.snkrs.com/en/263-men",
}

# XPATHS contains queries which are done by XPATH chrome extension. It get the desired data from website and store it
XPATHS = {
    "product-links": "//div[@class='product-container']/div/a/@href",
    "product-name": "//h1[@itemprop='name']/text()",
    "product-category": "",
    "product-img-url": "(//img[@itemprop='image']/@src)[__ITER__]",
    "product-description": "//div[@itemprop='description']//p/text()",
    "product-price-3": "(//span[@class='price']/text())[3]",
    "product-price-1": "(//span[@class='price']/text())[1]",
    "product-prev-price": "(//span[@class='price']/text())[2]",
    "sizes": "//span[@class='units_container']/span/text()",
}
