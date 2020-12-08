#!/usr/bin/env python3

from sys import argv
from hash_cracker import crack_hash, gen_rbtable, multi_crack



#cracking
if argv[0] == '-c':
  if argv[1] == '-l':
    """ 
    hash_path = ""
    rbt_path = ""
    out_path =""
    if argv[3] == '-o':
      out_path = argv[4]
      
    elif argv[3] == '-rbt':
      rbt_path = argv[4]
    """   
    
    multi_crack(hash_path=argv[2], rbt_path=argv[3], out_path=argv[4])
  else:
    crack_hash(argv[1], argv[2])

#generating stuff -> example files, rainbow tables etc.
elif argv[0] == '-gen':
  #state = dict, brute
  #hashalgo = sha512, md5, sha25
  #dict_path = if state == brute: just input a .,
  #            elif state == dict: input your path to your dictionary
  if argv[1] == '-rbt':
    gen_rbtable(state=str(argv[2]), hashalgo=str(argv[3]), dict_path=str(argv[4]), rb_output=str(argv[5]))
  if argv[1] == '-hf':
    print('Hashes')