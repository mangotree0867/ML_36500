import csv
import requests

url = 'https://min-api.cryptocompare.com/data/v2/histominute'

params = {
    'fsym': 'BTC',      # From symbol (Bitcoin)
    'tsym': 'USD',      # To symbol (US Dollar)
    'limit': 2000,      # Maximum number of data
    'aggregate': 1,     # Interval 1min
    'api_key': '6bd78243689fbb635cd376fd6247d7e380465eef7e0fa753e8c02e341f6e579a'       # **To safeguard my API call counts, I deleted my API key ***
}

response = requests.get(url, params=params)
data = response.json()

##SMA7
sma7 = sum([data['Data']['Data'][i]['close'] for i in range(0, 7)]) / 7
for i in range(7, len(data['Data']['Data'])):
    sma7 = (sma7 * 6 + data['Data']['Data'][i]['close']) / 7
    data['Data']['Data'][i]['sma7'] = sma7

##SMA25
sma25 = sum([data['Data']['Data'][i]['close'] for i in range(0, 25)]) / 25
for i in range(25, len(data['Data']['Data'])):
    sma25 = (sma25 * 24 + data['Data']['Data'][i]['close']) / 25
    data['Data']['Data'][i]['sma25'] = sma25

##SMA50
sma50 = sum([data['Data']['Data'][i]['close'] for i in range(0, 50)]) / 50
for i in range(50, len(data['Data']['Data'])):
    sma50 = (sma50 * 49 + data['Data']['Data'][i]['close']) / 50
    data['Data']['Data'][i]['sma50'] = sma50

##EMA7
ema7 = sum([data['Data']['Data'][i]['close'] for i in range(0, 7)]) / 7
prev_ema7 = ema7
for i in range(7, len(data['Data']['Data'])):
    ema7 = (2 * data['Data']['Data'][i]['close'] + 6 * prev_ema7) / 8 if prev_ema7 is not None else None
    data['Data']['Data'][i]['ema7'] = ema7
    prev_ema7 = ema7

##EMA25
ema25 = sum([data['Data']['Data'][i]['close'] for i in range(0, 25)]) / 25
prev_ema25 = ema25
for i in range(25, len(data['Data']['Data'])):
    ema25 = (2 * data['Data']['Data'][i]['close'] + 24 * prev_ema25) / 26 if prev_ema25 is not None else None
    data['Data']['Data'][i]['ema25'] = ema25
    prev_ema25 = ema25

##EMA50
ema50 = sum([data['Data']['Data'][i]['close'] for i in range(0, 50)]) / 50
prev_ema50 = ema50
for i in range(50, len(data['Data']['Data'])):
    ema50 = (2 * data['Data']['Data'][i]['close'] + 49 * prev_ema50) / 51 if prev_ema50 is not None else None
    data['Data']['Data'][i]['ema50'] = ema50
    prev_ema50 = ema50

with open('bitcoin_prices6.csv', mode='w', newline='') as csv_file:
    fieldnames = ['timestamp', '-1min', 'sma7', 'sma25', 'sma50', 'ema7', 'ema25', 'ema50', 'close']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for i, row in enumerate(data['Data']['Data']):
        writer.writerow({
            'timestamp': row['time'],
            '-1min': data['Data']['Data'][i-1]['close'] if i >= 1 else '',
            'sma7': row['sma7'] if 'sma7' in row else '',
            'sma25': row['sma25'] if 'sma25' in row else '',
            'sma50': row['sma50'] if 'sma50' in row else '',
            'ema7': row['ema7'] if 'ema7' in row else '',
            'ema25': row['ema25'] if 'ema25' in row else '',
            'ema50': row['ema50'] if 'ema50' in row else '',
            'close': row['close']
        })

print('Bitcoin historical closing prices saved to bitcoin_prices6.csv')