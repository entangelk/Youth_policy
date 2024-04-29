import requests
from dotenv import dotenv_values
import xml.etree.ElementTree as ET


# 청년 정책
# form :  https://www.data.go.kr/data/15088883/openapi.do

url='https://www.youthcenter.go.kr/opi/youthPlcyList.do'


config = dotenv_values("./.env")
keys = config.get('API_KEY')

display_count = 10

params ={
    'openApiVlak':keys,
'display': display_count,
'pageIndex': 1
}

pass
response = requests.get(url, params=params)
content = response.content.decode('utf-8')  # 이진 데이터를 UTF-8로 디코딩하여 문자열로 변환
root = ET.fromstring(content)  # XML 문자열을 파싱하여 ElementTree 객체로 변환


# <youthPolicy> 요소 반복하여 값 추출
for policy in root.findall('youthPolicy'):
    biz_id = policy.find('bizId').text
    biz_sjnm = policy.find('polyBizSjnm').text
    itcn_cn = policy.find('polyItcnCn').text
    spor_cn = policy.find('sporCn').text
    
    # 추출한 값 출력
    print("bizId:", biz_id)
    print("polyBizSjnm:", biz_sjnm)
    print("polyItcnCn:", itcn_cn)
    print("sporCn:", spor_cn)
    print()  # 개행 추가하여 각 정책의 정보를 구분합니다.




# type(contents)
# # <class 'dict'>
# contents['youthPolicy']['polyBizSecd']


# {"resultCode": "00", "resultMsg": "정상"}


# contents['header']['resultCode']
# # '00'
# contents['body']['totalCount']
# # 18
# type(contents['body']['items'])
# # <class 'list'>

'''
# mongodb 저장

from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")
# database 연결
database = mongoClient["data_go_kr"]
# collection 작업
collection = database['rent-loan-rate-info']
# insert 작업 진행
result = collection.insert_many(contents['body']['items'])

pass
'''