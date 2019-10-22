import geventcurl as pycurl
from cStringIO import StringIO
from gevent.pool import Group


urls = ['www.gevent.org', 'www.google.com', 'www.python.org']


def get(url):
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    output = StringIO()
    c.setopt(c.WRITEFUNCTION, output.write)
    c.perform()
    result = output.getvalue()
    print url, `result[:50]`
    c.close()

g = Group()
for url in urls:
    g.spawn(get, url)
g.join()

