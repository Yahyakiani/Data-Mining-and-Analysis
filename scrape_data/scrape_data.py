from utils.utils import *
import pandas as pd
import requests


def scrapped_data():
    print("\nScrapping the data....")
    columns = {
        "Name",
        "Brand",
        "Url",
        "Sizes",
        "Images",
        "Price",
        "Previous_Price",
        "Description",
    }
    df = pd.DataFrame(columns=columns)

    my_session = requests.session()
    for_cookies = my_session.get("https://www.snkrs.com")
    cookies = for_cookies.cookies
    headers = {
        "User-Agent": "Moziylla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0"
    }
    links = get_product_links(MISCS["Product-page-link"], my_session, headers, cookies)
    max_rows = 0

    for link in links:
        if max_rows >= 300:
            break
        print("\n\n\nExtracting data from {0}".format(link))

        (
            url,
            sizes,
            name,
            brand_name,
            images,
            price,
            prev_price,
            description,
        ) = extract_product_data(link, my_session, headers, cookies)

        df = df.append(
            {
                "Name": name,
                "Brand": brand_name,
                "Url": url,
                "Price": price,
                "Category": "Men Sneakers",
                "Sizes": sizes,
                "Description": description,
                "Previous_Price": prev_price,
                "Images": images,
            },
            ignore_index=True,
        )

        max_rows = max_rows + 1

    print(df.head())
