import zipfile
import itertools
import string
from threading import Thread
from datetime import datetime
import hashlib
"""

? How to optimate the bruteforcer ?
ToDo Webcracker schreiben ToDo

"""


asciis = string.ascii_lowercase[::1] + string.ascii_uppercase[::1]
myLetters = string.digits + asciis  + string.punctuation
fpwd = ""

def crack(zip, pwd, starttime):
  try:
    zip.extractall(pwd=str.encode(pwd))
    print('Success: Password is '+ pwd)
    endtime = datetime.now() - starttime
    print('Needed ', str(endtime), ' seconds')

  except Exception:
    pass

 
#bruteforce attack for zipfiles
def bruteforce(zipFile):
  starttime = datetime.now()
  for i in range(1,400):
    for char in map(''.join, itertools.product(myLetters, repeat=i)):
      t = Thread(target=crack, args=(zipFile, char))
      t.start()
def dictionary(zipFile):
  starttime = datetime.now()
  passwords = open('tuscl.txt', 'r')
  for line in passwords.readlines():
    pwd = line.strip('\n')
    t = Thread(target=crack, args=(zipFile, pwd, starttime))
    t.start()