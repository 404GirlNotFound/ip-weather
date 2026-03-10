from tinydb import TinyDB
# pip install tinydb

db=TinyDB('obiskovalci.json')

db.insert({'IP': '192.168.0.1', 'drzava': "Slovenia", "temp":20})

print(db.all())

#request.heders mors ze od prej znat