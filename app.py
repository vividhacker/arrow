#import hash_cracker
#import webforcr
import zipforcr
curDir = 'home>'

while True:
  print("""\nthe custom Cracker\n------------------\n\n(1) ZIP Bruteforcing\n(2) Web Bruteforcing\n(3) Hash Cracking\n\n(99) exit\n\n\n\n\n\n\n""")
  inp = input('> ')
  if int(inp) == 1:
    zip_inp = input('zipcracking> ')
    os.system('clear')
    print("""\nZip Cracking\n------------\n\n(1) dictionary attack\n(2) bruteforce attack\n\n(99) back\n\n\n\n\n\n\n""")
    if int(zip_inp) == 1:
      dic_zip_inp = input('zipcracking/dictionary')
      
  if int(inp) == 99:
    break
    
    