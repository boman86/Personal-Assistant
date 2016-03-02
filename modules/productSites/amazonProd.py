from bs4 import BeautifulSoup
import urllib
from Product import *

# given us a product object,

def initQuery(product):
    productName = urllib.quote(product.productName)
    url = "http://camelcamelcamel.com/search?sq=" + productName

    # load the url
    r = urllib.urlopen("http://camelcamelcamel.com/search?sq=" + productName).read()
    soup = BeautifulSoup(r)

    # find top queried item list
    itemsoup = soup.find(id="products_list")
    listItems = []
    for item in itemsoup.find_all('tr'):
        listItems.append(item.find('div').text)

    # update Product object
    product.addSiteName("amazon")
    product.addHomepage("http://camelcamelcamel.com")
    product.addQuerypage(url)
    product.addItemList(listItems)

    product.debug()


initQuery(Product("Sperry Topsider"))