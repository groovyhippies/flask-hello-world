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

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgresql://scott_yu_cspb3308_user:bAzMqyShdoA6k6BkxKUkFGmj7hp3j2RI@dpg-d2333abe5dus73a6tl1g-a/scott_yu_cspb3308")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball (
            First VARCHAR(255),
            Last VARCHAR(255),
            City VARCHAR(255),
            Name VARCHAR(255),
            Number INT
        );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

def inserting():
    conn = psycopg2.connect("postgresql://scott_yu_cspb3308_user:bAzMqyShdoA6k6BkxKUkFGmj7hp3j2RI@dpg-d2333abe5dus73a6tl1g-a/scott_yu_cspb3308")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        VALUES
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"

@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgresql://scott_yu_cspb3308_user:bAzMqyShdoA6k6BkxKUkFGmj7hp3j2RI@dpg-d2333abe5dus73a6tl1g-a/scott_yu_cspb3308")
    cur = conn.cursor()
    cur.execute('SELECT * FROM Basketball;')
    records = cur.fetchall()
    conn.close()

    response_string = "<table border='1'>"
    for player in records:
        response_string += "<tr>"
        for info in player:
            response_string += "<td>{}</td>".format(info)
        response_string += "</tr>"
    response_string += "</table>"

    return response_string
