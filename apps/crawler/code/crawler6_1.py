import requests

host = 'http://127.0.0.1:8000'
data = requests.get(f"{host}/crawler/6/download_file").content

with open('temp.py', 'wb') as fp:
    fp.write(data)
