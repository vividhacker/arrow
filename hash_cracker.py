import time
stime = time.time()
from itertools import product
from string import ascii_letters, digits, punctuation
from threading import Thread
from datetime import datetime
from hashlib import sha256,sha512,md5, new

sectime = time.time()
sectime = sectime - stime
print("Time to import libs: ", sectime)







myLetters =  ascii_letters, digits, punctuation


# Crack a hash
def crack_hash(hash, rb_table):
  starttime = datetime.now()
  rainbowtable = open(rb_table, "r")
  for line in rainbowtable.readlines():
    hashpwd = line.split('#', 1)
    if hash == hashpwd[0]:
      print('Success: Password is: '+ hashpwd[1] + "  ;  The hash was: "+ hash)
      print('Task completed in '+str(datetime.now-starttime)+' seconds')

#Rainbowtable Generator  
def gen_rbtable(state="dict",hash_algo="sha512",dict_path="lst/john.txt"):
  dict_path = str(dict_path)
  state = str(state)
  hash_algo = str(hash_algo)

  rb_output = "./rb_tables/"+dict_path.split('/')[int(len(dict_path.split('/'))-1)].replace('.txt', '')+'_'+hash_algo+'.txt'
  rb_output = rb_output.replace(' ', '')
  passwords = open(dict_path, 'r')
  output = open(rb_output, "w")
  starttime = datetime.now()
  if hash_algo == "sha512":
    if state == "dict":
      for line in passwords.readlines():
        global pwd
        pwd = line.strip('\n')
        hash = sha512(str.encode(pwd))
        output.write(hash.hexdigest() + "#"+ str(pwd) + "\n")
        stoptime = datetime.now() - starttime
        print(str(stoptime))
      output.close()
      passwords.close()
    if state == "brute":
      output = open('../rb_table.txt', "a")
      for i in range(1,64):
        for char in map(''.join, product(myLetters, repeat=i)):
          hash = sha512(str.encode(char))
          output.write(hash.hexdigest() + "#"+ char + "\n")
          stoptime = datetime.now() - starttime
          print(str(stoptime))
  if hash_algo == "md5":
    if state == "dict":
      for line in passwords.readlines():
        pwd = line.strip('\n')
        hash = md5(str.encode(pwd))
        output.write(hash.hexdigest() + "#"+ pwd + "\n")
        stoptime = datetime.now() - starttime
        print(str(stoptime))
      output.close()
      passwords.close()
      
    if state == "brute":
      output = open('../rb_table.txt', "a")
      for i in range(1,64):
        for char in map(''.join, product(myLetters, repeat=i)):
          hash = md5(str.encode(char))
          output.write(hash.hexdigest() + "#"+ char + "\n")
          stoptime = datetime.now() - starttime
          print(str(stoptime))
  if hash_algo == "sha256":
    if state == "dict":
      for line in passwords.readlines():
        pwd = line.strip('\n')
        hash = sha256(str.encode(pwd))
        output.write(hash.hexdigest() + "#"+ pwd + "\n")
        stoptime = datetime.now() - starttime
        print(str(stoptime))
      output.close()
      passwords.close()
    if state == "brute":
      output = open('../rb_table.txt', "a")
      for i in range(1,64):
        for char in map(''.join, product(myLetters, repeat=i)):
          hash = sha256(str.encode(char))
          output.write(hash.hexdigest() + "#"+ char + "\n")
          stoptime = datetime.now() - starttime
          print(str(stoptime))


gen_rbtable("dict", 'sha512', 'lst/john.txt')