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

##SMA7  //-1min
prev_sma7 = None
for i in range(7, len(data['Data']['Data'])):
    if prev_sma7 is None:
        sma7 = sum([data['Data']['Data'][i-j]['close'] for j in range(0, 7)]) / 7
    data['Data']['Data'][i]['sma7'] = sma7
    prev_sma7 = sma7

##EMA7  //-1min
prev_ema7 = None
for i in range(7, len(data['Data']['Data'])):
    if i-6 < 0:
        ema7 = None
    elif prev_ema7 is None:
        ema7 = sum([data['Data']['Data'][j]['close'] for j in range(i-6, i+1)]) / 7
    else:
        ema7 = (2 * data['Data']['Data'][i]['close'] + 6 * prev_ema7) / 8
    data['Data']['Data'][i]['ema7'] = ema7
    prev_ema7 = ema7


with open('bitcoin_prices5.csv', mode='w', newline='') as csv_file:
    fieldnames = ['timestamp', '-1min', 'sma7', 'ema7', 'price']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for i, row in enumerate(data['Data']['Data']):
        writer.writerow({
            'timestamp': row['time'],
            '-1min': data['Data']['Data'][i-1]['close'] if i >= 1 else '',
            'sma7': row['sma7'] if 'sma7' in row else '',
            'ema7': row['ema7'] if 'ema7' in row else '',
            'price': row['close']
        })

print('Bitcoin historical closing prices saved to bitcoin_prices5.csv')