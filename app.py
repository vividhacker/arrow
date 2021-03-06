#!/usr/bin/env python3

from sys import argv
from hash_cracker import crack_hash, gen_rbtable, multi_crack, gen_example_hashes



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



elif str(argv[0]) == '-gen':
  if argv[1] == '-rbt':
    gen_rbtable(state=str(argv[2]), hashalgo=str(argv[3]), dict_path=str(argv[4]))
  if argv[1] == '-hf':
    gen_example_hashes(state=str(argv[2]), hash_algo=str(argv[3]), dict_path=str(argv[4]))
