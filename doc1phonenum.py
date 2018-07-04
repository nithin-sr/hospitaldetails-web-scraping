import requests
import bs4
import csv
from datetime import datetime

headers = {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36'}
url = 'https://health.usnews.com/doctors/nathan-zziwambazza-350685'
html_content = requests.get(url, headers=headers)
html_content.status_code
soup = bs4.BeautifulSoup(html_content.text, 'lxml')
#print(soup.prettify())
name_box = soup.find('div', attrs={'class':'padding-top-normal'}).find('div', attrs={'class':''})#.find('div',attrs={'class':''})
#name_box = soup.find('')
name = name_box.text
print(name)
with open('doc1.csv','a') as csv_file:
  writer = csv.writer(csv_file)
  writer.writerow([name])