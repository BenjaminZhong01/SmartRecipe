
from lxml import etree
import requests
from urllib.request import urlopen 
from bs4 import BeautifulSoup
import pandas as pd

def scripeIngredients(website):
    html = urlopen(website)
    bsyc = BeautifulSoup(html.read(), "lxml")
    # find all of the line match the tag name and class name
    select_xml = bsyc.find_all('ol', 'wprm-recipe-instructions')
    fout.write(str(select_xml))
    instructions = []
    for i in select_xml:
        recipe_length = len(str(website[28:]).strip('/').strip('"'))
        recipe = BeautifulSoup(str(i), 'xml')
        instruction = recipe.find_all('div', 'wprm-recipe-instruction-text')
        for j in instruction:
            list = []
            list.append(str(website[28:]).strip('/').strip('"'))
            list.append(j.get_text())
            instructions.append(list)
        
    # print(instructions)
    if len(instructions):
        df1 = pd.DataFrame(instructions, columns=[
                           'Recipe'.ljust(recipe_length), 'Instruction'])
        print(df1)
        df1.to_csv('cleaned_instructions.txt', sep='\t', index=None, header=True, mode='a')
    return 

def ScrapingCookbook(url):
    r = requests.get(url)
    content = etree.HTML(r.content)
    html_data = content.xpath('//div[@class="archiverecipe"]/a/@href')
    return html_data

if __name__ == '__main__':
    url = "https://www.101cookbooks.com/archives.html#100+%20Vegetarian%20Recipes"
    zrj = 3265
    websites = ScrapingCookbook(url)[zrj:4000]
    fout = open('bsyc.txt', 'a', encoding='utf-8')
    time = zrj
    for i in websites:
        scripeIngredients(i)
        time += 1
        print(time)
    fout.close()
