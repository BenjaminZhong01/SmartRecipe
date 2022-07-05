# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 20:51:49 2021

@author: 15991
"""

import requests
from lxml import etree
def ScrapingCookbook(url):
    r = requests.get(url)
    content = etree.HTML(r.content)
    html_data = content.xpath('//div[@class="archiverecipe"]/a/@href')
    output = open('Recipes_Catalog.txt', 'w')
    for i in html_data:
        output.write(i+'\n')
    
if __name__ == '__main__':
    url = "https://www.101cookbooks.com/archives.html#100+%20Vegetarian%20Recipes"
    ScrapingCookbook(url)
   
