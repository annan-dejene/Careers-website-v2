from flask import Flask, render_template, jsonify


app = Flask(__name__, static_folder='public/static')

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'New York, USA',
    'salary': '100,000 USD'
  },
  {
    'id': 2,
    'title': 'Data Engineer',
    'location': 'Dubai, United Arab Emirates',
    'salary': '130,000 USD'
  },
  {
    'id': 3,
    'title': 'Full Stack Developer',
    'location': 'Remote',
    'salary': '120,000 USD'
  }
]

@app.route('/')
def index():
  return render_template('home.html', jobs=JOBS)


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
