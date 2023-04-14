import csv
import requests

url = 'https://min-api.cryptocompare.com/data/v2/histominute'

params = {
    'fsym': 'BTC',      # From symbol (Bitcoin)
    'tsym': 'USD',      # To symbol (US Dollar)
    'limit': 2000,      # Maximum number of data
    'aggregate': 1,     # Interval 1min
    'api_key': 'eaf45a319280874c05640ef522698d8db46fd612e723631920ffd4a540552f4f'       # **To safeguard my API call counts, I deleted my API key ***
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

##SMA25  //-1min
prev_sma25 = None
for i in range(25, len(data['Data']['Data'])):
    if prev_sma25 is None:
        sma25 = sum([data['Data']['Data'][i-j]['close'] for j in range(0, 25)]) / 25
    data['Data']['Data'][i]['sma25'] = sma25
    prev_sma25 = sma25

##SMA50  //-1min
prev_sma50 = None
for i in range(50, len(data['Data']['Data'])):
    if prev_sma50 is None:
        sma50 = sum([data['Data']['Data'][i-j]['close'] for j in range(0, 50)]) / 50
    data['Data']['Data'][i]['sma50'] = sma50
    prev_sma50 = sma50

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

##EMA25  //-1min
prev_ema25 = None
for i in range(25, len(data['Data']['Data'])):
    if i-24 < 0:
        ema25 = None
    elif prev_ema25 is None:
        ema25 = sum([data['Data']['Data'][j]['close'] for j in range(i-24, i+1)]) / 25
    else:
        ema25 = (2 * data['Data']['Data'][i]['close'] + 24 * prev_ema25) / 26
    data['Data']['Data'][i]['ema25'] = ema25
    prev_ema25 = ema25

##EMA25  //-1min
prev_ema50 = None
for i in range(50, len(data['Data']['Data'])):
    if i-49 < 0:
        ema50 = None
    elif prev_ema50 is None:
        ema50 = sum([data['Data']['Data'][j]['close'] for j in range(i-49, i+1)]) / 50
    else:
        ema50 = (2 * data['Data']['Data'][i]['close'] + 49 * prev_ema25) / 51
    data['Data']['Data'][i]['ema50'] = ema50
    prev_ema50 = ema50

with open('bitcoin_prices5.csv', mode='w', newline='') as csv_file:
    fieldnames = ['timestamp', '-1min', 'sma7', 'sma25', 'sma50', 'ema7', 'ema25', 'ema50', 'price']
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
            'price': row['close']
        })

print('Bitcoin historical closing prices saved to bitcoin_prices5.csv')