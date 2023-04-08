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

with open('bitcoin_prices2.csv', mode='w', newline='') as csv_file:
    fieldnames = ['timestamp', '-1min', '-2min', '-3min', '-4min', '-5min', '-6min', '-7min', '-8min', '-9min', '-10min', '-11min', '-12min', '-13min', '-14min', '-15min', '-16min', '-17min', '-18min', '-19min', '-20min', '-21min', '-22min', '-23min', '-24min', '-25min', '-26min', '-27min', '-28min', '-29min', '-30min', '-31min', '-32min', '-33min', '-34min', '-35min', '-36min', '-37min', '-38min', '-39min', '-40min', '-41min', '-42min', '-43min', '-44min', '-45min', '-46min', '-47min', '-48min', '-49min', '-50min', 'MA7', 'MA25', 'MA50', 'price']
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
            '-8min': data['Data']['Data'][i-8]['close'] if i >= 8 else '',
            '-9min': data['Data']['Data'][i-9]['close'] if i >= 9 else '',
            '-10min': data['Data']['Data'][i-10]['close'] if i >= 10 else '',
            '-11min': data['Data']['Data'][i-11]['close'] if i >= 11 else '',
            '-12min': data['Data']['Data'][i-12]['close'] if i >= 12 else '',
            '-13min': data['Data']['Data'][i-13]['close'] if i >= 13 else '',
            '-14min': data['Data']['Data'][i-14]['close'] if i >= 14 else '',
            '-15min': data['Data']['Data'][i-15]['close'] if i >= 15 else '',
            '-16min': data['Data']['Data'][i-16]['close'] if i >= 16 else '',
            '-17min': data['Data']['Data'][i-17]['close'] if i >= 17 else '',
            '-18min': data['Data']['Data'][i-18]['close'] if i >= 18 else '',
            '-19min': data['Data']['Data'][i-19]['close'] if i >= 19 else '',
            '-20min': data['Data']['Data'][i-20]['close'] if i >= 20 else '',
            '-21min': data['Data']['Data'][i-21]['close'] if i >= 21 else '',
            '-22min': data['Data']['Data'][i-22]['close'] if i >= 22 else '',
            '-23min': data['Data']['Data'][i-23]['close'] if i >= 23 else '',
            '-24min': data['Data']['Data'][i-24]['close'] if i >= 24 else '',
            '-25min': data['Data']['Data'][i-25]['close'] if i >= 25 else '',
            '-26min': data['Data']['Data'][i-26]['close'] if i >= 26 else '',
            '-27min': data['Data']['Data'][i-27]['close'] if i >= 27 else '',
            '-28min': data['Data']['Data'][i-28]['close'] if i >= 28 else '',
            '-29min': data['Data']['Data'][i-29]['close'] if i >= 29 else '',
            '-30min': data['Data']['Data'][i-30]['close'] if i >= 30 else '',
            '-31min': data['Data']['Data'][i-31]['close'] if i >= 31 else '',
            '-32min': data['Data']['Data'][i-32]['close'] if i >= 32 else '',
            '-33min': data['Data']['Data'][i-33]['close'] if i >= 33 else '',
            '-34min': data['Data']['Data'][i-34]['close'] if i >= 34 else '',
            '-35min': data['Data']['Data'][i-35]['close'] if i >= 35 else '',
            '-36min': data['Data']['Data'][i-36]['close'] if i >= 36 else '',
            '-37min': data['Data']['Data'][i-37]['close'] if i >= 37 else '',
            '-38min': data['Data']['Data'][i-38]['close'] if i >= 38 else '',
            '-39min': data['Data']['Data'][i-39]['close'] if i >= 39 else '',
            '-40min': data['Data']['Data'][i-40]['close'] if i >= 40 else '',
            '-41min': data['Data']['Data'][i-41]['close'] if i >= 41 else '',
            '-42min': data['Data']['Data'][i-42]['close'] if i >= 42 else '',
            '-43min': data['Data']['Data'][i-43]['close'] if i >= 43 else '',
            '-44min': data['Data']['Data'][i-44]['close'] if i >= 44 else '',
            '-45min': data['Data']['Data'][i-45]['close'] if i >= 45 else '',
            '-46min': data['Data']['Data'][i-46]['close'] if i >= 46 else '',
            '-47min': data['Data']['Data'][i-47]['close'] if i >= 47 else '',
            '-48min': data['Data']['Data'][i-48]['close'] if i >= 48 else '',
            '-49min': data['Data']['Data'][i-49]['close'] if i >= 49 else '',
            '-50min': data['Data']['Data'][i-50]['close'] if i >= 50 else '',

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

print('Bitcoin historical closing prices saved to bitcoin_prices2.csv')