import csv
import requests
import os.path
from datetime import datetime, timedelta

url = 'https://min-api.cryptocompare.com/data/v2/histominute'

params = {
    'fsym': 'BTC',      # From symbol (Bitcoin)
    'tsym': 'USD',      # To symbol (US Dollar)
    'limit': 2000,      # Maximum number of data
    'aggregate': 1,     # Interval 1min
    'api_key': ''
}

filename = 'automation.csv'

if os.path.isfile(filename):
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)
    
    start_time = int(data[-1]['timestamp']) + 60

## modify parmas
params['toTs'] = int(datetime.now().timestamp())
params['limit'] = int((params['toTs'] - start_time) / 60)
params['limit'] = min(params['limit'], 2000)

response = requests.get(url, params=params)
new_data = response.json()['Data']['Data']

for row in new_data:
    row['time'] = str(row['time'])
    data.append(row)

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

with open(filename, 'w', newline='') as csv_file:
    fieldnames = ['timestamp', '-1min', 'ema7', 'ema25', 'ema50', 'sma7', 'sma25', 'sma50', 'close']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        new_row = {k: v for k, v in row.items() if k in fieldnames}
        writer.writerow(new_row)