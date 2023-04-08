import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com')
except urllib.error.URLError:
    print('\33[1;31mNão está acessivel.\33[m')
else:
    print('\33[1;36mEstá acessivel.\33[m')
