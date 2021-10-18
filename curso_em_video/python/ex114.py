
import urllib.request

try:
    a = urllib.request.urlopen('http://google.com')
except:
    print("Couldn't reach site!")
else:
    print('site is available')
    print(a.read())
