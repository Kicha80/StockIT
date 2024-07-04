import requests
from bs4 import BeautifulSoup

def get_market_data():
    url = "https://finance.yahoo.com/quote/%5EIXIC?p=%5EIXIC"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the element that contains the market data
    market_data = soup.find('div', {'id': 'quote-header-info'})
    if market_data:
        name = market_data.find('h1').text
        price = market_data.find('span', {'data-reactid': '14'}).text
        change = market_data.find('span', {'data-reactid': '16'}).text
        print(f"Name: {name}")
        print(f"Price: {price}")
        print(f"Change: {change}")
    else:
        print("Could not find market data")

get_market_data()