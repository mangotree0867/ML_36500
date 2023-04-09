import csv
import requests

url = 'https://min-api.cryptocompare.com/data/v2/histominute'

params = {
    'fsym': 'BTC',      # From symbol (Bitcoin)
    'tsym': 'USD',      # To symbol (US Dollar)
    'limit': 2000,      # Maximum number of data
    'aggregate': 1,     # Interval 1min
    'api_key': ''       # **To safeguard my API call counts, I deleted my API key ***
}

response = requests.get(url, params=params)
data = response.json()

with open('bitcoin_prices4.csv', mode='w', newline='') as csv_file:
    fieldnames = ['timestamp', '-1min', 'price']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for i, row in enumerate(data['Data']['Data']):
        writer.writerow({
            'timestamp': row['time'],
            '-1min': data['Data']['Data'][i-1]['close'] if i >= 1 else '',
            'price': row['close']
        })

print('Bitcoin historical closing prices saved to bitcoin_prices4.csv')