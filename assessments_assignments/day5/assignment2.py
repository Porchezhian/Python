import urllib.request as urllib
from bs4 import BeautifulSoup
import pymysql

companies_loss = {}
companies_gain = {}

def getcompanydata(type, stock):
    tables = []
    td = []
    companies = {}
    val = 0 if stock == "nifty" else 1
    r = urllib.urlopen('https://moneycontrol.com').read()
    soup = BeautifulSoup(r, 'lxml')
    divs = soup.find_all('table', attrs={'class': 'rhsglTbl'})
    for div in divs:
        for th in div.find_all('th'):
            if (th.get_text().strip() == type):
                tables.append(div)
    td.extend(tables[val].find_all('td'))
    for i in range(0, len(td), 4):
        companies[td[i].find('a').get_text()] = td[i + 3].get_text()
    return companies

def createtables(table, type):
    db = pymysql.connect("localhost", "root", "", "test")
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE {0} (
             NAME  CHAR(20) NOT NULL,
             {1} FLOAT )""".format(table, type))
    db.close()

def storedata(table, type, name, value):
    db = pymysql.connect("localhost", "root", "", "test")
    cursor = db.cursor()
    string = """INSERT INTO {0}(NAME,
         {1})
         VALUES ('{2}', '{3}')""".format(table, type, name, value)
    cursor.execute(string)
    db.commit()
    db.close()

createtables('top_gainers_nifty', 'GAIN')
createtables('top_gainers_sensex', 'GAIN')
createtables('top_losers_nifty', 'LOSS')
createtables('top_losers_sensex', 'LOSS')


companies_gain = getcompanydata('%Gain', "nifty")
for key, value in companies_gain.items():
    storedata('top_gainers_nifty', 'GAIN', key, value)

companies_gain = getcompanydata('%Gain', "sensex")
for key, value in companies_gain.items():
    storedata('top_gainers_sensex', 'GAIN', key, value)

companies_loss = getcompanydata('%Loss', "nifty")
for key, value in companies_loss.items():
    storedata('top_losers_nifty', 'LOSS', key, value)

companies_loss = getcompanydata('%Loss', "sensex")
for key, value in companies_loss.items():
    storedata('top_losers_sensex', 'LOSS', key, value)