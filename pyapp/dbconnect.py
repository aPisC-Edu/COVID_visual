import sys
import os

from hdbcli import dbapi

connection = dbapi.connect('oktnb132.inf.elte.hu', 30015, os.environ.get('PY_USER'), os.environ.get('PY_PASS'))

#This statement prints true if the connection is successfully established
print(connection.isconnected())