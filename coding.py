import requests
from bs4 import BeautifulSoup

url = 'https://www1.shoppersdrugmart.ca/en/Store-Locator/Listing'
r= requests.get(url)
soup = BeautifulSoup(r.content,'html.parser')

soup.find_all('span',class_='strloc-allstr-store-phone')
everything = soup.find_all('span',class_='strloc-allstr-store-phone')
details = {}
everyy = []
for i in everything:
	everyy.append(i.text)

details = {}
location = []
phone_num = []
for i in range(len(everyy)):
	if i % 2 != 0:
		location.append(everyy[i])
	else:
		phone_num.append(everyy[i])

details = {}
details = dict(zip(phone_num,location))
s = pd.Series(details)

