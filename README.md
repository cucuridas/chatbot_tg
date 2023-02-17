# TG chatbot

업무자동화 및 알림 서비스를 제공해주기위한 내부 시스템으로서 개발에 대한 명세를 정의합니다

---

## 1. chatbot(app)구조

1. webex chatbot 응답구조

![image](https://user-images.githubusercontent.com/65060314/219557787-b39587cc-43a8-4a2e-beff-d27e6bdd4d36.png)
```
chatbot email 주소와 webex client를 통해 메세지 이벤트 발생
-> webhook을 통해 'webexcloud'에서 이벤트를 '백엔드서버(tg chatbot)'이 전달 받음
-> '백엔드서버(tg chatbot)' webexcloud로 '/message' api를 호출하여 상세내용 조회
-> 내용확인하여 로직 처리후 webexcloud로 결과 전달
-> webex client로 결과 메세지 출력
```

1. 프로젝트 서비스 실행 구조

```
1. './infra' 디렉토리의 docker-compo 파일을 통해 위부 서비스 container 생성
2. './Elasticsearch'의 index.json 파일의 내용을 elasticsearch api를 통해 추가 후 
'./Elasticsearch/document'의 정보도 생성한 index에 추가
3. 'poetry shell' 명령어를 통해 python env 환경으로 진입하여 'poetry update' 명령어 실행
4. 'poetry run python3 ./app/main.py' 명령어를 통해 app 실행
```

1. app 서비스 실행 내용

해당 내용은 main 파일이 실행되었을때의 실행 순서를 간략하게 나마 정리한 내용입니다 ‘corutine’ 형태로 실행되는 fastapi의 구조에 따라 해당내용가 다른 순서로 진행될 수 있음을 인지하시길 바랍니다

```
1. webex cloud api를 호출하여 webex bot 정보로 webhook을 생성
2. 생성된 정보를 redis에 저장
3. uvicorn을 통해 fastapi task 생성, schedule 역할을 하게되는 roketry taks 생성
4. asyncio.run을 통해 3번항목을 통해 생성되어진 task 실행
5. 서비스 실행
```

---

## 2. 중요 외부 서비스

1) Elasticsearch :

사용자가 입력한 서비스(단어)를 검색하기위한 엔진으로서 사용 유사도 검색(match)을 활용하여 client가 요청하는 서비스를 찾아주는 역할을 맡고있습니다

docker container를 통해 서비스가 제공되어지며 최초 container 생성 후 해당 프로젝트 디렉토리에서 ‘./Elasticsearch’의 디렉토리에서 index파일과 서비스파일을 api를 통해 저장해주어야합니다

2) Redis 

webhook을 통해 전달 받은 이벤트를 인메모리 환경에 저장해두어 client가 요청하는 서비스에 대한 로직처리가 끝나기까지 정보를 저장해두기위해 사용합니다 

webhook 이벤트를 통해 전달 받은 아래의 데이터를 저장합니다

```
"id": "{Webhook event id}",
"roomId": "{Client room id}",
"roomType": "{Client가 요청한 Room type}",
"personId": "{Client의 Id}",
"personEmail": "{Client의 Id(webex email)}",
"created": "{event가 생성된 날짜}"
```

3) Postgres

서비스 로직 처리 후 저장되어야하는 항목들에 대한 관리를 위한 생성한 database입니다

해당 데이터는 프로젝트 루트 디렉토리에 ‘data’라는 이름의 디렉토리에 mount 되어 저장되어집니다

1. team : 팀 정보가 담겨져 있는 Database
2. user : 정보가 담겨져 있는 Database
3. smtpinfo : 메일 전송 서비스를 위한 smtpinfo가 저장되어진 Database
4. tgday : user 별 tgday 정보가 담겨져있는 Database

---

## 3. 파일구조

파일 구조는 아래와 같습니다 

```
.
├── Dockerfile
├── Elasticsearch
│   ├── document
│   ├── index.json
│   └── synonym.txt
├── README.md
├── alembic
│   ├── README
│   ├── env.py
│   ├── script.py.mako
│   └── versions
├── alembic.ini
├── app
│   ├── __init__.py
│   ├── abstract
│   ├── api
│   ├── connection
│   ├── core
│   ├── main.py
│   ├── schedulerGroup
│   ├── service
│   └── util
├── docker-compose.yaml
├── infra
│   └── docker-compose.yml
├── pyproject.toml
└── tests
    ├── __init__.py
    ├── connection
    ├── service
    └── util
```

