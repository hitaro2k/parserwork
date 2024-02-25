from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('D:\chromedriver\chromedriver.exe')
driver = webdriver.Chrome(service=s)


driver.get('https://hh.ru/search/vacancy?text=python&ored_clusters=true&area=1&hhtmFrom=vacancy_search_list')

elements = driver.find_elements('span[data-qa="pager-page"]')

for element in elements:
    print(element.text)

driver.quit()
