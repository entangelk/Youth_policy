# 내게 맞춘 청년 정책


글로 적은 내 상황에 대한 맞춤 청년 정책을 추천해 준다.

구현 계획

1. 자연어를 수집받는다
 - 모델 학습에는 검색어를 학습시키고 해당 파라미터에 맞는 결과값을 도출하도록 학습
2. 형태소 분석기로 분석하여 토큰화한다.
3. 각 내용에 맞는 일련번호를 획득한다.
4. 해당 번호를 api를 통해 전달한다.
5. 전달받은 데이터를 화면에 뿌려준다.

필요 기술

fastAPI
okt
lda? 이건 잘 모르겠다.
단어 사전 생성?

머신러닝을 구현해야될까? 그건 잘 모르겠다.
있으면 좋을꺼같은데 데이터를 하나하나 저장하기는 힘들꺼같다.
아니면 저장해도 괜찮을거 같기도 하다.

방법 1.
 우선 데이터를 수집해서 머신러닝에 학습후 해당 카테고리에 대한 데이터를 로드

방법 2.
 입력받은 텍스트를 단순 분석 후 단어 추출 후 api에 쏘기

 - 다중 레이블 기반 학습
 ```
 import numpy as np
import pandas as pd
from skmultilearn.adapt import MLkNN
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

# 예시용 데이터 생성
data = {
    'text': ['I like apples and oranges', 'He prefers bananas and grapes', 'She enjoys strawberries and blueberries'],
    'label_1': [1, 0, 1],  # label_1: 과일을 좋아하는지 여부
    'label_2': [1, 1, 0]   # label_2: 과일을 선호하는지 여부
}

df = pd.DataFrame(data)

# TF-IDF 벡터화
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])

# 레이블 데이터 생성
y = df[['label_1', 'label_2']].values

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# MLkNN 모델 초기화 (k = 레이블 길이)
classifier = MLkNN(k=3)

# 모델 학습
classifier.fit(X_train, y_train)

# 테스트 데이터에 대한 예측
predictions = classifier.predict(X_test)

# 결과 출력
print("Predictions:")
print(predictions)

 ```
