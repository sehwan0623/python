import requests
from pprint import pprint


# 문제1. 날씨 데이터의 응답을 json 형태로 변환하여 key 값만 출력하시오.
# 공식문서의 요청변수와 예제 요청결과(JSON) 부분을 참고합니다.

def get_weather():
    # 여러분의 OpenWeatherMap API 키를 설정하세요
    api_key = '9fa589f18669c246b5a87a3d5040e178'
    
    #서울 위도
    lat = 37.56

    #서울 경도
    lon = 126.97

    url = f'https://api.openweathermap.org/data/2.5/weather?lat=37.56&lon=126.97&appid=9fa589f18669c246b5a87a3d5040e178'

    #url 전체
    #https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}

    #dict 형식으로 response 변수에 할당
    response = requests.get(url).json()

    # 요구사항에 맞도록 이곳의 코드를 수정합니다.

    return response


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    
    result = get_weather()

    #사용자가 보기 좋은 형식으로 print
    pprint(result)