dockerfile(file) : 해당 프로젝트를 docker image로 생성하기위한 dockerfile 명시

Elasticsearch(dir) : 최초 elasticsearch 생성 시 추가해야할 index 정보와 document 정보를 명시

alembic(dir) : alembic을 통한 DB 마이그레이션을 위한 디렉토리로서 ‘alembic upgrade head’ 명령어를 통해 마이그레이션 진행

app(dir) : 실제 app에 대한 source 코드가 존재하는 디렉토리 각 디렉토리별 상세내용은 아래와 같습니다

- abstract : 추상화 클래스에 대한 py 파일이 존재
- api : api route 정보가 설정되어진 py 파일 존재
- connetion : 외부 서비스와의 연결을 위한 py 파일 존재
- core : fastapi, roketry와 같은 app service에 대한 설정, db 모델링 정보, .env를 통한 app servier config 관리와 같은 py 파일 존재
- schedulerGroup : 해당 서비스는 ‘특정 알림 서비스’를 제공해 주기위해 roketry를 사용 해당 디렉토리는 shcedule 된 Task에 대한 명시가 정의되어진 py파일이 존재
- service : 실제적인 로직이 구현되어진 py파일이 존재
- util : 공통적으로 사용되는 기능들에 대한 구현이되어진 py파일이 존재

docker-compose.yml(file) : 해당 app을 Container로 실행 시키기위해 정의되어진 docker-compose file

*필히 Dockerfile을 통해 image 생성 후 해당 파일 실행

infra(dir) : 필수 연동해야하는 외부 서비스(elasticsearch , postgres, redis)들에 대한 정의를 한 docker-compose 파일이 존재

pyproject.toml(file) : poetry를 통해 추가한 모듈들에 대한 정의가 되어진 file ‘poetry update’ 명령어를 통해 모듈 설치

test(dir) : app 디렉토리의 기능 검증을 위해 작성한 test py 파일이 존재

---

## 4. env

환경 변수 내용입니다 상세내용은 아래와 같습니다

```
#server관련 설정
SERVER_WORKER={uvicorn이 app 실행시 실행시킬 worker의 갯수}
SERVER_HOST={uvicorn 서버의 Host 주소}
SERVER_PORT={uvicorn 서버의 Port 정보}

#redis관련 설정
REDIS_HOST={연동할 redis 서비스의 host}
REDIS_PORT={연동할 redis 서비스의 port}
#elasticsearch 관련 설정
ELASTCSEARCH_HOST={연동할 elasticsearch 서비스의 host}
ELASTCSEARCH_PORT={연동할 elasticsearch 서비스의 port}

#webex Api 관련 설정
WEBEX_BOT_TOKEN={webex bot 생성 시 발급되는 Toekn 값}
WEBEX_BOT_NAME={webex bot 생성 시 입력한 webex bot 이름}
WEBEX_BOT_EMAIL={webex bot 생성 시 입력한 webex bot email 정보}
#webhook 관련 설정
WEBHOOK_URL=https:{Webhook 발생시 전달받아 처리하게될 서버의 주소 [현 프로젝트의 서버주소]}
WEBHOOK_NAME={webexcloud에서 생성 요청할 webhook의 이름}

#Database 정보
DB_USER={연동할 postgres 서비스의 user 정보}
DB_PASSWROD={연동할 postgres 서비스의 user password 정보}
DB_HOST={연동할 postgres 서비스의 host 정보}
DB_PORT={연동할 postgres 서비스의 port 정보}
DB_NAME={연동할 postgres 서비스의 database 이름 정보}

#smtp 정보
SEND_MAIL={보내는 사람의 계정 정보[이메일 형식]}
SEND_PASSWORD={보내는 사람의 계정 비밀번호}
SMTP_URL={사용하게될 smtp Host 정보}
SMTP_PORT={사용하게될 smtp port 정보}
RECEIVE_MAIL={전달할 메일 주소 정보}
```