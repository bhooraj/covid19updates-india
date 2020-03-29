# this script need modification of few variables before getting the output
# change the URL for calculating data of the particular date accordingly
import math
import bs4
import codecs
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

page_html = codecs.open('./jekylldata/_site/05.html','r','utf-8') # File name for this chart would be something like 'table_date_time'
page_soup = soup(page_html,"html.parser")
table_html = page_soup.table

table = table_html
headings = [th.get_text() for th in table_html.find("tr").find_all("th")]
#print(headings)
datasets = []
for row in table.find_all("tr")[1:]:
    dataset = dict(zip(headings, (td.get_text() for td in row.find_all("td"))))
    datasets.append(dataset)
# print(datasets)

legendTitle ='Number Of Active Cases On The Last Update*'
chartTitle = 'State-Wise Covid-19 Active Cases Comparison'.upper()
typeOfChart = 'horizontalBar'
axis = 'xAxes'

def generateYAxisValues(datasets):
    # Generating yAxisData
    yAxisData = []
    for i in range(len(datasets)):
        yAxisData.append(datasets[i][headings[0]])
    return yAxisData
# To use this var for colorGenerated list
yAxisData = generateYAxisValues(datasets)

def generateXAxisValues(datasets):
    # Generating xAxisData
    xAxisData = []
    for i in range(len(datasets)):
        xAxisData.append(((int(datasets[i][headings[1]]) + int(datasets[i][headings[2]])) - (int(datasets[i][headings[3]]) + (int(datasets[i][headings[4]]))) ))
    return xAxisData
xAxisData = generateXAxisValues(datasets)

fixedColor = '#666699' # Here define the color of the bars
ifFixedColor = True

#use if random colours needed
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

