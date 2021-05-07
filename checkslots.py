import datetime,urllib.request, json, ssl, getopt, sys
from pync import Notifier
today = datetime.datetime.now()

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
districtid = 294 # Default is BBMP
try:
    # Define the getopt parameters
    opts, args = getopt.getopt(argv, 'd:', ['district'])
    # Check if the options' length is 2 (can be enhanced)
    if len(opts) == 0 and len(opts) > 1:
      print (bcolors.WARNING + 'usage: selectdistrict.py -d' + bcolors.ENDC)
    else:
      # Iterate the options and get the corresponding values
      for opt, arg in opts:
          if opt == '-d':
              districtid = arg
except getopt.GetoptError:
    # Print something useful
    print (bcolors.WARNING + 'usage: selectdistrict.py -d' + bcolors.ENDC)
    sys.exit(2)

#Public URL is not complete using sessions url instead
#url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+config.districtid+"&date="+today.strftime("%d-%m-%Y")
url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id="+str(districtid)+"&date="+today.strftime("%d-%m-%Y")
#print(url)
context = ssl._create_unverified_context() # Prevent Verification of SSL Ceritificates as it does not work insome systems
req = urllib.request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    },
)
try:
    gotdata=False
    with urllib.request.urlopen(req,context=context) as response:
        data = json.loads(response.read())
        for center in data['centers']:
            gotdata=True
            for session in center['sessions']:
                if session['min_age_limit'] == 18 and session["available_capacity"]>0:
                    print("-------Start-------")
                    text="Pincode:"+str(center['pincode'])+" Date:"+session["date"]+"\nvaccine:"+session["vaccine"]
                    title="CoWin: "+str(session["available_capacity"])+" slots available in "+center['name']
                    print(title+"\n"+text)
                    print("-------End-------")
                    Notifier.notify(text,title=title,group="CoWin",sound='Ping', open='https://selfregistration.cowin.gov.in/')
                    quit()
    if gotdata == True:
        print(bcolors.OKGREEN + "Checking on: " + bcolors.WARNING +str(today) + bcolors.ENDC)
    else:
        print(bcolors.WARNING + "Error on: " + bcolors.ENDC + str(today))    
except urllib.error.HTTPError:
    print(bcolors.WARNING + "Got 401 Error on: " + bcolors.ENDC + str(today))    