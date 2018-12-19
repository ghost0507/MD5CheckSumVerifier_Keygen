#
# * Program: MD5 Checksum Verifier 5.x
# * Release: Simple Keygen
# * Created with: Python 3.7.x
#

import hashlib

static = bytearray.fromhex("4c64664d43562d").decode()
regName = input("Enter any registration name: ")

if(regName==""):
    print("Registration name can't be empty!")
else:
    firstHash = (hashlib.md5(regName.encode('utf-8')).hexdigest()).upper()
    var1 = firstHash[12:14]
    var2 = firstHash[16:27]
    secondHash = (hashlib.md5(var2.encode('utf-8')).hexdigest()).upper()
    var3 = secondHash[19:22]
    print("Your registration code is: " + static + var1 + var3 + '\n')