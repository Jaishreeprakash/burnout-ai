import time

from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

db_url = settings.effective_database_url
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

is_sqlite = db_url.startswith("sqlite")
connect_args = {"check_same_thread": False} if is_sqlite else {}

# pool_pre_ping tests each connection with a cheap query before handing it to
# the app, so a connection the remote DB has silently dropped (idle timeout,
# transient DNS blip) gets transparently replaced instead of surfacing as a
# 500 mid-request. pool_recycle proactively retires connections before cloud
# load balancers (e.g. Supabase's pooler) tend to close them.
engine_kwargs = {"connect_args": connect_args, "pool_pre_ping": True}
if not is_sqlite:
    engine_kwargs.update(pool_size=20, max_overflow=30, pool_recycle=280, pool_timeout=30)

engine = create_engine(db_url, **engine_kwargs)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    # Retry session acquisition a few times with backoff so a transient DB
    # connectivity blip (dropped connection, brief DNS failure) doesn't
    # immediately fail every in-flight request with a 500.
    attempts = 3
    for attempt in range(attempts):
        db = SessionLocal()
        try:
            db.execute(text("SELECT 1"))
            break
        except OperationalError:
            db.close()
            if attempt == attempts - 1:
                raise
            time.sleep(0.5 * (attempt + 1))
    try:
        yield db
    finally:
        db.close()
