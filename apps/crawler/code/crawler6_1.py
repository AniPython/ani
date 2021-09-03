import requests

data = requests.get("http://anipython.com/crawler/6/download_file").content

with open('temp.py', 'wb') as fp:
    fp.write(data)
