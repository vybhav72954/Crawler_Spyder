import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Poppie.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# get user input for how many times to search
count = int(input('Enter count: '))

# get user input for which url to click on
position = int(input('Enter position: '))-1

while count >= 0:
    # re-reads the current url
    html = urllib.request.urlopen(url, context=ctx).read()
    # creates a new soup object
    soup = BeautifulSoup(html, 'html.parser')
    # searches the page for all <a> tags
    tags = soup('a')
    print("Retrieving: ", url)
    # upates the current url
    url = tags[position].get("href", None)
    count = count - 1
