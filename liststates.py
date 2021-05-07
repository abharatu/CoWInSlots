import urllib.request, json, ssl, sys, getopt

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"

context = ssl._create_unverified_context() # Prevent Verification of SSL Ceritificates as it does not work insome systems
req = urllib.request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    },
)

with urllib.request.urlopen(req,context=context) as response:
   data = json.loads(response.read())
   for state in data['states']:
       print(bcolors.OKGREEN + str(state['state_id'])  + bcolors.ENDC + ": " + str(state['state_name']))