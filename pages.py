import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.bbc.com/news',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'DNT': '1',
}

response = requests.get(URL, headers=headers)

parser = BeautifulSoup(response.text, 'html.parser')


header_div = parser.find("div" , id= "product-navigation-menu")
header_ul = header_div.find('ul' , attrs={"role" : "list"})
header_ul_list = header_ul.find_all('li')

for list in header_ul_list:
    print(list.text)





