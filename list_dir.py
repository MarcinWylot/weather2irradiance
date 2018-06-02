#! /usr/bin/python3
from urllib.request import Request, urlopen, urlretrieve
from bs4 import BeautifulSoup
import re

#urls=set()
def read_url(url):
#    url = url.replace(" ","%20")
	req = Request(url)
	a = urlopen(req).read()
	soup = BeautifulSoup(a, 'html.parser')
	x = soup.find_all('a')
	for i in x:
        #file_name = i.extract().get_text()
        #url_new = url + file_name
        #url_new = url_new.replace(" ","%20")
        #if(file_name[-1]=='/' and file_name[0]!='.'):
        #    read_url(url_new)
		_url = i.get('href')
		if(_url.endswith('/') and not _url.startswith('/data/gfs4/') and i.extract().get_text()):
#			if (_url.endswith('01/')):# or _url.endswith('04/') ): 
				read_url(url+_url)

		if(_url.endswith('grb2') and i.extract().get_text() and  re.match("gfs_4_[0-9]+_0000_0(1[1-8]|0[3-9]|21)", _url)):
			print(url+_url)
			#urls.add(url+_url)
        #print(i.extract().get_text())
        #print(i.get('href'))

read_url("https://nomads.ncdc.noaa.gov/data/gfs4/201701/")
read_url("https://nomads.ncdc.noaa.gov/data/gfs4/201702/")
read_url("https://nomads.ncdc.noaa.gov/data/gfs4/201703/")
read_url("https://nomads.ncdc.noaa.gov/data/gfs4/201704/")
read_url("https://nomads.ncdc.noaa.gov/data/gfs4/201705/")
read_url("https://nomads.ncdc.noaa.gov/data/gfs4/201706/")
read_url("https://nomads.ncdc.noaa.gov/data/gfs4/201707/")
read_url("https://nomads.ncdc.noaa.gov/data/gfs4/201708/")
read_url("https://nomads.ncdc.noaa.gov/data/gfs4/201709/")
read_url("https://nomads.ncdc.noaa.gov/data/gfs4/201710/")
read_url("https://nomads.ncdc.noaa.gov/data/gfs4/201711/")
read_url("https://nomads.ncdc.noaa.gov/data/gfs4/201712/")
read_url("https://nomads.ncdc.noaa.gov/data/gfs4/201801/")
read_url("https://nomads.ncdc.noaa.gov/data/gfs4/201802/")
read_url("https://nomads.ncdc.noaa.gov/data/gfs4/201803/")
read_url("https://nomads.ncdc.noaa.gov/data/gfs4/201804/")
#for url in urls:
#	print(url)

