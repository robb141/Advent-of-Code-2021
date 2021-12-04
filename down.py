import requests
import browser_cookie3
from datetime import datetime
import sys
import os

day = sys.argv[1] if len(sys.argv) > 1 else datetime.today().strftime('%d')

if os.path.exists(f'{day}.txt'):
    pass
else:
    url = f'https://adventofcode.com/2021/day/{int(day)}/input'
    cj = browser_cookie3.chrome()

    r = requests.get(url, allow_redirects=True, cookies=cj)
    with open(f'{day}.txt', 'w') as f:
        f.write(r.text)
