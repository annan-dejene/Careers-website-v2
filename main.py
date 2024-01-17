from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db


app = Flask(__name__, static_folder='public/static')

@app.route('/')
def index():
  return render_template('home.html', jobs=load_jobs_from_db())


@app.route('/api/jobs')
def list_jobs():
  return jsonify(load_jobs_from_db())


@app.route('/job/<id>')
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return 'Not Found', 404
  
  return render_template('jobpage.html', job=job)
  


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
