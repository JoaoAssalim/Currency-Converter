from bs4 import BeautifulSoup 
import requests
import pyfiglet 


ascii_banner = pyfiglet.figlet_format("CURRENCY CONVERTER") 
print(ascii_banner) 

def dollar(amount):
    HTML = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=BRL")
    soup = BeautifulSoup(HTML.text, 'html.parser')
    dollar = soup.find("p", attrs={'class':'result__BigRate-sc-1bsijpp-1 iGrAod'}).text

    return float(dollar[0:4]) * amount

def cad(amount):
    HTML = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=CAD&To=BRL")
    soup = BeautifulSoup(HTML.text, 'html.parser')
    cad = soup.find("p", attrs={'class':'result__BigRate-sc-1bsijpp-1 iGrAod'}).text

    return float(cad[0:4]) * amount

def eur(amount):
    HTML = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=BRL")
    soup = BeautifulSoup(HTML.text, 'html.parser')
    eur = soup.find("p", attrs={'class':'result__BigRate-sc-1bsijpp-1 iGrAod'}).text

    return float(eur[0:4]) * amount

def gbp(amount):
    HTML = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=GBP&To=BRL")
    soup = BeautifulSoup(HTML.text, 'html.parser')
    gbp = soup.find("p", attrs={'class':'result__BigRate-sc-1bsijpp-1 iGrAod'}).text

    return float(gbp[0:4]) * amount

def ars(amount):
    HTML = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=ARS&To=BRL")
    soup = BeautifulSoup(HTML.text, 'html.parser')
    ars = soup.find("p", attrs={'class':'result__BigRate-sc-1bsijpp-1 iGrAod'}).text

    return float(ars[0:4]) * amount

print('-='*40)

amount = input('How many do you want to convert to BRL: ')

print('-='*40)

if amount.isdigit():
    amount = float(amount)

    print(f'''
    USD - {dollar(amount):.2f}
    CAD - {cad(amount):.2f}
    EUR - {eur(amount):.2f}
    GBP - {gbp(amount):.2f}
    ARS - {ars(amount):.2f}
    ''')

else:
    print('EEnter an integer number!')
