import numpy as np

def dbselect(conn, select, dt):
  cursor = conn.cursor()
  cursor.execute(select)
  res = cursor.fetchall()
  cursor.close()
  n = np.array([tuple(i) for i in res], dt)
  return n