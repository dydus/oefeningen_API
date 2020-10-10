import requests
import urllib.parse
import xmltodict
import rauth
import xml.etree.ElementTree as ElementTree
from tabulate import tabulate


#variables
Input = ""
key = ""
book = ""
title = []
author = []

#processing
print ("Welk boek wil je opzoeken?")
book = input()
URL = ("https://www.goodreads.com/search.xml?key=" + key + "&q=" + urllib.parse.quote(book))
XML = requests.get(URL)
root = ElementTree.fromstring(XML.content)
for word in root.findall('.//best_book/title'):
    title.append(word.text)
for word in root.findall('.//best_book/author/name'):
    author.append(word.text)
table = (list(zip(title, author)))

#answer
if len(table) == 0:
    print("er zijn geen boeken gevonden met deze titel")
else:
    print(tabulate(table, headers=["title","author"]))