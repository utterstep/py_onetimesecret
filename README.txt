Thin Python 3.7 binding for onetimesecret.com API.
Unicode-safe.
Description of API itself you can find here: https://onetimesecret.com/docs/api

Usage:

from onetimesecret import OneTimeSecret

o = OneTimeSecret("YOUR_EMAIL", "YOUR_OTS_APIKEY")
secret = o.share(u"test")

print o.retrieve_secret(secret["secret_key"])
# {u'secret_key': u'dtr7ixukiolpx1i4i87kahmhyoy2q65',
# u'value': u'test'}


____________
Feel free to contact me in any case: 8uk.8ak@gmail.com