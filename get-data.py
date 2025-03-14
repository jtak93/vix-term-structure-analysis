
import requests
import pandas as pd
from datetime import datetime, timedelta
import os

# Define the directory to save the JSON files
save_directory = 'data'

# Create the directory if it doesn't exist
os.makedirs(save_directory, exist_ok=True)

# List every day of the year
# List every day of the past year
end_date = datetime.now()
start_date = end_date - timedelta(days=2)
trading_dates = pd.date_range(start=start_date, end=end_date).tolist()

# Making a GET request for each date

for date in trading_dates:
    formatted_date = date.strftime('%Y-%m-%d')
    url = f'https://cdn.cboe.com/api/global/delayed_quotes/term_structure/2025/VIX_{formatted_date}.json'
    r = requests.get(url)

    # check status code for response received
    # success code - 200
    if r.status_code == 200:
        file_path = os.path.join(save_directory, f'VIX_{formatted_date}.json')
        with open(file_path, 'wb') as file:
            file.write(r.content)
    else:
        print(f"Failed to retrieve data for {formatted_date}")