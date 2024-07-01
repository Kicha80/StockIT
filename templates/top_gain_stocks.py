import requests
import csv
from io import StringIO

def get_stock_symbols(api_key, exchange):
    url = f'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={api_key}&exchange={exchange}'
    response = requests.get(url)
    if response.status_code == 200:
        # Convert CSV data to a list of dictionaries
        csv_data = response.text
        reader = csv.DictReader(StringIO(csv_data))
        data = list(reader)
        return data
    else:
        print(f"Error: Status code {response.status_code} received.")
        return None

# Example usage
api_key = 'NDUYYCPNO3KKHI71'
exchange = 'NSE'  # or 'BSE' for Bombay Stock Exchange
symbols_data = get_stock_symbols(api_key, exchange)
if symbols_data is not None:
    for stock in symbols_data:
        print(stock['symbol'], stock['name'], stock['exchange'])