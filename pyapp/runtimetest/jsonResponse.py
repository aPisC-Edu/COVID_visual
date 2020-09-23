from flask import Response
import json
from bson import json_util

def jsonResponse(data):
  return Response(json.dumps(data, default=json_util.default), mimetype='application/json')