from bs4 import BeautifulSoup
import requests
import time
import datetime
import pandas as pd
import csv

def check_price():
    URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1"
    }
    
    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    
    title = soup2.find(id='productTitle').get_text()
    price = soup2.find(id='priceblock_ourprice').get_text()
    
    price = price.strip()[1:]
    title = title.strip()
    
    today = datetime.date.today()
    
    data = [title, price, today]
    
    with open('Amazon_data.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

# Create CSV with headers
header = ['Title', 'Price', 'Date']
with open('Amazon_data.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)

# Run check_price after a set time and write data into CSV
while True:
    check_price()
    time.sleep(86400)  # Sleep for 24 hours

# Read and display CSV data
df = pd.read_csv('Amazon_data.csv')
print(df)
