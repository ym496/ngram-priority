import requests
import sys

words = sys.argv[1].split(',')
words_format = "%2C".join(words) 
url_to_fetch = f'https://books.google.com/ngrams/json?content={words_format}&year_start=1800&year_end=2019&corpus=en-2019&smoothing=3'
freq_list = []
try:
    response = requests.get(url_to_fetch)
    if response.status_code == 200:
        json_data = response.json()
        for i in json_data:
            name,timeseries = i['ngram'], i['timeseries'][-1]
            freq_list.append((name,timeseries))
    else:
        print("Error")

except Exception as e:
    print(f"Error")

sorted_freq_list = sorted(freq_list,key=lambda x: x[1], reverse=True)
for i,(name,freq) in enumerate(sorted_freq_list, start=1):
    print(f"{i}. {name}")
