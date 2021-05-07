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

# Get the arguments from the command-line except the filename
argv = sys.argv[1:]
stateid = 16 # Default is Karnataka
try:
    # Define the getopt parameters
    opts, args = getopt.getopt(argv, 's:', ['state'])
    # Check if the options' length is 2 (can be enhanced)
    if len(opts) == 0 and len(opts) > 1:
        print (bcolors.WARNING + 'usage: listdistricts.py -s' + bcolors.ENDC)
    else:
      # Iterate the options and get the corresponding values
      for opt, arg in opts:
          if opt == '-s':
              stateid = arg
except getopt.GetoptError:
    # Print something useful
    print (bcolors.WARNING + 'usage: listdistricts.py -s' + bcolors.ENDC)
    sys.exit(2)

print("Selected State Id is: " + bcolors.OKGREEN + str(stateid) + bcolors.ENDC)

url = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/"+str(stateid)

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
   for district in data['districts']:
       print(bcolors.OKGREEN + str(district['district_id'])  + bcolors.ENDC + ": " + str(district['district_name']))