# 정적 페이지 웹 스크래핑 -> requests, beautifulsoup
# 정적 페이지 : 요청한 url에서 응답받은 html을 그대로 사용한 경우 (Server Side Rendering)

import requests
from bs4 import BeautifulSoup

def web_request(url):
    response = requests.get(url)
    print(response)     # <Response [200]>
    print(response.status_code)     # 200 (응답코드드)
    print(response.text)        # html
    return response

# url = "https://www.naver.com"
# response = web_request(url)

with open('../html_sample.html', 'r', encoding='utf-8') as f:
    html = f.read()

bs = BeautifulSoup(html, 'html.parser')
# print(bs)
# print(type(bs))

def test_find():
    # find
    tag = bs.find('li')
    # print(tag)
    # print(type(tag))

    # find_all
    tags = bs.find_all('section', {'id': 'section1'})
    print(tags) 
    print(type(tags))

# test_find()

