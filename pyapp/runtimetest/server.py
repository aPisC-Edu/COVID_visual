
import traceback
import db
from flask import Flask
import os
from jsonResponse import jsonResponse

import numpy as np
from Algorithms.AR import AR

app = Flask(__name__)
port = int(os.environ.get('PORT', 3000))

@app.route('/')
def hello():
    try:
        conn = db.connect()

        cursor = conn.cursor()
        cursor.execute("select CURRENT_UTCTIMESTAMP from DUMMY")
        ro = cursor.fetchone()
        cursor.close()
        conn.close()
        return jsonResponse({"status": "OK", "time": str(ro["CURRENT_UTCTIMESTAMP"])})
    except :
        return traceback.format_exc()

@app.route('/select')
def sel():
    try:
        conn = db.connect()

        # Initialize select and data type
        select = 'select measure_ts, sum(confirmed) confirmed from "ENVDUV_COVID_1"."COVID_visual.db.data::COVIDTIMESERIES" where region like \'%China%\' group by measure_ts order by measure_ts;'
        dt = np.dtype([
        ("f2", object),
        ("f1", "int32"),
        ])

        # Run query
        n = db.select(conn, select, dt)
        
        y = n["f1"]

        y = n["f1"]
        z = n["f2"]
        x = np.arange(y.shape[0])
        y2 = np.log(y)
        y3 = -y2

        c = y.shape[0]
        c2 = round(c/2) # train size

        tr_y = y[:c2]
        tt_y = y[c2:]

        tr_x = z[:c2]
        tt_x = z[c2:]

        #train, test = train_test_split(y, train_size=20)


        # Visualize the forecasts (blue=train, green=forecasts)
        #plt.plot(x, y2)
        #plt.plot(x, np.polyval(p3, x))
        #plt.plot(x, np.polyval(p4, x))
        #plt.show()


        plt.plot(tr_x,tr_y)
        #plt.plot(z,y)
        plt.plot(tt_x,tt_y)

        #plt.plot(x2, LR(x, y, x2)) # linear
        #plt.plot(x2, ExpR(x, y, x2)) # exponential
        #plt.plot(x2, GaussR(x, y, x2)) # Gauss
        res = MA(tr_x, tr_y, tt_x)
        dbinsert(conn, z, res, 'confirmed', 'ENVDUV_T2', None, None)

        return jsonResponse({"status": "OK", "data": y.tolist()})
    except :
        return traceback.format_exc()

@app.route('/result/<resid>')
def result(resid):
    conn = db.connect()

    # Initialize select and data type
    select = 'select "PROVINCE", "REGION", "MEASURE_TS", "CONFIRMED", "SUSPECTED", "RECOVERED", "DEATH", "RESULT_ID" from "ENVDUV_COVID_1"."COVID_visual.db.data::COVID_RESULT" where "RESULT_ID" = ?;'
    
    cursor = conn.cursor()
    cursor.execute(select, resid)
    res = cursor.fetchall()
    cursor.close()
    n = [list(i) for i in res]
    return jsonResponse({"status": "ok", "data": n})

@app.route('/run/ar/<resid>')
def run(resid):
    try:
        conn = db.connect()

        # Initialize select and data type
        select = 'select measure_ts, sum(confirmed) confirmed from "ENVDUV_COVID_1"."COVID_visual.db.data::COVIDTIMESERIES" where region like \'%China%\' group by measure_ts order by measure_ts;'
        dt = np.dtype([
        ("f2", object),
        ("f1", "int32"),
        ])

        # Run query
        n = db.select(conn, select, dt)
        
        y = n["f1"]

        y = n["f1"]
        z = n["f2"]

        c = y.shape[0]
        c2 = round(c/2) # train size

        tr_y = y[:c2]
        tt_y = y[c2:]

        tr_x = z[:c2]
        tt_x = z[c2:]
        res = AR(tr_x, tr_y, tt_x)
        db.insert(conn, z, res, 'confirmed', resid, None, None)

        return jsonResponse({"status": "OK", "data":{ "tr_x": tr_x.tolist(), "tt_x": tt_x.tolist(), "tr_y": tr_y.tolist(), "tt_y": tt_y.tolist()}})
    except :
        return traceback.format_exc()


if __name__ == '__main__':
    app.run(port=port)