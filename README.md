# Text Trade Analytics - 증권사 리포트 감성분석을 통한 자동 종목추천 시스템 구축
-----------------------

> 주식투자, 증권사 리포트를 알면 돈이 보인다는데....

-----------------------

## Django 백엔드 서버

백엔드 서버 실행 방법과 코드 변경 가이드입니다.

## 처음 실행하기.

### 환경 설치
- Docker 설치
- backend 폴더 내에서 venv 가상환경 생성
- 가상환경 실행 후, 장고 패키지 설치
- 가상환경 실행 스크립트 - `source .venv/bin/activate` (자기 가상환경 이름 입력하기)
```
$ pip install -r requirements.txt
```
- 새로운 패키지를 설치할 경우, 이 명령어 실행
```
$ pip freeze > requirements.txt
```

### 1. DB 띄우기
- PostgresDB를 도커에 띄워서 사용
  - 1.docker run -d \
    --name my_postgres \
    -p 5432:5432 \
    -e POSTGRES_DB=stock_db \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_PASSWORD=password \
    postgres:latest
  - 2.docker exec -it my_postgres psql -U postgres
  - 3.CREATE TABLE stock_broker_report (
    pdf_name VARCHAR(100) PRIMARY KEY,
    wdate DATE,
    company VARCHAR(45),
    title VARCHAR(45),
    content VARCHAR(1500),
    stock_broker VARCHAR(45),
    target_opinion VARCHAR(45),
    target_price INT,
    report_link VARCHAR(200),
    pdf_text TEXT,
    pdf_summerize TEXT,
    pdf_sent_score FLOAT,
    pdf_sent_topic VARCHAR(500)
    );
  - 4.SELECT column_name, data_type, is_nullable, column_default
    FROM information_schema.columns
    WHERE table_name = 'stock_broker_report';
- 서버가 실행되기 전에 실행되었는지 확인
- 도커를 끄지 않는 한 계속 실행된다. 서버 실행하기 전 잘 돌아가고 있나 대시보드에서 확인 해주기
```
$ docker-compose up -d --build
```

### 2. Migration 하기
- 장고와 데이터베이스를 연결해주는 작업
- 새로운 모델이 추가될 때마다 해주어야 한다.
```
python manage.py makemigrations
python manage.py migrate 
```

### 3. 장고 로컬 서버 띄우기
- 로컬 서버 주소: http://localhost:8000
```
$ python3 manage.py runserver 
```

### 4. DB에 csv 데이터 import하기
- 만약 장고 어드민 페이지에서 주식 데이터가 보이지 않는다면, 스크립트를 사용해서 csv 데이터를 임포트해준다
- 만약 새로운 파일을 추가해서 추가데이터를 넣어야 할 경우, import_stock_data 스크립트 제일 위에 있는 FILE_NAME을 바꿔서 실행해주면 된다
```
$ python3 import_stock_data.py
```

#### 그외 필요시:
- 장고 어드민 페이지 계정 생성 (`admin/admin`)
- http://127.0.0.1:8000/admin 접속시 사용
```
python manage.py createsuperuser
```

### 모델 추가하기
- 모델이란? DB 테이블의 데이터를 장고에서 불러오고 컨트롤할 수 있게 해주는 코드 (`Animal` 모델 참고)
- 모델 추가하기:
1. `models.py`에 모델 추가
2. `python manage.py makemigrations`로 마이그레이션 파일 생성
3. `python manage.py migrate`로 디비 테이블 생성
4. `admin.py`에 추가해서 어드민 페이지에 보이도록
5. 변경된 파일들과 마이그레이션 파일을 `git commit`

### API 추가하기
Django Rest Framework라는 장고 써드파티 라이브러리 사용
1. API에서 사용될 모델을 만든다 - `models.py`
2. API에서 사용될 Serializer를 만든다 - `serializers.py`
  - Serializer는 모델 <-> json으로 변환해주는 역할
  - Serializer에서 모델 필드들을 꼭 포함해준다.
3. API를 만든다 - `views.py`
  - List 타입과 Detail 타입을 클래스를 각각 만든다.
  - 만든 클래스들을 각 약속된 주소 형식에 맞게 `urls.py`에 추가해준다.

## Front-end Vue.js setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

----------------------------------------------------------------------

## 구현 영상

<p align="center">
  <img src="[https://github.com/HyeoOng/Text_Trade_Analytics/assets/112822303/6160d3ce-e092-40fd-bbdf-a453835e5406](https://github.com/HyeoOng/Text_Trade_Analytics/assets/112822303/0df8f1b2-8de0-41ab-ad98-d31c5da4e75f)https://github.com/HyeoOng/Text_Trade_Analytics/assets/112822303/0df8f1b2-8de0-41ab-ad98-d31c5da4e75f">
</p>
