import urllib.request

# API 호출을 위한 client_id, client_secret 변수 설정
client_id = 'QhPoL12n7DWdVgE2Dng7'
client_secret = 'BUZRc7wQWK'

encText = urllib.parse.quote('오늘 점심')

# 요청 URL
# url = "https://openapi.naver.com/v1/search/news.json?query=" + encText
url = "https://openapi.naver.com/v1/search/news.xml?query=" + encText

# Request 객체 생성 -> 헤더 설정
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)

print(response.getcode())   # getcode() : 응답 코드 반환

response_body = response.read()     # read() : 응답 내용 반환
print(response_body.decode('utf-8'))
