# -*- coding: UTF-8 -*-

__author__ = 'Step'
from onetimesecret import OneTimeSecret

o = OneTimeSecret("YOUR_EMAIL", "YOUR_OTS_APIKEY")
secret = o.share(u"Привет, Хабр")
# {u'updated': 1340611352,
# u'created': 1340611352,
# u'recipient': [],
# u'metadata_key': u'653lzljgwgj74ys6hvrpta2wmhaamrg', ### Ключ метаданных (просмотренно/нет, когда, запаролено ли и т.д.).
# Доступ к метаданным по ссылке вида https://onetimesecret.com/private/META_KEY
# u'metadata_ttl': 86400,
# u'secret_ttl': 86400,
# u'state': u'new',
# u'passphrase_required': False,
# u'ttl': 86400,
# u'secret_key': u'3ery270erhtk1gjsti90d70z5h8aqgd', ### Ключ секрета, доступ к самому
# по ссылке вида https://onetimesecret.com/secret/SECRET_KEY
#
# u'custid': u'anon'}

print o.retrieve_secret(secret[u"secret_key"])
# {u'secret_key': u'dtr7ixukiolpx1i4i87kahmhyoy2q65',
# u'value': u'Привет, Хабр'}

print o.retrieve_meta(secret["metadata_key"])
# {u'received': 1340731164,
# u'updated': 1340731164,
# u'created': 1340731159,
# u'recipient': [],
# u'metadata_key': u'qvu20axsugif3fo4zjas5ujvp1q9k75',
# u'metadata_ttl': 86398,
# u'state': u'received', ### Сообщение было прочитано
# u'ttl': 86400,
# u'custid': u'anon'}
