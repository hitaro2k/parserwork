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


def main_page(eu, us , tech , ent , other):
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    main = soup.find("main", id="main-content")
    content = main.find_all("div", class_="ssrcss-p44stw-Container eqfxz1e7")

    seen_texts = set()  # Множество для хранения уникальных строк

    for lists in content:
        list = lists.find('ul', attrs={"role": "list"})
        list_items = list.find_all('li')
        for list_item in list_items:
            f = list_item.find("div", attrs={"data-testid": "promo"})
            list_links = list_item.find("a")
            if list_links is not None and f is not None:
                for text in f:
                    link = text.findAll("a")
                    for link_title in link:
                        textsa = text.text
                        if textsa not in seen_texts:
                            seen_texts.add(textsa)
                            elements = textsa.split()
                            last_two_elements = elements[-2:]
                            if "europe" in list_links.get('href'):
                                maket = {
                                    "data": last_two_elements[1],
                                    "title": list_links.text,
                                    "link": f"{URL}{list_links.get('href').replace('/news', '')}"
                                }
                                eu.append(maket)
                            elif "us" in list_links.get('href'):
                                maket = {
                                    "data": last_two_elements[1],
                                    "title": list_links.text,
                                    "link": f"{URL}{list_links.get('href').replace('/news', '')}"
                                }
                                us.append(maket)
                            elif "technology" in list_links.get('href'):
                                maket = {
                                    "data": last_two_elements[1],
                                    "title": list_links.text,
                                    "link": f"{URL}{list_links.get('href').replace('/news', '')}"
                                }
                                tech.append(maket)
                            elif "entertainment-arts" in list_links.get('href'):
                                maket = {
                                    "data": last_two_elements[1],
                                    "title": list_links.text,
                                    "link": f"{URL}{list_links.get('href').replace('/news', '')}"
                                }
                                ent.append(maket)
                            else:
                                maket = {
                                    "data": last_two_elements[1],
                                    "title": list_links.text,
                                    "link": f"{URL}{list_links.get('href').replace('/news', '')}"
                                }
                                other.append(maket)