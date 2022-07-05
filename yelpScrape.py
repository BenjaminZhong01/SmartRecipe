import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common import exceptions as ex

import re
import pandas as pd

chrome_options = webdriver.ChromeOptions()
# 使用headless无界面浏览器模式
# chrome_options.add_argument('--headless')
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "none"
print("a")


chrome_options.add_argument('--disable-gpu')
driver_Create = webdriver.Chrome()
# print("a")

#df = pd.DataFrame(columns=['Area','Name', 'href'])
df = pd.DataFrame(columns=['Name', 'href'])
area = ['New%20York%20City','Manhattan','Brooklyn','Queens','The%20Bronx','Staten%20Island']



for i in range (0,231,10):
    web = "https://www.yelp.com/search?cflt=restaurants&find_loc=New%20York%20city&start="+str(i)
    driver_Create.get(web)
    time.sleep(5)
    print("a")
    driver_Create.implicitly_wait(50)

    for j in range(9, 19):
        path = "//*[@id='main-content']/div/ul/li[" + str(j) + "]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/h4/span/a"

        try:
            res_list = driver_Create.find_element_by_xpath(path)
            name = res_list.get_attribute("name")
            link = res_list.get_attribute("href")
            content = {'Name': name, 'href': link}
            df = df.append([content], ignore_index=True)
        except ex.StaleElementReferenceException:
            print("abnoram element")
            res_list = driver_Create.find_element_by_xpath(path)
            name = res_list.get_attribute("name")
            link = res_list.get_attribute("href")
            content = {'Name': name, 'href': link}
            df = df.append([content], ignore_index=True)


    df.to_csv('res list.csv', encoding='utf-8')
    time.sleep(10)



print("d")


