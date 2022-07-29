import requests
import json
import pandas as pd
from bs4 import BeautifulSoup


def fetch_cryptos_html():
    # make a request to the target website
    url = "https://cryptopunks.app/"
    r = requests.get(url)
    if r.status_code == 200:
        # if the request is successful return the HTML content
        return r.text
    else:
        # throw an exception if an error occurred
        raise Exception("an error occurred while fetching cryptopunks html")


def extract_info(doc):
    # parse the HTML content with Beautiful Soup
    soup = BeautifulSoup(doc, "html.parser")

    # find all the elements in collections table
    crypto_punks = soup.find_all("div", {"class": "col-flex col-md-2 col-sm-3 col-xs-6"})

    # iterate through the elements
    cryptos_list = []
    for punk in crypto_punks:
        # extract the information needed from our observation
        cryptos_list.append({
            "cryptos": punk.text.strip().replace("\n", " "),
            "image": punk.find("img")['src']
        })

    return cryptos_list


# fetch CryptoPunk's HTML content
html = fetch_cryptos_html()

# extract our data from the HTML document
cryptos = extract_info(html)

# save results to JSON file
with open("cryptos.json", "w") as f:
    f.write(json.dumps(cryptos, indent=2))


