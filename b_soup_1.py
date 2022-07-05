
from lxml import etree
import requests
from urllib.request import urlopen 
from bs4 import BeautifulSoup
import pandas as pd

def scripeIngredients(website):
    html = urlopen(website)
    bsyc = BeautifulSoup(html.read(), "lxml")
    select_xml = bsyc.find_all('li', 'wprm-recipe-ingredient') #find all of the line match the tag name and class name
    fout.write(str(select_xml))
    df = pd.DataFrame(columns=['Recipe','Amount','Unit','Ingredient'])
    recipes = []
    for i in select_xml:
        list = []
        recipe_length = len(str(website[28:]).strip('/').strip('"'))
        list.append(str(website[28:]).strip('/').strip('"'))
        recipe = BeautifulSoup(str(i), 'xml')
        try:
            amount = recipe.find('span', 'wprm-recipe-ingredient-amount')
            list.append(amount.get_text())
        except:
            list.append('')
        try:
            unit = recipe.find('span', 'wprm-recipe-ingredient-unit')
            list.append(unit.get_text())
        except:
            list.append('')
        try: 
            name = recipe.find('span', 'wprm-recipe-ingredient-name')
            list.append(name.get_text())
        except:
            list.append('')
        recipes.append(list)
    if len(recipes):
        df1 = pd.DataFrame(recipes, columns=['Recipe'.ljust(recipe_length), 'Amount', 'Unit', 'Ingredient'])
        print(df1)
        df1.to_csv('cleaned.txt', sep='\t', index=None, header=True, mode='a')
    return 

def ScrapingCookbook(url):
    r = requests.get(url)
    content = etree.HTML(r.content)
    html_data = content.xpath('//div[@class="archiverecipe"]/a/@href')
    return html_data

if __name__ == '__main__':
    url = "https://www.101cookbooks.com/archives.html#100+%20Vegetarian%20Recipes"
    a = 2016
    websites = ScrapingCookbook(url)[a:2200]
    fout = open('bsyc_temp.txt', 'a', encoding='utf-8')
    time = a
    for i in websites:
        scripeIngredients(i)
        time += 1
        print(time)
    fout.close()