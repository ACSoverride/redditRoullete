import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import random
import webbrowser
#
linklist = []
def function1():
    # ignoring the ssl certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode == ssl.CERT_NONE

    url = ("https://www.reddit.com")
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # getting the anchor tags and things that start with http
    tags = soup("a")
    for stuffs in tags:
        kringe = (stuffs.get('href', None))
        kringey = str(kringe)
        if kringey.startswith("https:") or kringey.startswith("http:") == (True):
            if kringey.startswith("https://www.redditinc.com") == (False):
                if kringey.startswith("https://www.reddithelp.com") == (False):
                    if kringey.startswith("about.reddit.com") == (False):
                        if kringey.startswith("https://www.reddit.com/help")== (False):
                            if kringey.startswith("https://www.reddit.com/login") == (False):
                                if kringey.startswith("https://www.reddit.com/coins") == (False):
                                    linklist.append(kringey)

    linktoopen = (random.choice(linklist))
    print("Reddit Roullete")
    print(linktoopen)
    webbrowser.open(linktoopen)
    input("Press enter to close")

def function2():
    try:
        function1()
    except:
        function2()
function2()
