# Understanding Data Science
> 쥬피터 노트북 여는 방법   
https://tensorflow.blog/2018/04/19/colab-%ED%8C%81-%EA%B9%83%ED%97%88%EB%B8%8C-%EB%85%B8%ED%8A%B8%EB%B6%81-%EB%B0%94%EB%A1%9C-%EC%97%B4%EA%B8%B0/   

> https://colab.research.google.com/github/다음주소붙여넣기
## 데이터 사이언스란?
데이터 사이언스 = 데이터를 다루는 일
소프트웨어로 데이터를 모을 수 있다.
쇼핑몰, 음악, 정치 캠페인 등 사람들의 마음을 사로잡기 위해 데이터가 꼭 필요한 시대가 도래했다.
데이터를 다룰 수 있는 역량은 앞으로도 계속 중요해질 것.
데이터 사이언티스트가 하는 일 = 가치를 더할 수 있는 일을 찾고 데이터를 이용하여 문제를 해결하는 것. 수학과 통계, 특정분야에 대한 지식, 프로그래밍 역량 등이 중요하다.

## 데이터 사이언스의 목적
### 데이터 사이언스는 딥러닝, 인공지능 만을 위한 것이 아니다.

1. 데이터를 모으는 과정
2. 데이터를 옮기고 저장하는 과정
3. 데이터를 정리하는 과정
여기까지가 데이터 엔지니어링 -
4. 분석
5. 여러 테스트 시행 - 1 ~ 5 단계 - 시간과 노력에 비해 얻어 낼 수 있는 가치가 많음. 
6. 인공지능 - 시간과 노력에 비해 창출 가치가 현재는 작음

### 프로그래밍 언어
R - 통계와 시각화만을 위한 툴
Pythhon - 데이터 사이언스를 위한 라이브러리(numpy, 텐서플로우)가 등장하면서 대두. 다양한 분야에서 사용가능. 다른 분야와 접목도 쉬움.

### 데이터 사이언스 과정
1. 문제 정의하기 - 목표, 기간 방향, 필요한 데이터 목록 등 설정.
2. 데이터 모으기 - 웹 크롤링, 자료 모으기
3. 데이터 다듬기 - 데이터 관찰, 정리
4. 데이터 분석하기 - 데이터 파악, 변형, 통계 분석, 인사이트 도출, 의미 발견
5. 데이터 시각화 및 커뮤니케이션 - 리포트 작성, 시각화, 커뮤니케이션.

## numpy
numerical python = 숫자와 관련한 일을 하는 파이썬 도구
### numpy와 list의 차이
numpy 리스트는 사칙연산이 가능하다. + - * / 모두 가능   
array1 = np.array([1,2,3,4]) 일 때 array1 + 4는 array([5,6,7,8])이 출력된다.  
numpy에서는 한가지 자료형만 표현 가능하다. [1, 2, True, 5] 불가  
list에서는 여러가지 자료형을 한번에 묶을 수 있다.   
numpy 속도처리가 list보다 더 빠르다.   
수치 계산이 많을 때 numpy가 더 효율적일 것.   

## pandas
numpy를 기반으로 만들어진 라이브러리.
