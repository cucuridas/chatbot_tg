# dev README .md

---
개발 환경 구축 시 필요한 내용들을 정리하였습니다

---

## 개발환경 설정

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

