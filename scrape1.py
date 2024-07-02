import requests
from bs4 import BeautifulSoup

def fetch_market_summary():
    url = 'https://www.moneycontrol.com/markets/indian-indices/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    market_summary = {}
    
    # Find the sections that contain the market indices
    market_sections = soup.find_all('div', class_='IND')
    for section in market_sections:
        # Check for Nifty 50 link
        nifty = section.find('a', {'title': 'Nifty 50'})
        if nifty:
            index_value = section.find('span', {'id': 'sp_val'})
            change = section.find('span', {'id': 'sp_chg'})
            change_percent = section.find('span', {'id': 'sp_perchg'})
            if index_value and change and change_percent:
                market_summary['Nifty'] = {
                    'index_name': 'Nifty 50',
                    'index_value': index_value.text.strip(),
                    'change': change.text.strip(),
                    'change_percent': change_percent.text.strip()
                }
        
        # Check for BSE Sensex link
        sensex = section.find('a', {'title': 'BSE Sensex'})
        if sensex:
            index_value = section.find('span', {'id': 'sp_val'})
            change = section.find('span', {'id': 'sp_chg'})
            change_percent = section.find('span', {'id': 'sp_perchg'})
            if index_value and change and change_percent:
                market_summary['Sensex'] = {
                    'index_name': 'BSE Sensex',
                    'index_value': index_value.text.strip(),
                    'change': change.text.strip(),
                    'change_percent': change_percent.text.strip()
                }
    
    return market_summary

# Test the function
if __name__ == "__main__":
    market_summary = fetch_market_summary()
    if market_summary:
        print("Market Summary:")
        for index, data in market_summary.items():
            print(f"{index} Index")
            for key, value in data.items():
                print(f"{key}: {value}")
            print()
    else:
        print("No market summary data available.")