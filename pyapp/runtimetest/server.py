import os
from flask import Flask
from cfenv import AppEnv
from hdbcli import dbapi
import traceback

app = Flask(__name__)
env = AppEnv()

port = int(os.environ.get('PORT', 3000))
hana = env.get_service(name='ENVDUV-cb6znz6p8ij57f78-COVID_visual-hdi_db')

@app.route('/')
def hello():
    try:
        conn = dbapi.connect(address=hana.credentials['host'], port=int(hana.credentials['port']), user=hana.credentials['user'], password=hana.credentials['password'])

        cursor = conn.cursor()
        cursor.execute("select CURRENT_UTCTIMESTAMP from DUMMY")
        ro = cursor.fetchone()
        cursor.close()
        conn.close()
        return "Current time is: " + str(ro["CURRENT_UTCTIMESTAMP"])
    except :
        return traceback.format_exc()



if __name__ == '__main__':
    app.run(port=port)