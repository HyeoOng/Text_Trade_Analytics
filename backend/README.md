# Django 백엔드 서버

백엔드 서버 실행 방법과 코드 변경 가이드입니다.

# 처음 실행하기.

## 환경 설치
- Docker 설치
- backend 폴더 내에서 venv 가상환경 생성
- 가상환경 실행 후, 장고 패키지 설치
```
$ pip install -r requirements.txt
```

## 1. DB 띄우기
- MariaDB를 도커에 띄워서 사용
- 서버가 실행되기 전에 실행되었는지 확인
- 도커를 끄지 않는 한 계속 실행된다. 서버 실행하기 전 잘 돌아가고 있나 대시보드에서 확인 해주기
```
$ docker-compose up -d --build
```

## 2. Migration 하기
- 장고와 데이터베이스를 연결해주는 작업
- 새로운 모델이 추가될 때마다 해주어야 한다.
```
python manage.py makemigrations
python manage.py migrate 
```

## 3. 장고 로컬 서버 띄우기
- 로컬 서버 주소: http://localhost:8000
```
$ python3 manage.py runserver 
```

### 그외 필요시:
- 장고 어드민 페이지 계정 생성 (`admin/admin`)
- http://127.0.0.1:8000/admin 접속시 사용
```
python manage.py createsuperuser
```

## 모델 추가하기
- 모델이란? DB 테이블의 데이터를 장고에서 불러오고 컨트롤할 수 있게 해주는 코드 (`Animal` 모델 참고)
- 모델 추가하기:
1. `models.py`에 모델 추가
2. `python manage.py makemigrations`로 마이그레이션 파일 생성
3. `python manage.py migrate`로 디비 테이블 생성
4. `admin.py`에 추가해서 어드민 페이지에 보이도록
5. 변경된 파일들과 마이그레이션 파일을 `git commit`

