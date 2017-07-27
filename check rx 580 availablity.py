# To download the page
import requests

# parse the page
from bs4 import BeautifulSoup

# Delay between page refreshes
import time

# email notifications
import smtplib


def checkNcix():
    # Site for product
    url = "http://www.ncix.com/detail/gigabyte-radeon-rx-580-gaming-ce-140597.htm"
    
    # pretend we are browser
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    
    # download the url page
    response = requests.get(url, headers=headers)
    
    # parse the requested page
    soup = BeautifulSoup(response.text, "lxml")
    stock = getattr(soup.find('strong', attrs={'id': 'shipinginfo1'}), "text", 0)

    # check if available
    if stock == "Back Order":
        return 0
    else:
        return 1    

def checkDirectCan():
    
    # Site for product
    url = "http://www.directcanada.com/products/?sku=12981140545&vpn=RX%20580%20GAMING%20X%208G&manufacture=MSI"
    
    # pretend we are browser
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    
    # download the url page
    response = requests.get(url, headers=headers)
    
    # parse the requested page
    soup = BeautifulSoup(response.text, "lxml")
    stock = getattr(soup.find('span', attrs={'class': 'stock'}), "text", 0)
    
    # check if available
    if stock == "Not Available":
        return 0
    else:
        return 1


# check every 60 seconds
    
while True:

    if checkNcix():
        print("Check NCIX")
        break
    
    if checkDirectCan():
        print("Check Direct Canada")
        break

    print("nope")
    # wait 60 seconds
    time.sleep(60)
    
    
    
    
    
    
