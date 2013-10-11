#!/usr/bin/python
#Simple script used to check the availability of an API
import requests
import socket, errno, sys

# Timeout in second
timeout = 5
# List of routes to check
routes = ['app/version/', 'term', 'status', 'app/version/dev']
# API Base URL
url = 'http://api.getswipefeed.com/'


# Go through every route of an API to check if everything is up
def checkAPI():
  failed = []
  for route in routes:
    try:
        r = requests.get(url + route, timeout=timeout)
        if r.status_code != 200:
          failed.append(route)
    except:
      failed.append(route);

  # Do we had error(s) ?
  if len(failed) != 0:
    sys.exit(str(failed) + ' wasn\'t available') # ERROR
  else:
    sys.exit(0) # ALL GOOD

# Main
checkAPI()
