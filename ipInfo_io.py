import requests

SESSION = requests.Session()

SESSION.headers.update({
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-IN;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'cookie': 'flash=; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%229328da08-463a-4c74-ae75-6980e8923247%22; _gid=GA1.2.639856530.1671740281; __stripe_mid=b034eaa7-1a8d-4753-893d-935f522d9b87b617de; _ga_RWP85XL4SC=GS1.1.1671747635.5.0.1671747635.60.0.0; _ga=GA1.2.938640176.1669869064; _gat_UA-2336519-21=1',
    'referer': 'https://ipinfo.io/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
})

def get_ip_info(ip_address):
    SESSION.headers.update({
        'x-forwarded-for': f'{ip_address}',
    })
    url = f'https://ipinfo.io/widget/demo/{ip_address}'
    response = SESSION.get(url)
    return response.json()
