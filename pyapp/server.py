import os
import sys
from flask import Flask
from hdbcli import dbapi

conn_data = {
    'server' : 'oktnb132.inf.elte.hu',
    'port': 30015,
    'user': os.environ.get('PY_USER'),
    'password': os.environ.get('PY_PASS')
}

app = Flask(__name__)

port = int(os.environ.get('PORT', 3000))
@app.route('/')
def hello():
    conn = dbapi.connect(conn_data['server'], conn_data['port'], conn_data['user'], conn_data['password'])

    cursor = conn.cursor()
    #cursor.execute("select CURRENT_UTCTIMESTAMP from DUMMY", {})
    cursor.execute('select top 1 * from "COVID_VISUAL_HDI_DB_1"."COVID_visual.db.data::COVIDTIMESERIES";')
    ro = cursor.fetchone()
    cursor.close()
    conn.close()

    return "Current time is: " + str(conn_data)

if __name__ == '__main__':
    app.run(port=port)