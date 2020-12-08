import time
<<<<<<< HEAD
=======
stime = time.time()
>>>>>>> 03176a839c3b76be4dd017fbeb5524c76171115a
from itertools import product
from string import ascii_letters, digits, punctuation
from threading import Thread
from datetime import datetime
<<<<<<< HEAD
from hashlib import sha1, sha224, sha256, sha384, sha512,md5, new
from os import path

=======
from hashlib import sha256,sha512,md5, new

sectime = time.time()
sectime = sectime - stime
print("Time to import libs: ", sectime)
>>>>>>> 03176a839c3b76be4dd017fbeb5524c76171115a







myLetters =  ascii_letters, digits, punctuation


# Crack a hash
def crack_hash(hash, rb_table):
  starttime = datetime.now()
  rainbowtable = open(rb_table, "r")
  for line in rainbowtable.readlines():
    hashpwd = line.split('#', 1)
    if hash == hashpwd[0]:
<<<<<<< HEAD
      return hashpwd[1]

#cracking multiple hashes
def multi_crack(hash_path="", out_path="output.txt", rbt_path="./lst/john.txt"):
  output_file = open(out_path, 'w')
  hash_file = open(hash_path, 'r')
  for line in hash_file.readlines():
    output_file.write(crack_hash(line.strip('\n'), rbt_path))
=======
      print('Success: Password is: '+ hashpwd[1] + "  ;  The hash was: "+ hash)
      print('Task completed in '+str(datetime.now-starttime)+' seconds')
>>>>>>> 03176a839c3b76be4dd017fbeb5524c76171115a

#Rainbowtable Generator  
def gen_rbtable(state="dict",hash_algo="sha512",dict_path="lst/john.txt"):
  dict_path = str(dict_path)
  state = str(state)
  hash_algo = str(hash_algo)

  rb_output = "./rb_tables/"+dict_path.split('/')[int(len(dict_path.split('/'))-1)].replace('.txt', '')+'_'+hash_algo+'.txt'
  rb_output = rb_output.replace(' ', '')
