from docassemble.base.util import *
import requests
import sys
      
def print_api():

  headers = {'X-API-Key': 'KKKioU5R9xsXIRt2sqfSD0Z1lGyEaTkv'}

  try:
    r = requests.get('https://13.235.171.91/api/list', headers=headers, verify=False)
    r.raise_for_status()
    info = r.json()
    # Process the retrieved data
  except requests.exceptions.HTTPError as err:
    return(f"HTTP error occurred: {err}")
    sys.exit(1)
  except requests.exceptions.RequestException as e:
    return(f"Request failed: {e}")
    sys.exit(1)