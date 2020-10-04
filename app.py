from os import path
import hash_cracker

directory = ""

while True:
  cmd_line = input(directory, " » ")
  cmdv = cmd_line.split(" ")
  
  if cmdv[0] == "crack":
    if cmdv[1] == "-rb":
      if cmdv[2] != "":
        if path.exists(str(cmdv[2])):
          rainbow_table_file = open(cmdv[2])
          return rainbow_table_file
        else:
          print('Rainbowtable not found')
        if cmdv[3] == "-f":
          if path.exists(str(cmdv[4])):
            hash_file = open(str(cmdv[4]))
            for line in hash_file.readlines():
              crack_hash(line, rainbow_table_file)
        if cmdv[3] != "-f":
          crack_hash(cmdv[3])
      else:
        print('Rainbowtable not specified')
   
  elif cmdv[0]  == "gen_rb":
    if cmdv[1] == "-d":
      if path.exists(str(cmdv[2])):
         dictionary_file_path = str(cmdv[2])
         return dictionary_file_path
      elif not path.exists(str(cmdv[2])):
        print('The dictionary file path does not exist')
    elif cmdv[2] == "-bg":
      state="brute"