import pycurl
from cStringIO import StringIO
import sys
import time
import socket
import json
import os

STATUS_OK = 0
STATUS_WARNING = 1
STATUS_ERROR = 2

MY_URL = "https://www.google.com"

c = pycurl.Curl()
c.setopt(c.URL, MY_URL)
c.setopt(c.FOLLOWLOCATION, True)

def monitor(success, url, api_key, app_key):
    if success:
        status = STATUS_OK
    else:
        status = STATUS_ERROR
    c2 = pycurl.Curl()
    c2.setopt(c2.URL, "https://app.datadoghq.com/api/v1/check_run?api_key={0}&application_key={1}".format(api_key, app_key))
    data = {
       "check": "check_http",
       "host_name": socket.gethostname(),
       "timestamp": int(time.time()),
       "status": status,
       "message": "Testing {0}".format(url),
       "tags": ["url:{0}".format(url)]
    }
    c2.setopt(c2.POSTFIELDS, json.dumps(data))
    c2.setopt(c2.HTTPHEADER, ["Content-type: application/json"])
    try:
        c2.perform()
        print c2.getinfo(c2.RESPONSE_CODE)
    finally:
        c2.close()
    
try:
    s = StringIO()
    c.setopt(pycurl.WRITEFUNCTION, s.write)
    c.perform()
    success = c.getinfo(c.RESPONSE_CODE) == 200
    monitor(success, sys.argv[1], os.environ["DATADOG_API_KEY"], os.environ["DATADOG_APP_KEY"])
finally:
    c.close()
