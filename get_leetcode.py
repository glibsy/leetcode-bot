from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver

driver = webdriver.Chrome()

url = 'https://leetcode.com/problemset/all/'
html_doc = driver.get(url)


soup = BeautifulSoup(html_doc, 'html.parser')

tag = soup.find("div", class_="mx-[10px] grid grid-cols-7 text-xs text-label-3 dark:text-dark-label-3")

tag = tag.a


while tag != None:
    tag = tag.next_sibling
    print(tag)
    print()
