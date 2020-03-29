# this script need modification of few variables before getting the output
import math
import bs4
import codecs
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

xAxisData = []
yAxisData = []
for i in range(5): # change this value when you add a new table.md
    fileLink = str('./jekylldata/_site/0'+f'{i+1}'+'.html')
    page_html = codecs.open(fileLink,'r','utf-8')
    page_soup = soup(page_html,"html.parser")
    page_title = page_soup.title
    page_title_text = page_title.get_text()
    if page_title_text.endswith(' | Your awesome title'):
        page_title_text = page_title_text[:-21]
    yAxisData.append(page_title_text)
    table_html = page_soup.table
    table = table_html
    headings = [th.get_text() for th in table_html.find("tr").find_all("th")]
    datasets = []
    for row in table.find_all("tr")[1:]:
        dataset = dict(zip(headings, (td.get_text() for td in row.find_all("td"))))
        datasets.append(dataset)

    
    def nationalcounter(datasets):
        state_count = 0;
        national_count = 0;
        for i in range(len(datasets)):
            state_count = ((int(datasets[i][headings[1]]) + int(datasets[i][headings[2]])) - (int(datasets[i][headings[3]]) + (int(datasets[i][headings[4]]))) )
            national_count += state_count
        return national_count
    xAxisData.append(nationalcounter(datasets))


legendTitle ='Number Of Active Cases'
chartTitle = 'DATE-WISE ACTIVE CASES COMPARISON'
typeOfChart = 'bar'
axis = 'yAxes'


fixedColor = '#e87a74' # Here define the color of the bars
ifFixedColor = True

#used if random colours needed
def getRandomColor():
    letters = '0123456789ABCDEF'
    color = '#'
    for i in range(6):
        color += letters[math.floor(math.random() * 16)]
    return color

# generating color for no of bars
colorsGenerated = []
tempColor = ''
for i in range(len(yAxisData)):
    if ifFixedColor:
        tempColor = fixedColor
    else:
        tempColor = getRandomColor()
    colorsGenerated.append(tempColor)
