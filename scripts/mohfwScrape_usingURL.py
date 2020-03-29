#python script to get the data.
import bs4
import codecs
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
stats_url = 'https://www.mohfw.gov.in/'
uClient = uReq(stats_url)
page_html = uClient.read()
uClient.close()
#page_html = codecs.open('stats.html','r','utf-8')
page_soup = soup(page_html,"html.parser")
# table_html = page_soup.table
table_div = page_soup.find('div',{'class':'newtab'})
table_html = table_div.find('table',{'class':'table'})
# print(table_html)
table = table_html
headings = [th.get_text() for th in table_html.find("tr").find_all("th")]
#print(headings)
datasets = []
for row in table.find_all("tr")[1:]:
    dataset = dict(zip(headings, (td.get_text() for td in row.find_all("td"))))
    datasets.append(dataset)

def scrapeData(headings, datasets):
    # For printing out headings
    for j in range(1, len(headings)):
        if j == len(headings) - 1:
            print(headings[j])
        else:
            print(headings[j], end = " | ")

    print("------- | -- | -- | --")

    for i in range(len(datasets) - 1):
        for k in range(1, len(headings)):
            if k == len(headings) - 1:
                print(datasets[i][headings[k]])
            else:
                print(datasets[i][headings[k]], end = " | ")

scrapeData(headings, datasets)
