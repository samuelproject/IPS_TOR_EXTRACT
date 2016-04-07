#!/usr/bin/python
#Author : @saamux /Twitter
#Github : https://github.com/samuelproject

import requests
from bs4 import BeautifulSoup

def ips_tor():
	web_ips_tor = requests.get("http://torstatus.blutmagie.de/").text
	response = BeautifulSoup(web_ips_tor, 'html.parser')
	listIPsTor = open('tor_ips.txt','ab+')
	cont = 0
	readIps = listIPsTor.readlines()
	for ip in response.find_all("a", {"class":"who"}):
		if ip.string +"\n" in readIps:
			pass
		else:
			cont+=1
			print ip.string
			listIPsTor.write(ip.string+'\n')

	if cont > 0:
		print "Agregando un total de %d direcciones IP de TOR..." %cont
	else:
		print "No se han detecado nuevas direcciones IPs  de TOR"	



if __name__ == '__main__':
	ips_tor()
