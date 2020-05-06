import os
import sys
from hdbcli import dbapi
import numpy as np
import matplotlib
import math
import matplotlib.pyplot as plt


conn_data = {
    'server' : 'oktnb132.inf.elte.hu',
    'port': 30015,
    'user': 'PY_TU',
    'password': os.environ.get('PY_PASS')
}

conn = dbapi.connect(conn_data['server'], conn_data['port'], conn_data['user'], conn_data['password'])

cursor = conn.cursor()
#cursor.execute("select CURRENT_UTCTIMESTAMP from DUMMY", {})
cursor.execute('select measure_ts, sum(confirmed) confirmed from "COVID_VISUAL_HDI_DB_1"."COVID_visual.db.data::COVIDTIMESERIES" where region like \'%China%\' group by measure_ts order by measure_ts;')
res = cursor.fetchall()
cursor.close()
conn.close()

dt = np.dtype(np.unicode_, 16)

n = np.array([tuple(i) for i in res], np.dtype([
  ("f2", object),
  ("f1", "int32"),
]))

#fig, ax = plt.subplots()
#ax.plot(n["f2"], n["f1"])

#plt.show()



# Load/split your data
y = n["f1"]
x = np.arange(y.shape[0])
y2 = np.log(y)
y3 = -y2
#train, test = train_test_split(y, train_size=20)

# Fit your model
p1 = np.polyfit(x, y, 1) # for linear fitting
p2 = np.polyfit(x, y2, 1) # for exponential fitting
p3 = np.polyfit(x, y3, 2) # for gauss fitting


# Visualize the forecasts (blue=train, green=forecasts)
plt.plot(x, y, c='green')
plt.plot(x, p1[0] * x + p1[1], c='blue') # linear
plt.plot(x, math.exp(p2[1]) * np.exp(x * p2[0]) , c='blue') # exponential
plt.plot(x, math.exp(p3[2]) * np.exp(-x^2 * p3[0] - x*p3[1]), c='blue') # gauss
plt.show()