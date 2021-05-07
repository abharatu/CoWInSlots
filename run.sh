echo "We are in $PWD"
python="python3"
$python liststates.py
read -p $'Select State (\e[32m16\e[0m:)' stateid
if [ -n $stateid ]
then
    stateid=16
fi
$python listdistricts.py -s $stateid
read -p $'Select District (\e[32m294\e[0m:)' districtid
if [ -n $districtid ]
then
    districtid=294
fi
echo "\033[91mPlease be responsible setting the frequency you may slow down the server if its too small!\033[0m"
read -p $'Select Frequency in Seconds (\e[32m30\e[0m:)' freq
if [ -n $freq ]
then
    freq=30
fi
while true ; do ($python $PWD/checkslots.py -d $districtid); sleep $freq; done