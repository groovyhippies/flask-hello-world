import psycopg2
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from --scott yu-- in 3308'

@app.route('/db_test')
def test():
    conn = psycopg2.connect("postgresql://scott_yu_cspb3308_user:bAzMqyShdoA6k6BkxKUkFGmj7hp3j2RI@dpg-d2333abe5dus73a6tl1g-a/scott_yu_cspb3308")
    conn.close()
    return "Database connection successful!"
