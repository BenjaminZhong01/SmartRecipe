import requests
from bs4 import BeautifulSoup

url='https://www.101cookbooks.com/archives.html#100+%20Vegetarian%20Recipes'
strhtml=requests.get(url)
soup=BeautifulSoup(strhtml.text,'lxml')
data = soup.select('//div[@class="archiverecipe"]/a/@href')
for i in data[0:4]:
    print(i)
    
    