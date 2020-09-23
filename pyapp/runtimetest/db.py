from cfenv import AppEnv
from hdbcli import dbapi
import numpy as np

env = AppEnv()
hana = env.get_service(name='ENVDUV-cb6znz6p8ij57f78-COVID_visual-hdi_db')

def connect():
  conn = dbapi.connect(address=hana.credentials['host'], port=int(hana.credentials['port']), user=hana.credentials['user'], password=hana.credentials['password'])
  return conn

  
def select(conn, select, dt):
  cursor = conn.cursor()
  cursor.execute(select)
  res = cursor.fetchall()
  cursor.close()
  n = np.array([tuple(i) for i in res], dt)
  return n


def insert(conn, x, y, col, resid, pro, reg,):
  sql = 'INSERT INTO "ENVDUV_COVID_1"."COVID_visual.db.data::COVID_RESULT" (province, region, measure_ts, '+ col +', result_id ) VALUES (?, ?, ?, ?, ?);'
  cursor = conn.cursor()
  for i in range(len(x)):
    cursor.execute(sql, (pro, reg, x[i], y[i], 'ENVDUV_T1'))
  cursor.close()
  pass