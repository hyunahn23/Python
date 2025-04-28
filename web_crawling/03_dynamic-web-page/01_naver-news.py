# 동적 페이지 웹 스크래핑 <- selenium
# 동적 페이지 : 요청한 URL에서 응답받은 HTML 안의 JS를 실행해 HTML을 새로 만든 경우 (Client Side Rendering)

# Selenium
# - 인증을 요구하는 특정 웹 페이지의 데이터 스크랩a
# - 무한 댓글 스크랩
# - 브라우저용 매크로로써 사용 가능

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 1. chrome 실행
# path = 'chromedriver.exe'
# service = webdriver.chrome.service.Service(path)
# driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome()

# 2. 특정 url 접근
# driver.get('https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=chat+gpt')
driver.get('https://naver.com')
time.sleep(1)

# 3. 검색 처리
search_box = driver.find_element(By.ID, "query") 
search_box.send_keys('뉴진스')
search_box.send_keys(Keys.RETURN)
time.sleep(1)

# - 뉴스 탭 이동
news_btn = driver.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[8]/a')
news_btn.click()
time.sleep(1)


# 4. 스크롤 처리
for _ in range(5):
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.END)
    time.sleep(1)
 

# 5. 특정 요소에 접근
news_contents_elems = driver.find_elements(By.CSS_SELECTOR, ".news_contents")
print(len(news_contents_elems))

for news_contents_elem in news_contents_elems:
    # print(news_contents_elem)
    # print(type(news_contents_elem))
    a_tag = news_contents_elem.find_element(By.CSS_SELECTOR, ".news_tit")
    title = a_tag.text
    href = a_tag.get_attribute('href')
    print(title, '|', href)

driver.quit()