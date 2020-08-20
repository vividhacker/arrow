import zipfile
import itertools
import string 
from threading import Thread
from datetime import datetime
import hashlib

myLetters = string.punctuation, string.ascii_letters, string.digits

# Crack a hash
def crack_hash(hash):
  starttime = datetime.now()
  rainbowtable = open('rtable.txt', "r")
  for line in rainbowtable.readlines():
    hashpwd = line.split('#', 1)
    if hash == hashpwd[0]:
      print('Success: Password is: '+ hashpwd[1])
      print('Task completed in '+str(datetime.now-starttime)+' seconds')

#Rainbowtable Generator  
def gen_rbtable(state="dict",hashalgo="sha512"):
  passwords = open('tuscl.txt', 'r')
  output = open("rtable.txt", "w")
  starttime = datetime.now()
  if hashalgo == "sha512":
    if state == "dict":
      for line in passwords.readlines(): 
        pwd = line.strip('\n')
        hash = hashlib.sha512(str.encode(pwd))
        output.write(hash.hexdigest() + "#"+ str(pwd) + "\n")
        stoptime = datetime.now() - starttime
        print(str(stoptime))
      output.close()
      passwords.close()
    if state == "brute":
      output = open("rtable.txt", "w")
      for i in range(1,400):
        for char in map(''.join, itertools.product(myLetters, repeat=i)):
          hash = hashlib.sha512(str.encode(char))
          output.write(hash.hexdigest() + "#"+ pwd + "\n")
          stoptime = datetime.now() - starttime
          print(str(stoptime))
  if hashalgo == "md5":
    if state == "dict":
      for line in passwords.readlines():
        pwd = line.strip('\n')
        hash = hashlib.md5(str.encode(pwd))
        output.write(hash.hexdigest() + "#"+ pwd + "\n")
        stoptime = datetime.now() - starttime
        print(str(stoptime))
      output.close()
      passwords.close()
      
    if state == "brute":
      output = open("rtable.txt", "w")
      for i in range(1,400):
        for char in map(''.join, itertools.product(myLetters, repeat=i)):
          hash = hashlib.md5(str.encode(char))
          output.write(hash.hexdigest() + "#"+ pwd + "\n")
          stoptime = datetime.now() - starttime
          print(str(stoptime))
        
  if hashalgo == "sha256":
    if state == "dict":
      for line in passwords.readlines():
        pwd = line.strip('\n')
        hash = hashlib.sha256(str.encode(pwd))
        output.write(hash.hexdigest() + "#"+ pwd + "\n")
        stoptime = datetime.now() - starttime
        print(str(stoptime))
      output.close()
      passwords.close()
    if state == "brute":
      output = open("rtable.txt", "w")
      for i in range(1,400):
        for char in map(''.join, itertools.product(myLetters, repeat=i)):
          hash = hashlib.sha256(str.encode(char))
          output.write(hash.hexdigest() + "#"+ pwd + "\n")
          stoptime = datetime.now() - starttime
          print(str(stoptime))
          
gen_rbtable("brute", "sha512")