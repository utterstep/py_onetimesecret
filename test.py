# -*- coding: UTF-8 -*-

__author__ = 'Step'
from onetimesecret import OneTimeSecret

o = OneTimeSecret("YOUR_EMAIL", "YOUR_OTS_APIKEY")
secret = o.share(u"Test")


print(o.retrieve_secret(secret[u"secret_key"]))


print(o.retrieve_meta(secret["metadata_key"]))
