from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from app.core.config import Settings


"""
sqlAlchemy를 통해 orm 사용하기위해 정의되는 python 파일입니다 engine을 통해 연결 객체를 입력받아
sessionmaker 클래스를 통해 session 연결을 진행합니다

"""

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{Settings.DB_USER}:{Settings.DB_PASSWROD}@{Settings.DB_HOST}:{Settings.DB_PORT}/{Settings.DB_NAME}"

engine: AsyncEngine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True, pool_pre_ping=True)
Session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()


def get_db():
    db = None
    try:
        db = Session()
        yield db
    finally:
        db.close()
