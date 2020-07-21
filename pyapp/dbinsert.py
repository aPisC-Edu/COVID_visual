def dbinsert(conn, x, y, col, resid, pro, reg,):
  sql = 'INSERT INTO "ENVDUV_COVID_1"."COVID_visual.db.data::COVID_RESULT" (province, region, measure_ts, '+ col +', result_id ) VALUES (?, ?, ?, ?, ?);'
  cursor = conn.cursor()
  for i in range(len(x)):
    cursor.execute(sql, (pro, reg, x[i], y[i], 'ENVDUV_T1'))
  cursor.close()

  pass