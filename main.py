import urllib.request
from bs4 import BeautifulSoup

#get word list from txt

for item in wordlist:
    resp = urllib.request.urlopen("http://http://en.wikipedia.org/wiki/{1}".format())
    soup = BeautifulSoup(resp.read(), from_encoding=resp.info().get_param('charset'))
