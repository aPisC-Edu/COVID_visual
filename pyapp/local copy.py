import os
import sys
from hdbcli import dbapi
import numpy as np
import matplotlib
import math
import matplotlib.pyplot as plt

from dbconnect import dbconnect
from dbselect import dbselect
from Algorithms.LR import LR
from Algorithms.ExpR import ExpR
from Algorithms.GaussR import GaussR


# Initialize connection
conn = dbconnect()

# Initialize select and data type
select = 'select measure_ts, sum(confirmed) confirmed from "ENVDUV_COVID_1"."COVID_visual.db.data::COVIDTIMESERIES" where region like \'%China%\' group by measure_ts order by measure_ts;'
dt = np.dtype([
  ("f2", object),
  ("f1", "int32"),
])

# Run query
n = dbselect(conn, select, dt)

# close connection
conn.close()


# Load/split your data
y = n["f1"]
x = np.arange(y.shape[0])
y2 = np.log(y)
y3 = -y2
#train, test = train_test_split(y, train_size=20)


# Visualize the forecasts (blue=train, green=forecasts)
#plt.plot(x, y2)
#plt.plot(x, np.polyval(p3, x))
#plt.plot(x, np.polyval(p4, x))
#plt.show()


plt.plot(x,y)

x2 = np.arange(10)
#plt.plot(x2, LR(x, y, x2)) # linear
#plt.plot(x2, ExpR(x, y, x2)) # exponential
#plt.plot(x2, GaussR(x, y, x2)) # Gauss
a = 0.00051
plt.plot(x2, LR(x, np.exp(a * y), x2) )
plt.plot(x2, np.log(LR(x, np.exp(a * y), x2)) / a)

#plt.plot(x,  np.exp(-( p4[0] * np.power(x, 4) + p4[1] * np.power(x, 3) + p4[2] * np.power(x, 2) + p4[3] * x + p4[4] ) )) # gauss quad
plt.show()