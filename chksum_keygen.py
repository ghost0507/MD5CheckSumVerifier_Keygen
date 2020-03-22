#
# * Program: MD5 Checksum Verifier v5.x
# * Release: Simple Keygen
# * Created with: Python 3.8.x
#

import hashlib

def getMD5(inputText):
  return hashlib.md5(inputText.encode('utf-8')).hexdigest().upper()

static = 'LdfMCV-'
regName = input("Enter any registration name: ")

if(regName.strip()==""):
    print("Registration name can't be empty!")
else:
   md5Hash1 = getMD5(regName)
   var1 = md5Hash1[12:14]
   var2 = md5Hash1[16:27]
   md5Hash2 = getMD5(var2)
   var3 = md5Hash2[19:22]
   print("Registration code: " + static + var1 + var3)
