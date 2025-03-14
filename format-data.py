import os
import json

# Define the directory containing the JSON files
directory_path = 'data'
filtered_data_directory = 'filtered_data'
os.makedirs(filtered_data_directory, exist_ok=True)


# Loop through all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.json'):
        file_path = os.path.join(directory_path, filename)
        
        # Open and read the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)
            expirations = data.get('data').get('expirations')
            prices = data.get('data').get('prices')
            # loop expirations
            res = {}
            for expiration in expirations:
                symbol = expiration.get('symbol')
                res[symbol] = {
                    'expirationDate': expiration.get('expirationDate'),
                    'month': expiration.get('month'),
                }

            # find the latest price for each symbol and write into object above
            for price in prices:
                symbol = price.get('index_symbol')
                if symbol not in res:
                    res[symbol] = {}
                if 'price' not in res[symbol] or res[symbol]['price'] is None:
                    res[symbol]['price'] = price.get('price')
                    res[symbol]['price_time'] = price.get('price_time')
                else:
                    if price.get('price_time') > res[symbol].get('price_time'):
                        res[symbol]['price'] = price.get('price')
                        res[symbol]['price_time'] = price.get('price_time')
            print(res)
            file_path = os.path.join(filtered_data_directory, f'formatted_{filename}.json')
            with open(file_path, 'w') as file:
                json.dump(res, file, indent=4)
        