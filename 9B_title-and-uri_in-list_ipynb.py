import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import json

ctx = ssl.create_default_context() # ssl - Secure Sockets Layer
ctx.check_hostname = False # get hostname to go false
ctx.verify_mode = ssl.CERT_NONE # to pass SSL without certificate

# get the URL to extract HTML so parsing that with BeautifulSoup
url = 'https://www.cia.gov/the-world-factbook/page-data/countries/page-data.json'
print("Opening the file connection...")

uh = urllib.request.urlopen(url, context=ctx) # <http.client.HTTPResponse at 0x2200d6b4888>
print("HTTP status", uh.getcode()) # Get the URL status

html = uh.read().decode() # to read and decode
print(f"Reading done. Total {len(html)} characters read. \n") # Get length of html

getjson = json.loads(html)

smaljson = getjson['result']['data']['countries']['edges']

smaljson2 = len(smaljson)
print(f"{smaljson2} arrays.")

theurl = 'https://www.cia.gov/the-world-factbook'

country_names=[]
country_url=[]

for idx, val in enumerate(smaljson):
    getjson2 = val['node']['title']
    
    getjson3 = val['node']['uri']
    mixgeturl = theurl + getjson3
    
    country_names.append(getjson2)
    country_url.append(mixgeturl)

temp1=country_names
temp2=country_url

temp1ln = len(temp1)
temp2ln = len(temp2)
print(f"{temp1ln} arrays.\n")
print(f"{temp2ln} arrays.\n")

print(temp1, "\n")
print(temp2)
