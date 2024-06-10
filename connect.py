import sqlalchemy import create_engine, text

engine = create_engine("f'postgresql+psycopg2://{postgres}:{123}@{localhost}:{5432}/{postgres}'")


with engine.connect() as conn:
    conn.execute(text('SELECT "hello"'))