<<<<<<< HEAD
  if path.exists(rb_output) == True:
    print('Rainbowtable already exists')
  else:
    passwords = open(dict_path, 'r', errors="ignore")
    output = open(rb_output, "w", errors="ignore")
    starttime = datetime.now()

    #implementation of different hashalgorithms
    if hash_algo == "sha1":
      if state == "dict":
        for line in passwords.readlines():
          pwd = line.strip('\n')
          hash = sha1(str.encode(pwd))
          output.write(hash.hexdigest() + "#"+ pwd + "\n")

        stoptime = datetime.now() - starttime
        print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")
        output.close()
        passwords.close()

      if state == "brute":
        output = open('../rb_table.txt', "a")
        for i in range(1,64):
          for char in map(''.join, product(myLetters, repeat=i)):
            hash = sha1(str.encode(char))
            output.write(hash.hexdigest() + "#"+ char + "\n")

          stoptime = datetime.now() - starttime
          print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")
        output.close()
        passwords.close()
    
    elif hash_algo == "sha256":

      if state == "dict":

        for line in passwords.readlines():

          pwd = line.strip('\n')
          hash = sha256(str.encode(pwd))
          output.write(hash.hexdigest() + "#"+ pwd + "\n")
        stoptime = datetime.now() - starttime
        print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()

      if state == "brute":

        output = open('../rb_table.txt', "a")
        for i in range(1,64):

          for char in map(''.join, product(myLetters, repeat=i)):
            hash = sha256(str.encode(char))
            output.write(hash.hexdigest() + "#"+ char + "\n")
          stoptime = datetime.now() - starttime
          print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()

    elif hash_algo == "sha384":

      if state == "dict":

        for line in passwords.readlines():

          pwd = line.strip('\n')
          hash = sha384(str.encode(pwd))
          output.write(hash.hexdigest() + "#"+ str(pwd) + "\n")
        stoptime = datetime.now() - starttime
        print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()

      if state == "brute":

        output = open('../rb_table.txt', "a")
        for i in range(1,64):

          for char in map(''.join, product(myLetters, repeat=i)):
            hash = sha384(str.encode(char))
            output.write(hash.hexdigest() + "#"+ char + "\n")
          stoptime = datetime.now() - starttime
          print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")
          
          output.close()
          passwords.close()

    elif hash_algo == "sha512":

      if state == "dict":

        for line in passwords.readlines():

          pwd = line.strip('\n')
          hash = sha512(str.encode(pwd))
          output.write(hash.hexdigest() + "#"+ str(pwd) + "\n")
        stoptime = datetime.now() - starttime
        print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()

      if state == "brute":

        output = open('../rb_table.txt', "a")
        for i in range(1,64):

          for char in map(''.join, product(myLetters, repeat=i)):
            hash = sha512(str.encode(char))
            output.write(hash.hexdigest() + "#"+ char + "\n")
          stoptime = datetime.now() - starttime
          print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")
          
          output.close()
          passwords.close()

      if state == "brute":
        output = open('../rb_table.txt', "a")
        for i in range(1,64):
          for char in map(''.join, product(myLetters, repeat=i)):
            hash = sha512(str.encode(char))
            output.write(hash.hexdigest() + "#"+ char + "\n")
          stoptime = datetime.now() - starttime
          print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")
    
    elif hash_algo == "md5":
      
      if state == "dict":
        
        for line in passwords.readlines():

          pwd = line.strip('\n')
          hash = md5(str.encode(pwd))
          output.write(hash.hexdigest() + "#"+ pwd + "\n")
        stoptime = datetime.now() - starttime
        print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()
        
      if state == "brute":

        output = open('../rb_table.txt', "a")
        for i in range(1,64):
          
          for char in map(''.join, product(myLetters, repeat=i)):
            hash = md5(str.encode(char))
            output.write(hash.hexdigest() + "#"+ char + "\n")
          stoptime = datetime.now() - starttime
          print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()

    elif hash_algo == "ntlm":

      if state == "dict":

        for line in passwords.readlines():

          pwd = line.strip('\n')
          hash = new('md4', pwd.encode('utf-16le'))
          output.write(hash.hexdigest() + "#"+ pwd + "\n")
        stoptime = datetime.now() - starttime
        print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()
    
      if state == "brute":

        output = open('../rb_table.txt', "a")
        for i in range(1,64):

          for char in map(''.join, product(myLetters, repeat=i)):

            hash = new('md4', char.encode('utf-16le'))
            output.write(hash.hexdigest() + "#"+ char + "\n")
          stoptime = datetime.now() - starttime
          print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()

