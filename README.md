# Timegate TG-Cloud BigData Management Backend

---
타임게이트 클라우드 BigData 관리시스템의 백엔드 프로젝트 파일럿에 대한 개발 명세를 정리한다.
해당 프로젝트는 기본적으로 파이썬 fastAPI 웹프레임워크 + SqlAlchemy ORM + PostgreSQL (RDMBS) 기반으로 구성하고 비동기(async) 기반의 API 개발 및 인프라 연동을 목표로 한다.
프로젝트 개발을 위한 파이썬 가상환경으로는 poetry 를 사용하며, 설치 및 설정 방법은 하단을 참고한다.

---

## 개발환경 설정

>~~인스톨러를 통한 파이썬 설치 (Python 버전 3.11.1)~~
* ~~로컬 환경에 파이썬 3.11.x 버전을 아래 url 을 통해 설치한다.~~   
  ~~[파이썬 다운로드](http://www.python.org/downloads)~~
* 여러 파이썬 버전을 하나의 PC 에서 사용해야할 경우 특정 버전의 인스톨러 설치 대신 아래 pyenv 를 설치하도록 한다.
- 설치 확인
```shell
 python --version
```

> pyenv 를 통한 파이썬 설치 (Python 버전 3.11.1)
* pyenv 는 파이썬 버전 관리 매니저 라이브러리로써 아래 링크를 통해 설치한다.  
[macOS 에서 설치](https://leesh90.github.io/environment/2021/04/03/python-install/)  
[윈도우에서 pyenv-win 설치](https://thekkom.tistory.com/69)  


* 설치 후  pyenv 의 파이썬 버전 db 를 업데이트 하고, 특정 파이썬 버전을 설치한다.
```shell
pyenv update  # pyenv db update
pyenv install --list  # 설치할 수 있는 버전 확인 
pyenv install 3.11.1  # 3.11.1 버전 설치 
pyenv global 버전  # 전역으로 사용할 파이썬 버전을 지정
```
* git clone 받은 프로젝트에서 아래 명령어를 실행하여 해당 파이썬 버전으로 설정한다.
```shell
pyenv local 3.11.1  # 현재 프로젝트의 파이썬 버전을 3.11.1 로 지정
python3 --version  # 3.11.1 이 출력되야 함. python 이 아닌 python3 으로 실행해야 함
```
* (poetry 설치 후) 패키지 관리자인 poetry 설치 후 해당 poetry 가 pyenv local 로 설정한 파이썬 버전을 사용하도록 하려면 아래와 같이 실행한다.
```shell
poetry env use python3
poetry env info  # 3.11.1 이 출력되야 함
# 이후 poetry update 등을 실행
```

<br/>

>패키지 관리자 설치 - Poetry (버전 1.2 later)
* Poetry 는 pyproject.toml 파일을 통해 패키지 관리 및 가상환경 설정을 할 수 있는 라이브러리이다.
* 로컬 환경에 다음 url 을 참고해 poetry 를 설치 한다.    
  [Poetry docs/Installation](https://python-poetry.org/docs/#installation)
* 윈도우의 경우, 절차대로 설치 후 환경변수에 PATH 등록까지 해야 한다.

<br/>

>Poetry 를 이용한 가상환경 실행 및 패키지 설치
* git clone 한 경로의 커맨드라인에서 아래 명령어를 차례로 실행한다.
```shell
  # pyenv 로 파이썬 설치한 경우
  poetry config virtualenvs.in-project true  # 현재 경로에 venv 가상환경을 생성
  poetry env use python3  # poetry 가 사용할 파이썬 버전을 지정 (pyenv local 로 설정한 버전이 설정됨)
  poetry env info  # 3.11.1 이 출력되야 함
  poetry update  # 의존성 설치 (pyproject.toml 에 정의된 패키지를 설치 - poetry.lock 삭제후 poetry install 하는것과 같다.)
  
  # 파이썬 단독 설치한 경우
  # poetry config virtualenvs.in-project true  (현재 커맨드라인 경로에 .venv 생성)
  # poetry shell  (가상환경 activate)
  # poetry update
``` 

* 개발 진행시 추가할 패키지가 있다면 다음과 같이 add 명령어를 사용해 설치한다.
```shell
poetry add some-library1 some-library2
poetry add decohints mypy --dev  # 개발시에만 필요한 패키지의 경우 --dev 옵션을 추가후 사용한다.
```

* 설치된 패키지 목록의 정보는 다음과 같이 확인할 수 있다.
```shell
poetry show
```

* [poetry 사용 참고 블로그](https://velog.io/@hj8853/Poetry%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC-%EA%B0%80%EC%83%81%ED%99%98%EA%B2%BD-%EB%A7%8C%EB%93%A4%EA%B8%B0)

<br/>

>Intellij 또는 PyCharm SDKs 설정
* 개발 IDE 는 JetBrains 의 PyCharm 또는 IntelliJ 의 python 플러그인을 통해 가능하며, vscode 같은 에디터 툴을 사용해도 된다.
  어떤 개발 툴을 사용하든 파이썬 가상환경 사용시 커맨드라인을 통해 적용 가능하지만
  툴 자체에서 제공하는 코드 어시스트 등의 기능을 사용하기 위해서 파이썬 인터프리터 설정(또는 가상환경 설정)을 해주어야 한다.
* IntelliJ 의 경우에는 아래와 같이 SDK 설정을 통해 위에서 설치한 poetry 가상환경을 설정해준다. (PyCharm 의 경우에는 인터프리터 설정)
```shell
File -> Project Structure -> SDKs ->
 + (Add New SDK) 버튼 클릭 -> Add Python SDK -> Poetry Environment ->
    Existing environment 선택 후 위에서 설정한 poetry 가상환경 경로(.venv) 선택 및 추가 ->
     현재 Project SDK 에서 선택 후 적용
```

<br/>

>.venv 디렉토리 Excluded 설정 (Intellij/PyCharm)
* 위의 가상환경 생성시 poetry config virtualenvs.in-project 명령어를 실행 후 poetry shell & install 한 경우 프로젝트 root 하위에 .venv 가 생성되는데
  IDE 에서 해당 .venv 폴더에서 우클릭 - Mark Directory as - Excluded 를 선택해준다.
  이렇게 하지 않으면 auto import 등의 기능이 정상 작동하지 않고, 검색등을 했을때 .venv 내의 파일에서도 검색을 하므로 반드시 excluded 로 바꿔준다.

<br/>

> 코드 포맷팅 툴 - Black 설정
* 파이썬 코드포맷팅 툴인 Black 을 사용하여 코드 포맷팅을 실시간으로 적용한다.
* IntelliJ/PyCharm 의 경우 다음 링크등을 참고하여 Externel Tool 로 설치 및 설정한다. (단축키등을 지정해 변경시마다 설정할 수 있다.)
  [링크1](https://medium.com/daehyun-baek/python-%EC%BD%94%EB%93%9C-%EC%8A%A4%ED%83%80%EC%9D%BC-%ED%88%B4-pycharm-%ED%99%98%EA%B2%BD-flake8-black-4adba134696a)
  [링크2](https://velog.io/@heka1024/PyCharm-%ED%8F%AC%EB%A7%A4%ED%84%B0%EB%A1%9C-Black-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0)
  단, Program arguments 에 --line-length=110 을 추가해 기본 라인 길이 88 대신 110을 사용 한다.
* IntelliJ/PyCharm 의 Settings - Editor - Code Style 에서 Hard wrap at 의 값도 110 으로 변경해준다.

<br/>

> pre-commit 설정
* 아래 명령어를 차례로 실행하여 commit, push 단계에서의 flake8 (code inspect), black (formatting) 자동 검사 설정을 한다. (위의 poetry update 완료 후)
```shell
poetry run pre-commit autoupdate
poetry run pre-commit install --hook-type pre-commit --hook-type pre-push
```

<br/>

> 파일 인코딩 설정
* 개발 환경의 파일 인코딩을 UTF-8 로 설정한다.
* IntellJ/PyCharm 의 경우 아래 절차를 통해 인코딩 설정을 변경한다.
```shell
Settings -> Editor -> File Encodings 에서 Global, Project, Properties 모두 UTF-8 로 변경후 적용한다.
```

<br/>

## SQLModel (SqlAlchemy) 사용을 위한 엔티티 정의
* 본 프로젝트는 DB 처리를 위해 ORM (Object-relational mapping) 을 사용하며, 파이썬에서 가장 널리 사용되는 ORM 라이브러리인 SqlAlchemy 를 사용한다.
* SqlAlchemy 는 1.4 버전 이후부터 비동기 기반의 DB 처리를 지원하기 때문에 본 프로젝트는 1.4 버전의 SqlAlchemy 를 사용한다.
* 단, sqlAlchemy 를 좀 더 쉽게 사용하고, pydantic 모델과의 동시 사용을 위해 SQLModel (https://github.com/tiangolo/sqlmodel) 라이브러리를 SqlAlchemy 의 wrapper 라이브러리로 사용한다.
* SQLModel 는 대부분의 기능들이 sqlAlchemy 와 pydantic 의 기능을 wrapping 한 것이므로 모델에 대한 정의만 아래 예시와 같이 해주면 SqlAchemy 를 사용하는것과 큰 차이는 없다.
* SQLModel 에 대한 정의는 app/models/entities 경로 하위의 py 파일들에 해당 테이블에 정의하며, 이렇게 정의된 모델은 엔티티라고 읽도록 한다.
* 엔티티를 정의하는 파일의 prefix 로 ```em_``` 을 추가하여 이 파일이 엔티티 모델을 정의한 파일이라고 쉽게 알 수 있도록 한다.
* 새로운 엔티티 파일을 추가한 경우, ```entities/__init__.py``` 파일에 import 구문을 넣어주도록 한다. (alembic, sqlalchemy 등에서 base 모델을 처리하기 위함.)
* SQLMOdel 라이브러리 형식으로 users 테이블의 엔티티 모델 정의 예시는 다음과 같다.(em_user.py)
```python
class EmUser(EmBase, table=True):
  # EmBase 가 SQLModel 을 상속받으며 기본적으로 id, created_at, updated_at 필드를 포함한다.
  # table=True 로 설정하면 이 모델은 pydantic 모델뿐 아니라 SqlAlchemy 모델(DB모델)로도 사용함을 의미한다.
  __tablename__ = "users"  # 실제 테이블명을 정의한다.
  # pydantic 관련 속성은 Field 내부 옵션으로, SqlAlchemy 관련 속성은 sa_column 로 정의한다. (sa_column 에 인자는 SqlAlchemy 모델 정의할때와 동일하다)
  username: str = Field(sa_column=Column(String(255), unique=True, nullable=False))
  password: str = Field(sa_column=Column(Text, nullable=False))
  name: str = Field(sa_column=Column(String(255), nullable=False))
  mobile: Optional[str] = Field(
    default=None, sa_column=Column(String(20), unique=True, nullable=True)
  )
  # enum 형태로 컬럼 정의할 경우 아래와 같이 정의하고, postgres 의 경우 enum 에 대한 dataTypes 가 생성된다. (alembic downgrade 시 수기 제거 명령어 추가 필요)
  level: UserLevelEnum = Field(
    default=UserLevelEnum.GENERAL.value,
    sa_column=Column(
      "user_level",
      sqlAlchemyEnum(
        UserLevelEnum,
        name="user_level",
        values_callable=lambda obj: [e.value for e in obj],
      ),
      nullable=False,
      default=UserLevelEnum.GENERAL.value,
      server_default=UserLevelEnum.GENERAL.value,
    ),
  )
```
* 위와 같이 정의 후 ```app/models/entities/__init__.py``` 파일에는 다음과 같이 해당 파일이 import 되어야 한다.
```python
from app.models.entities.em_user import *
```
* 이렇게 정의한 SQLModel 모델은 SqlAlchemy 의 DB 접근 모델로도 사용가능하고, 웹 요청/응답에 사용할 수 있는 pydantic 모델로도 사용 가능하다.

<br/>

## alembic (DB 마이그레이션 및 버전 관리) 사용
* DB 의 테이블등을 수정할 경우 직접 DB 에서 DDL 을 통해 변경할 수 있지만 본 프로젝트에서는 alembic 이라는 툴을 통해 코드 기반의 DB 테이블 관리를 하도록 한다.
* alembic 을 통해 app/entities 경로에 정의된 엔티티 파일들을 기반으로 코드 기반의 db 마이그레이션 및 버저닝을 할 수 있다.
* 위의 sqlalchemy 엔티티 모델을 추가한 뒤, 해당 엔티티 모델을 실제 DB 에 적용하도록 하기 위해 다음과 같은 명령을 커맨드라인에서 수행한다.
```shell
* 스크립트 생성
alembic revision -m "코멘트" --autogenerate

* 위 명령어 실행후 /alembic/versions 경로에 생긴 해당 코멘트에 해당되는 py 파일에 변경사항이 잘 반영된지 확인 후 아래 명령어를 실행하면 실제 db 에 반영한다.
alembic upgrade head
```

* 로컬에서 별도의 postgres 를 설치하여 개발할 경우 .env 에 DB_URL 을 변경해주고 아래 alembic 명령어를 수행하면 해당 DB 에 테이블이 생성된다.
```shell
alembic upgrade head  # 반대로 초기 상태로 테이블을 제거하는것은 alembic downgrade base (주의)
```
* alembic 을 통한 db 마이그레이션등은 /alembic/env.py 파일에 설정된 db url, entity 경로등을 통해 수행된다.

> PostgreSql 기본 스키마(/postgres) 가 아닌 별도 스키마 사용시 (ex: /bigdata_pilot)
  DBeaver 툴 사용시 기본 database (스키마) 인 postgres 만 보이도록 기본 설정되어 있으므로 다음과 같이 설정한다.
  ```해당 connection 우클릭 -> connection settings > PostgreSql 탭 -> show all databases 체크```

<br/>

## Application 구동

### .env 파일 생성
> 프로젝트 root 에 .env 파일이 필요하며 env_file_sample 을 참조하여 생성하고 팀원에게 설정값등을 전달받도록 한다.  
  .env 환경변수 파일은 git repository 에 올라가지 않도록 gitignore 에 추가되어 있다. 

### app 실행
> 개발 단계에서의 앱 실행은 /app/main.py 파일의 main 함수를 통해 실행하며, asgi 서버인 uvicorn 을 통해 앱이 구동된다.
* IntelliJ/Pycharm 등의 IDE 에서는 main 함수에서 우클릭 Run/Debug 버튼을 통해 실행하며 이후부터는 우측상단 또는 하단 Run / Debug 탭에서 실행가능 하다.

* 커맨드라인에서 실행할 경우 아래와 같이 실행한다.
```shell
uvicorn app.core.server:app --reload
```

* 기본 설정된 환경 사용시 앱이 구동되면 다음 url 을 통해 api docs (swagger 또는 redoc) 화면으로 접근이 가능하다. (.env 의 APP_HOST:APP_PORT 의 값 사용)  
[http://localhost:8000/docs](http://localhost:8000/docs)  # swagger docs page  
[http://localhost:8000/redoc](http://localhost:8000/redoc)  # redoc docs page  



## 중요 의존성 라이브러리
```
- 웹프레임워크 - fastapi

- 데이터 모델 Validator - pydantic

- DB ORM 모듈 - sqlAlchemy (1.4+)

- 비동기 db 쿼리 언어 지원(sqlAlchemy 기반) - databases

- DB 마이그레이션 관리 툴(sqlAlchemy 기반) - alembic

- 비동기 PostgreSQL driver - asyncpg

- 비동기 서버 게이트웨이 라이브러리 (ASGI) - Starlette (included in fastapi)

- ASGI 기반 웹서버 - Uvicorn (실제 배포시에는 Gunicorn 을 통해 Uvicorn 워커를 사용하는 방식으로 사용한다)

- 비동기 레디스 클라이언트 - aioredis

- 엘라스틱서치 클라이언트 - elasticsearch [async]

- 로깅 라이브러리 - loguru

- 암호 해싱 - passlib

- Json Web Token - pyjwt

- json 직렬화/역직렬화 라이브러리 - ujson

- 유니코드, 아스키 변환 (url 에 유니코드 to 아스키 변환 등) - python-slugify, unicode

- 테스팅 툴 - pytest
```
>본 프로젝트와 연동하는 인프라는 다음과 같다.
- PostgreSQL (RDBMS -14 later)
- ElasticSearch ((BigData Query - 8 later)
- Airflow (BigData Job Trigger)
- Redis (Cache Store))

* 위 연동 인프라를 비동기 기반으로 사용하기 위해 해당 인프라의 async 연동을 지원해주는 라이브러리를 활용하도록 한다.