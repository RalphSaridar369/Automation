import requests
from bs4 import BeautifulSoup
import smtplib
import time

def send_mail_Gmail(ConvertedPrice):

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('insert Email to send from','password')

    subject= 'Price Fell Down'
    body = ConvertedPrice
    msg= f"Check the prices for {TitleConverted} \n\n\n its  {PriceConverted}"


    server.sendmail(
        'insert Email to send from','insert Email to send to',msg
    )

    server.quit()

url="https://www.ebay.com/itm/playstation-5-digital-edition-PS5-BRAND-NEW-UNOPENED/174547366170?hash=item28a3d5711a:g:NVIAAOSwkK5fzCEv"

#google 'User agent' copy and paste it below

header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.400 (Edition Campaign 34)"}

page = requests.get(url,headers=header)
soup = BeautifulSoup(page.content,'html.parser')

Title = soup.find(id="CenterPanelInternal").find(id="LeftSummaryPanel").find(class_='vi-swc-lsp').findChild().\
    findChild().get_text()

TitleConverted = Title[16:len(Title)]

    #.find(class_="ucb").findAll[1]('div').findChild().get_text()
Price = soup.find(id="CenterPanelInternal").find(id="LeftSummaryPanel").findChild().\
    findNextSibling().find('form').findAll('div')[0].findNextSibling().findChild().\
    findChild().findNextSibling().findChild().findNextSibling().findChild().get_text()

PriceConverted= int(Price[4:7])

print(TitleConverted,"\nUS $   ",PriceConverted)


if(PriceConverted>800):
    send_mail_Gmail(PriceConverted)