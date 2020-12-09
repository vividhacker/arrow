import time
from itertools import product
from string import ascii_letters, digits, punctuation
from threading import Thread
from datetime import datetime
from hashlib import sha1, sha224, sha256, sha384, sha512,md5, new, sha3_224, sha3_256, sha3_384, sha3_512
from os import path

myLetters =  ascii_letters, digits, punctuation


# Crack a hash
def crack_hash(hash, rb_table):
  starttime = datetime.now()
  rainbowtable = open(rb_table, "r")
  for line in rainbowtable.readlines():
    hashpwd = line.split('#', 1)
    if hash == hashpwd[0]:
      return hashpwd[1]

def create_hash(inp="youdumn", hashalgo="sha1"):
  if hashalgo == "sha1":
    out = sha1(str.encode(inp)).hexdigest()
    return out
  elif hashalgo == "sha224":
    out = sha224(str.encode(inp)).hexdigest()
    return out
  elif hashalgo == "sha384":
    out = sha384(str.encode(inp)).hexdigest()
    return out
  elif hashalgo == "sha512":
    out = sha512(str.encode(inp)).hexdigest()
    return out
  elif hashalgo == "md5":
    out = md5(str.encode(inp)).hexdigest()
    return out
  elif hashalgo == "ntlm":
    out = new('md4', inp.encode('utf-16le')).hexdigest()
    return out
  elif hashalgo == "sha3_224":
    out = sha3_224(str.encode(inp)).hexdigest()
    return out
  elif hashalgo == "sha3_256":
    out = sha256(str.encode(inp)).hexdigest()
    return out
  elif hashalgo == "sha3_512":
    out = sha3_512(str.encode(inp)).hexdigest()
    return out

  
#cracking multiple hashes
def multi_crack(hash_path="", out_path="output.txt", rbt_path="./lst/john.txt"):
  output_file = open(out_path, 'w')
  hash_file = open(hash_path, 'r')
  for line in hash_file.readlines():
    output_file.write(crack_hash(line.strip('\n'), rbt_path))

#Rainbowtable Generator  
def gen_rbtable(state="dict",hash_algo="sha512",dict_path="lst/john.txt"):
  dict_path = str(dict_path)
  state = str(state)
  hash_algo = str(hash_algo)

  rb_output = "./rb_tables/"+dict_path.split('/')[int(len(dict_path.split('/'))-1)].replace('.txt', '')+'_'+hash_algo+'.txt'
  rb_output = rb_output.replace(' ', '')
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

    elif hash_algo == "sha3_224":
      
      if state == "dict":
        
        for line in passwords.readlines():

          pwd = line.strip('\n')
          hash = sha3_224(str.encode(pwd))
          output.write(hash.hexdigest() + "#"+ pwd + "\n")
        stoptime = datetime.now() - starttime
        print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()
        
      if state == "brute":

        output = open('../rb_table.txt', "a")
        for i in range(1,64):
          
          for char in map(''.join, product(myLetters, repeat=i)):
            hash = sha3_224(str.encode(char))
            output.write(hash.hexdigest() + "#"+ char + "\n")
          stoptime = datetime.now() - starttime
          print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()

    elif hash_algo == "sha3_256":
      
      if state == "dict":
        
        for line in passwords.readlines():

          pwd = line.strip('\n')
          hash = sha3_256(str.encode(pwd))
          output.write(hash.hexdigest() + "#"+ pwd + "\n")
        stoptime = datetime.now() - starttime
        print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()
        
      if state == "brute":

        output = open('../rb_table.txt', "a")
        for i in range(1,64):
          
          for char in map(''.join, product(myLetters, repeat=i)):
            hash = sha3_256(str.encode(char))
            output.write(hash.hexdigest() + "#"+ char + "\n")
          stoptime = datetime.now() - starttime
          print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()
    
    elif hash_algo == "sha3_284":
      
      if state == "dict":
        
        for line in passwords.readlines():

          pwd = line.strip('\n')
          hash = sha3_384(str.encode(pwd))
          output.write(hash.hexdigest() + "#"+ pwd + "\n")
        stoptime = datetime.now() - starttime
        print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()
        
      if state == "brute":

        output = open('../rb_table.txt', "a")
        for i in range(1,64):
          
          for char in map(''.join, product(myLetters, repeat=i)):
            hash = sha3_384(str.encode(char))
            output.write(hash.hexdigest() + "#"+ char + "\n")
          stoptime = datetime.now() - starttime
          print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()

    elif hash_algo == "sha3_512":
      
      if state == "dict":
        
        for line in passwords.readlines():

          pwd = line.strip('\n')
          hash = sha3_512(str.encode(pwd))
          output.write(hash.hexdigest() + "#"+ pwd + "\n")
        stoptime = datetime.now() - starttime
        print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()
        
      if state == "brute":

        output = open('../rb_table.txt', "a")
        for i in range(1,64):
          
          for char in map(''.join, product(myLetters, repeat=i)):
            hash = sha3_512(str.encode(char))
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

    elif hash_algo == "sha3_224":
      
      if state == "dict":
        
        for line in passwords.readlines():

          pwd = line.strip('\n')
          hash = sha3_224(str.encode(pwd))
          output.write(hash.hexdigest()+ "\n")
        stoptime = datetime.now() - starttime
        print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()
        
      if state == "brute":

        output = open('../rb_table.txt', "a")
        for i in range(1,64):
          
          for char in map(''.join, product(myLetters, repeat=i)):
            hash = sha3_224(str.encode(char))
            output.write(hash.hexdigest()+ "\n")
          stoptime = datetime.now() - starttime
          print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()  

    elif hash_algo == "sha3_256":
      
      if state == "dict":
        
        for line in passwords.readlines():

          pwd = line.strip('\n')
          hash = sha3_256(str.encode(pwd))
          output.write(hash.hexdigest() + "\n")
        stoptime = datetime.now() - starttime
        print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()
        
      if state == "brute":

        output = open('../rb_table.txt', "a")
        for i in range(1,64):
          
          for char in map(''.join, product(myLetters, repeat=i)):
            hash = sha3_256(str.encode(char))
            output.write(hash.hexdigest()+ "\n")
          stoptime = datetime.now() - starttime
          print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()  

    elif hash_algo == "sha3_384":
      
      if state == "dict":
        
        for line in passwords.readlines():

          pwd = line.strip('\n')
          hash = sha3_384(str.encode(pwd))
          output.write(hash.hexdigest() + "\n")
        stoptime = datetime.now() - starttime
        print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()
        
      if state == "brute":

        output = open('../rb_table.txt', "a")
        for i in range(1,64):
          
          for char in map(''.join, product(myLetters, repeat=i)):
            hash = sha3_384(str.encode(char))
            output.write(hash.hexdigest()+ "\n")
          stoptime = datetime.now() - starttime
          print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()

    elif hash_algo == "sha3_512":
      
      if state == "dict":
        
        for line in passwords.readlines():

          pwd = line.strip('\n')
          hash = sha3_512(str.encode(pwd))
          output.write(hash.hexdigest() + "\n")
        stoptime = datetime.now() - starttime
        print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()
        
      if state == "brute":

        output = open('../rb_table.txt', "a")
        for i in range(1,64):
          
          for char in map(''.join, product(myLetters, repeat=i)):
            hash = sha3_512(str.encode(char))
            output.write(hash.hexdigest()+ "\n")
          stoptime = datetime.now() - starttime
          print("Finished rainbowtable-Creation in: "+str(stoptime)+" seconds")

        output.close()
        passwords.close()

create_hash()