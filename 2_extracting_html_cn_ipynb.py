import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context() # ssl - Secure Sockets Layer
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# get the URL to extract HTML so parsing that with BeautifulSoup
url = 'https://www.cia.gov/the-world-factbook/countries/china/'
print("Opening the file connection...")

uh = urllib.request.urlopen(url, context=ctx)
print("HTTP status",uh.getcode())

html = uh.read().decode()
print(f"Reading done. Total {len(html)} characters read.", "\n")

soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())
