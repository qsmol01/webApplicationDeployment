import urllib2
import base64
import ssl
from bs4 import BeautifulSoup

request = urllib2.Request("https://www.kona.com/sidekiq")
base64string = base64.encodestring('%s:%s' % ("kona", "cagan1")).replace('\n', '')
context = ssl._create_unverified_context()
request.add_header("Authorization", "Basic %s" % base64string)
result = urllib2.urlopen(request, context=context)

soup = BeautifulSoup(result, 'html.parser')
t = soup.find_all('a', href="/sidekiq/queues")
count = float(filter(str.isdigit, str(t)))