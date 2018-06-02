#! /bin/bash

# drop database energy
#create database energy WITH SHARD DURATION 1000w
#influx --database energy --precision s --import --path ./XXX.inxlux #producka i moc
#influx --database energy --precision s --import --path ./weather_pvlib.influx
# DML
# CONTEXT-DATABASE: energy
# CONTEXT-RETENTION-POLICY: autogen


#pv_id = '189' #google.maps.LatLng(52.1105687,20.0631030) TBA_PV
#pv_id = '13' #google.maps.LatLng(53.1573740,16.6280650) putas

wgrib2="$HOME/energy/grib2/wgrib2/wgrib2"
file1=$1
#fields='-match '':((VIS|TMP|SUNSD|APCP|APCP|DSWRF|ALBDO).*(:surface:))|(:(PWAT|CWAT|RH).*(:entire))|(:(TCDC).*(cloud))'' '
lon='-lon 53.165573 16.611314'
lon='-lon 53.1573740 16.6280650 -lon 52.1105687 20.0631030'


#$wgrib2 $file1 -s -vt $lon 
#exit
#curl $file1 -s
#wget -O - -i ./grib_list_test | 
#rm -f ./weather$1.raw
for f in `cat  /home/martin/Dropbox/projekty/energetyka/data/rawData/grib_lists/grib_list$1`; do
#	echo $f
	curl -O --retry 999 $f  
#| $wgrib2 - -s -vt $lon $fields >> ./weatheri$1.raw
	sleep 2
	# awk -f awk FS=:
done
#$wgrib2 - -s -vt $lon $fields | awk -f awk FS=: > ./weather.influx
