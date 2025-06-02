import requests
import execjs
import time
import json

cookies = {
  // 你的cookie
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.mashangpa.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.mashangpa.com/problem-detail/16/',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
with open('16.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
ctx = execjs.compile(js_code)
t = int(time.time() * 1000)
h5 = ctx.call('get_sign', 3, t)

response = requests.post('https://www.mashangpa.com/api/problem-detail/16/data/', cookies=cookies, headers=headers, data=json.dumps(h5))
print(response.json()['current_array'])
