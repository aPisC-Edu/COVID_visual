import os
import sys
from hdbcli import dbapi
import numpy as np
import matplotlib
import math
import matplotlib.pyplot as plt

from dbconnect import dbconnect
from dbselect import dbselect
from dbinsert import dbinsert
from Algorithms.LR import LR
from Algorithms.ExpR import ExpR
from Algorithms.GaussR import GaussR
from Algorithms.AR import AR
from Algorithms.MA import MA


# Initialize connection
conn = dbconnect()

sql = 'INSERT INTO "ENVDUV_COVID_1"."COVID_visual.db.data::COVID_RESULT" (result_id) VALUES (?)'
cursor = conn.cursor()
#cursor.execute(sql, 'ENVDUV_T1')
cursor.close()


# Initialize select and data type
select = 'select measure_ts, sum(confirmed) confirmed from "ENVDUV_COVID_1"."COVID_visual.db.data::COVIDTIMESERIES" where region like \'%China%\' group by measure_ts order by measure_ts;'
dt = np.dtype([
  ("f2", object),
  ("f1", "int32"),
])

# Run query
n = dbselect(conn, select, dt)


# Load/split your data
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

# close connection
conn.close()

plt.plot(z, res)



#plt.plot(x,  np.exp(-( p4[0] * np.power(x, 4) + p4[1] * np.power(x, 3) + p4[2] * np.power(x, 2) + p4[3] * x + p4[4] ) )) # gauss quad
plt.show()