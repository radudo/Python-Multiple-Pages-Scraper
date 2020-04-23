from bs4 import BeautifulSoup
import requests
url = 'https://scrapingclub.com/exercise/list_basic/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
count = 1
for i in items:
    #Strip is used to trim / parse the conent 
    itemName = i.find('h4', class_='card-title').text.strip('\n')
    itemPrice = i.find('h5').text
    print(' %s ) Item Name: %s, Price: %s' % (count, itemName, itemPrice))
    count = count + 1
#Next Pages Scraping
pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')
for link in links:
    #check if Link is number
    pageNum = int(link.text) if link.text.isdigit() else None
    #If page number is digit add link to url list
    if pageNum != None:
        x = link.get('href')
        #add url to list
        urls.append(x)
for i in urls:
    newUrl = url + i
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for i in items:
        #Strip is used to trim / parse the conent 
        itemName = i.find('h4', class_='card-title').text.strip('\n')
        itemPrice = i.find('h5').text
        print(' %s) Item Name: %s, Price: %s' % (count, itemName, itemPrice))
        count = count + 1