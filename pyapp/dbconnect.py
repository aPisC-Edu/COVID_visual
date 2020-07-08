import sys
import os

from hdbcli import dbapi

def dbconnect():
  conn_data = {
    'server' : 'oktnb132.inf.elte.hu',
    'port': 30015,
    'user': 'PY_TU',
    'password': os.environ.get('PY_PASS')
  }
  return dbapi.connect(conn_data['server'], conn_data['port'], conn_data['user'], conn_data['password'])
