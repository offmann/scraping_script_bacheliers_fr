#!/usr/bin/python3

import requests
import lxml.html as lh
import csv

url_base = 'https://ocean.ac-lille.fr/publinet/resultats?previousIdBaseSession=pub_10&actionId=6'

page = requests.get(url_base)

doc = lh.fromstring(page.content)

ul_elements = doc.xpath('//ul')


for alpha in ul_elements:
        letters = list(alpha.text_content())

lista = []
for letter in letters:
        url_alpha = url_base+'&valCriLettre='+letter
        page_alpha = requests.get(url_alpha)
        doc_alpha = lh.fromstring(page_alpha.content)
        tr_elements = doc_alpha.xpath('//tr')
        for element in tr_elements:
                lista.append(element.text_content())

with open('output.csv','wb') as resultFile:
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerows(lista)