#generating example files with hashes from dictionaries
def gen_example_hashes(state="dict",hash_algo="sha512",dict_path="lst/john.txt"):
  dict_path = str(dict_path)
  state = str(state)
  hash_algo = str(hash_algo)

  rb_output = "./example_hashfiles/"+dict_path.split('/')[int(len(dict_path.split('/'))-1)].replace('.txt', '')+'_'+hash_algo+'.txt'
  rb_output = rb_output.replace(' ', '')
  if path.exists(rb_output) == True:
    print('the example-hashfile already exists')
  else:
    passwords = open(dict_path, 'r',errors="ignore")
    output = open(rb_output, "w", errors="ignore")
    starttime = datetime.now()

    #implementation of different hashalgorithms
    if hash_algo == "sha1":
      if state == "dict":
        for line in passwords.readlines():
          pwd = line.strip('\n')
          hash = sha1(str.encode(pwd))
          output.write(hash.hexdigest()+ '\n')
        stoptime = datetime.now() - starttime
        print("Finished example-Creation in: "+str(stoptime)+" seconds")
        output.close()
        passwords.close()
      if state == "brute":
        output = open('../rb_table.txt', "a")
        for i in range(1,64):
          for char in map(''.join, product(myLetters, repeat=i)):
            hash = sha1(str.encode(char))
            output.write(hash.hexdigest() + "#"+ char + "\n")
          stoptime = datetime.now() - starttime
          print("Finished example-Creation in: "+str(stoptime)+" seconds")
        output.close()
        passwords.close()
    
    elif hash_algo == "sha256":

      if state == "dict":

        for line in passwords.readlines():

          pwd = line.strip('\n')
          hash = sha256(str.encode(pwd))
          output.write(hash.hexdigest()+ '\n')
        stoptime = datetime.now() - starttime
        print("Finished example-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()

      if state == "brute":

        output = open('../rb_table.txt', "a")
        for i in range(1,64):

          for char in map(''.join, product(myLetters, repeat=i)):
            hash = sha256(str.encode(char))
            output.write(hash.hexdigest()+ '\n')
          stoptime = datetime.now() - starttime
          print("Finished example-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()

    elif hash_algo == "sha384":

      if state == "dict":

        for line in passwords.readlines():

          pwd = line.strip('\n')
          hash = sha384(str.encode(pwd))
          output.write(hash.hexdigest() + "#"+ str(pwd) + "\n")
        stoptime = datetime.now() - starttime
        print("Finished example-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()

      if state == "brute":

        output = open('../rb_table.txt', "a")
        for i in range(1,64):

          for char in map(''.join, product(myLetters, repeat=i)):
            hash = sha384(str.encode(char))
            output.write(hash.hexdigest()+ '\n')
          stoptime = datetime.now() - starttime
          print("Finished example-Creation in: "+str(stoptime)+" seconds")
          
          output.close()
          passwords.close()

    elif hash_algo == "sha512":

      if state == "dict":

        for line in passwords.readlines():

          pwd = line.strip('\n')
          hash = sha512(str.encode(pwd))
          output.write(hash.hexdigest() +  "\n")
        stoptime = datetime.now() - starttime
        print("Finished example-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()

      if state == "brute":

        output = open('../rb_table.txt', "a")
        for i in range(1,64):

          for char in map(''.join, product(myLetters, repeat=i)):
            hash = sha512(str.encode(char))
            output.write(hash.hexdigest()+ '\n')
          stoptime = datetime.now() - starttime
          print("Finished example-Creation in: "+str(stoptime)+" seconds")
          
          output.close()
          passwords.close()

      if state == "brute":
        output = open('../rb_table.txt', "a")
        for i in range(1,64):
          for char in map(''.join, product(myLetters, repeat=i)):
            hash = sha512(str.encode(char))
            output.write(hash.hexdigest()+ '\n')
          stoptime = datetime.now() - starttime
          print("Finished example-Creation in: "+str(stoptime)+" seconds")
    
    elif hash_algo == "md5":
      
      if state == "dict":
        
        for line in passwords.readlines():

          pwd = line.strip('\n')
          hash = md5(str.encode(pwd))
          output.write(hash.hexdigest()+ '\n')
        stoptime = datetime.now() - starttime
        print("Finished example-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()
        
      if state == "brute":

        output = open('../rb_table.txt', "a")
        for i in range(1,64):
          
          for char in map(''.join, product(myLetters, repeat=i)):
            hash = md5(str.encode(char))
            output.write(hash.hexdigest()+ '\n')
          stoptime = datetime.now() - starttime
          print("Finished example-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()

    elif hash_algo == "ntlm":

      if state == "dict":

        for line in passwords.readlines():

          pwd = line.strip('\n')
          hash = new('md4', pwd.encode('utf-16le'))
          output.write(hash.hexdigest()+ '\n')
        stoptime = datetime.now() - starttime
        print("Finished example-Creation in: "+str(stoptime)+" seconds")
        output.close()
        passwords.close()
    
      if state == "brute":

        output = open('../rb_table.txt', "a")
        for i in range(1,64):

          for char in map(''.join, product(myLetters, repeat=i)):

            hash = new('md4', char.encode('utf-16le'))
            output.write(hash.hexdigest()+ '\n')
          stoptime = datetime.now() - starttime
          print("Finished example-Creation in: "+str(stoptime)+" seconds") 

        output.close()
        passwords.close()

gen_example_hashes(dict_path="lst/john.txt", hash_algo="md5")
=======
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
>>>>>>> 03176a839c3b76be4dd017fbeb5524c76171115a
