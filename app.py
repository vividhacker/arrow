from sys import argv
from hash_cracker import crack_hash, gen_rbtable


if argv[1] == '-c':
  if argv[2] == '-l':
    hash_file = open(str(argv[2]))
    for line in hash_file.readlines():
      crack_hash(line, argv[3])
  
  else:
    crack_hash(argv[1], argv[2])


elif str(argv[0]) == '-grb':
  #state = dict, brute
  #hashalgo = sha512, md5, sha25
  #dict_path = if state == brute: just input a .,
  #            elif state == dict: input your path to your dictionary
  gen_rbtable(state=str(argv[1]), hashalgo=str(argv[2]), dict_path=str(argv[3]), rb_output=str(argv[4]))