import csv
import requests

url = 'https://min-api.cryptocompare.com/data/v2/histominute'

params = {
    'fsym': 'BTC',      # From symbol (Bitcoin)
    'tsym': 'USD',      # To symbol (US Dollar)
    'limit': 1440,      # Maximum number of data
    'aggregate': 1,     # Interval 1min
    'api_key': ''       # **To safeguard my API call counts, I deleted my API key ***
}

response = requests.get(url, params=params)
data = response.json()

with open('bitcoin_prices.csv', mode='w', newline='') as csv_file:
    fieldnames = ['timestamp', '-1min', '-2min', '-3min', '-4min', '-5min', '-6min', '-7min', 'MA7', 'price']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for i, row in enumerate(data['Data']['Data']):
        writer.writerow({
            'timestamp': row['time'],
            '-1min': data['Data']['Data'][i-1]['close'] if i >= 1 else '',
            '-2min': data['Data']['Data'][i-2]['close'] if i >= 2 else '',
            '-3min': data['Data']['Data'][i-3]['close'] if i >= 3 else '',
            '-4min': data['Data']['Data'][i-4]['close'] if i >= 4 else '',
            '-5min': data['Data']['Data'][i-5]['close'] if i >= 5 else '',
            '-6min': data['Data']['Data'][i-6]['close'] if i >= 6 else '',
            '-7min': data['Data']['Data'][i-7]['close'] if i >= 7 else '',
            'MA7': (data['Data']['Data'][i-1]['close']+data['Data']['Data'][i-2]['close']
                    +data['Data']['Data'][i-3]['close']+data['Data']['Data'][i-4]['close']
                    +data['Data']['Data'][i-5]['close']+data['Data']['Data'][i-6]['close']
                    +data['Data']['Data'][i-7]['close'])/7 if i >= 7 else '',
            'price': row['close']
        })

print('Bitcoin historical closing prices saved to bitcoin_prices.csv')