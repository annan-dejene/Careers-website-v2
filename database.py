from sqlalchemy import create_engine, text
import os


DB_STR = os.environ['DB_CONNECTION_STRING']

engine = create_engine(DB_STR, connect_args={
  'ssl': {
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
  
    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))
  
  return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"SELECT * from jobs WHERE id = :val"), 
      {"val": id}
    )

    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0]._mapping)
  