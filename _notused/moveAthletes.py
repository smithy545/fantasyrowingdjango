import sqlite3
import re
from types import *

def sub(item):
    return re.sub(u'[\n\t]+', u'', item).strip()

def quotify(s):
    if type(s) == NoneType:
        return u'""'
    elif type(s) == ListType:
        return [quotify(x) for x in s]
    elif type(s) == DictType:
        temp = {}
        for key in s:
            temp[key] = quotify(s[key])
        return temp
    elif type(s) != UnicodeType:
        s = unicode(s)
    return u'"' + sub(s).strip() + u'"'

conn1 = sqlite3.connect("teams.db")
conn2 = sqlite3.connect("db.sqlite3")

c1 = conn1.cursor()
c2 = conn2.cursor()

for athlete in c1.execute("SELECT * FROM athlete;"):
    command = u"INSERT INTO runleague_athlete ('ranking','id', 'first_name', 'last_name', 'height', 'weight', 'hometown', 'high_school', 'school', 'year', 'age', 'major', 'side') VALUES("

    values = [quotify(athlete[0])]
    values += [quotify(x) for x in athlete]

    command += u",".join(values) + ");"
    c2.execute(command)

conn2.commit()
conn1.close()
conn2.close()
