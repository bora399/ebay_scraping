#This code includes scraping basics with an random ebay product.
#If you want to learn everything about web scraping with bs4 library, check out this link : https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#Made by bora399

import requests
from bs4 import BeautifulSoup as bs

def get_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = bs(response.text, 'lxml')
    else:
        quit()    
    return soup
    
def get_detail_data(soup):
    # title
    # price
    # items sold
    title = soup.find('h1',{"class":"x-item-title__mainTitle"}).find("span").text
    price = soup.find('span',id="prcIsum").text
    sold = soup.find('div',{"class":"w2b-cnt w2b-3 w2b-red"}).find("span",{"class":"w2b-head"}).text
    print("The title of the product :",title)
    print("The price of the product :",price)
    print("The number of sales :",sold)
    
def main():
    url = 'https://www.ebay.com/itm/402256288165?epid=9037162364&_trkparms=ispr%3D1&hash=item5da857d9a5:g:TV0AAOSw4ytetX0j&amdata=enc%3AAQAGAAAA4ICDlS4qbZDFU55%2FslgmdL2xTjywdBEECqIBKtZhTDtEikv%2F9g2UEi7%2BxRhU7vs2W6awOdNm3QYlZ4mD8VYUrrFqlZWrYuMyf2NFkCAzEiJXlfQsKVgfw1RqST%2FDEZoOsOTpgA9arpMHl0a2xHxH6r59zuMVQVoEdSOisaFXtjloYf2qR5wu7lMjfUip%2FX%2FdIeoWeXGNzwaHkIN8rsgKbCW0ZWQCapFw1Lx0DCmt1mIdaJev9Plkb9TY3rt9xl1kUxmmdO%2BYY%2BPqJ3yiyhy1NxVqV4RjTN9gV9pWepCsLmVq%7Ctkp%3ABFBM4r_qnIdg&var=672174687331'
    get_detail_data(get_page(url))
    
if __name__ == '__main__':
    main()