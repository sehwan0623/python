import pprint
import requests

# 전체 정기예금 상품 리스트를 출력하시오.
# 공식문서의 요청변수와 예제 요청결과(JSON) 부분을 참고합니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 출력합니다.
# 3. 위의 결과 중 key 값이 "baseList" 인 데이터를 출력합니다.

def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    #api_key = "d1031efc889f8c9985716997a7161689"
    url = 'https://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth' : '1a9fb2baf17c6066cf13d56da82c4bee',
        'topFinGrpNo' : '020000',
        'pageNo' : 1
    }
    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    response = requests.get(url, params=params).json()
    response = (response["result"]["baseList"])
    return response

    
# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)