import urllib2
import re
import random

lastNameUrl = "http://www2.census.gov/topics/genealogy/1990surnames/dist.all.last"
firstNameUrl = "http://deron.meranda.us/data/census-derived-all-first.txt"

response = urllib2.urlopen(lastNameUrl)
html = response.read()
lastNames = [re.match(r"(\w+)", s).group(0) for s in html.splitlines()]
response = urllib2.urlopen(firstNameUrl)
html = response.read()
firstNames = [re.match(r"(\w+)", s).group(0) for s in html.splitlines()]

for name in firstNames:
    print name.lower().capitalize()+" "+random.choice(lastNames).lower().capitalize()
