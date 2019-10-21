import hashlib

def passwd(password):
  ps = password.encode()
  newpasswd= hashlib.sha3_512(ps).hexdigest()
  return newpasswd

k= passwd("username")

if passwd("username") == k:
  print(True)
else:
  print(False)

l= passwd("oigjewogijiewukshbjfbdskfvbaj2367t382732oi2bjhkfdbvmyf bv827z8273r8o2klfhwe")
print(l)
print( len(l) )
