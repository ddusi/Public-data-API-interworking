# Public data API interworking 
공공데이터 API를 내부 DRF API서버와 연동하여 데이터 가공 후 원하는 정보만 화면에 출력하는 작업입니다.
- 작업범주 
    1. 건축물대장
    2. 토지정보


## Issues - PR Form 
Feature : new function develop 새로운 기능 개발 <br>
Update : old function fix and upgrade 기존 기능 향상 <br>
Bug : bug fix 버그 수정 <br>
Enhancement : New feature or request 기능 요청, 제안 <br>

PR은 같은 제목으로 올리고 내용은 resolve #00 으로 연결.


## environment
python==3.6.8 <br>
django==2.2.7

**추가된 라이브러리들**
 - furl==2.1.0 <br>
     urllib보다 url을 다루기에 편하고, immutable한 url객체를 mutable하게 조작 하기 위함. 
 - xmltodict==0.12.0 <br>
     공공데이터 api에서 제공하는 형식은 xml만 있기 때문에, 간편하게 json형식으로 바꿔주는 라이브러리 사용. 
     기존 django의 코드를 보면 최종형태를 json형식으로 뿌리고 있으며, ajax로 다루기도 편함. 
 - orderedmultidict==1.0.1 <br>
     `xmltodict`에 종속되는 라이브러리. <br>
     
 requirements.txt 파일로 관리하고 있습니다. 

## django의 권한 설정 
```
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
```
기본 권한 설정은 `AllowAny`으로 설정하였습니다. 모든 유저들이 접근 할 수있다는 의미 입니다. 
슈퍼유저 혹은 특정 유저들만 호출할 수 있도록 하는 것을 원하시면 권한설정 작업을 해야합니다.


## django의 패키지화 
django도 자바의 spring과 마찬가지로 각 models, views, forms 등등을 패키지화 하여 관리할 수 있습니다. 
![image](https://user-images.githubusercontent.com/58924238/94524928-3ee84680-026e-11eb-9236-a6cd4179edbf.png)



# 설치 및 시작

1. 설치 
```
git clone https://github.com/DenimY/jangyeonju.git
cd jangyeonju
python manage.py runserver
```

2. 공공데이터 api 호출
서버를 실행 한 후, 아래 url에 들어갑니다. 

```
http://localhost:8000/rfapi/getTitle-info/
```
![image](https://user-images.githubusercontent.com/58924238/94525973-cc786600-026f-11eb-8bc0-133ca9dd86fb.png)
```
{ 
           "sigunguCd": "11680",
            "bjdongCd": "10300",
            "bun": "0012",
            "ji": "0000",
            "numOfRows": "20"
}
```
위와 같은 데이터를 JSON형식으로 입력 후, POST로 요청시 공공데이터 API가 응답합니다. 
![image](https://user-images.githubusercontent.com/58924238/94526169-1b260000-0270-11eb-8768-94cd4cebed35.png)

3. templates에 데이터 출력하기
데이터 요청은 위와 같이 이루어 지며 templates에 출력된 화면은 다음과 같습니다. 
```
http://localhost:8000/property-detail/
```
![image](https://user-images.githubusercontent.com/58924238/94526410-70faa800-0270-11eb-9a5d-93591aa038ab.png)

토지정보 

![토지 정보](https://user-images.githubusercontent.com/58924238/94574765-770f7980-02ae-11eb-84ec-7e25e31eef1b.png)










