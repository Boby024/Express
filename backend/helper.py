import hashlib

def prepareforJSON(listFromDB, modeller):
  modeledList = []
  for first in listFromDB:
    modeledList.append(dict(zip(modeller, first)))
  return modeledList

def encodePASSWD(password):
  ps = password.encode()
  newpasswd= hashlib.sha3_512(ps).hexdigest()
  return newpasswd


