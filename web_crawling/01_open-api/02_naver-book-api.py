import urllib.request
import json
import mysql.connector

# API KEY
client_id = 'QhPoL12n7DWdVgE2Dng7'
client_secret = 'BUZRc7wQWK'

# 검색어
searchText = urllib.parse.quote('소나기')

# url 및 헤더 설정
url = 'https://openapi.naver.com/v1/search/book.json?query=' + searchText + '&display=100'
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

# API 요청 및 결과값 json 변환 (dictionary)
response = urllib.request.urlopen(request)
response_body = response.read()
response_body = json.loads(response_body)
# print(response_body)

book_list = response_body['items']

# DB 연결 객체 생성
connection = mysql.connector.connect(
    host="localhost",
    user="ohgiraffers",
    password="ohgiraffers",
    database="bookdb"
)

# sql 수행을 위한 cursor
cursor = connection.cursor()

sql = "INSERT INTO naver_book (book_title, book_image, author, publisher, isbn, book_description, pub_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"

# 받아온 정보만큼 sql 수행
for book_info in book_list:
    values = (book_info['title'], book_info['image'], book_info['author'],
              book_info['publisher'], str(book_info['isbn']), 
              book_info['description'], book_info['pubdate'])

    cursor.execute(sql, values)

# 데이터베이스 커밋 (반영)
connection.commit()

# cursor 및 연결 객체 종료(반납)
cursor.close()
connection.close()

