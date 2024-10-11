# import requests
# url = 'https://ip.smartproxy.com/json'
# proxy = '89.42.81.219:12323'
# # proxy = 'gate.smartproxy.com:15555'
# username = '14a51f7dce1cf'
# password = 'e041b7ba43'

# proxies = {
#     'http': f'http://{username}:{password}@{proxy}',
#     'https': f'http://{username}:{password}@{proxy}'
# }

# response = requests.get(url, proxies=proxies)
# print(response.json())

from seleniumwire import webdriver

# Selenium Wire configuration to use a proxy
PROXY_USERNAME = "14a51f7dce1cf"
PROXY_PASSWORD = "e041b7ba43"
PROXY_HOST = "89.42.81.219"
PROXY_PORT = "12323"
seleniumwire_options = {
    'proxy': {
        'http': f'http://{PROXY_USERNAME}:{PROXY_PASSWORD}@{PROXY_HOST}:{PROXY_PORT}',
        'verify_ssl': False,
    },
}

driver = webdriver.Chrome(seleniumwire_options=seleniumwire_options)


driver.get('http://www.google.com')
