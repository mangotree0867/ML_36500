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

with open('bitcoin_prices3.csv', mode='w', newline='') as csv_file:
    fieldnames = ['timestamp', '-1min', 'MA7', 'MA25', 'MA50', 'price']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for i, row in enumerate(data['Data']['Data']):
        writer.writerow({
            'timestamp': row['time'],
            '-1min': data['Data']['Data'][i-1]['close'] if i >= 1 else '',

            'MA7': (data['Data']['Data'][i-1]['close']+data['Data']['Data'][i-2]['close']
                    +data['Data']['Data'][i-3]['close']+data['Data']['Data'][i-4]['close']
                    +data['Data']['Data'][i-5]['close']+data['Data']['Data'][i-6]['close']
                    +data['Data']['Data'][i-7]['close'])/7 if i >= 7 else '',

            'MA25': (data['Data']['Data'][i-1]['close']+data['Data']['Data'][i-2]['close']
                     +data['Data']['Data'][i-3]['close']+data['Data']['Data'][i-4]['close']
                     +data['Data']['Data'][i-5]['close']+data['Data']['Data'][i-6]['close']
                     +data['Data']['Data'][i-7]['close']+data['Data']['Data'][i-8]['close']
                     +data['Data']['Data'][i-9]['close']+data['Data']['Data'][i-10]['close']
                     +data['Data']['Data'][i-11]['close']+data['Data']['Data'][i-12]['close']
                     +data['Data']['Data'][i-13]['close']+data['Data']['Data'][i-14]['close']
                     +data['Data']['Data'][i-15]['close']+data['Data']['Data'][i-16]['close']
                     +data['Data']['Data'][i-17]['close']+data['Data']['Data'][i-18]['close']
                     +data['Data']['Data'][i-19]['close']+data['Data']['Data'][i-20]['close']
                     +data['Data']['Data'][i-21]['close']+data['Data']['Data'][i-22]['close']
                     +data['Data']['Data'][i-23]['close']+data['Data']['Data'][i-24]['close']
                     +data['Data']['Data'][i-25]['close'])/25 if i >= 25 else '',

            'MA50': (data['Data']['Data'][i-1]['close']+data['Data']['Data'][i-2]['close']
                    +data['Data']['Data'][i-3]['close']+data['Data']['Data'][i-4]['close']
                    +data['Data']['Data'][i-5]['close']+data['Data']['Data'][i-6]['close']
                    +data['Data']['Data'][i-7]['close']+data['Data']['Data'][i-8]['close']
                    +data['Data']['Data'][i-9]['close']+data['Data']['Data'][i-10]['close']
                    +data['Data']['Data'][i-11]['close']+data['Data']['Data'][i-12]['close']
                    +data['Data']['Data'][i-13]['close']+data['Data']['Data'][i-14]['close']
                    +data['Data']['Data'][i-15]['close']+data['Data']['Data'][i-16]['close']
                    +data['Data']['Data'][i-17]['close']+data['Data']['Data'][i-18]['close']
                    +data['Data']['Data'][i-19]['close']+data['Data']['Data'][i-20]['close']
                    +data['Data']['Data'][i-21]['close']+data['Data']['Data'][i-22]['close']
                    +data['Data']['Data'][i-23]['close']+data['Data']['Data'][i-24]['close']
                    +data['Data']['Data'][i-25]['close']+data['Data']['Data'][i-26]['close']
                    +data['Data']['Data'][i-27]['close']+data['Data']['Data'][i-28]['close']
                    +data['Data']['Data'][i-29]['close']+data['Data']['Data'][i-30]['close']
                    +data['Data']['Data'][i-31]['close']+data['Data']['Data'][i-32]['close']
                    +data['Data']['Data'][i-33]['close']+data['Data']['Data'][i-34]['close']
                    +data['Data']['Data'][i-35]['close']+data['Data']['Data'][i-36]['close']
                    +data['Data']['Data'][i-37]['close']+data['Data']['Data'][i-38]['close']
                    +data['Data']['Data'][i-39]['close']+data['Data']['Data'][i-40]['close']
                    +data['Data']['Data'][i-41]['close']+data['Data']['Data'][i-42]['close']
                    +data['Data']['Data'][i-43]['close']+data['Data']['Data'][i-44]['close']
                    +data['Data']['Data'][i-45]['close']+data['Data']['Data'][i-46]['close']
                    +data['Data']['Data'][i-47]['close']+data['Data']['Data'][i-48]['close']
                    +data['Data']['Data'][i-49]['close']+data['Data']['Data'][i-50]['close']
                    )/50 if i >= 50 else '',
            'price': row['close']
        })

print('Bitcoin historical closing prices saved to bitcoin_prices3.csv')