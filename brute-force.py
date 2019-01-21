import sys
from sys import argv, exit
from time import time
from hashlib import md5
from itertools import product
from datetime import datetime
from string import ascii_lowercase, ascii_uppercase, digits

hash_ = "your Hash"
special = '@_#'
charset_ = '5'
minlength = 6
maxlength = 6

crack = []

charset = {"1":  ascii_lowercase,
           "2":  ascii_uppercase,
           "3":  digits,
           "4":  ascii_lowercase
               + ascii_uppercase,
           "5":  ascii_lowercase
               + digits,
           "6":  ascii_uppercase
              + digits,
           "7":  ascii_lowercase
              + ascii_uppercase
              + digits,
           "8": ascii_lowercase
              + ascii_uppercase
              + digits
              + special
           }
charset = charset[charset_]

colors = {"R":"\033[91m",
           "G":"\033[92m",
           "~":"\033[00m"
         }



def bruteforce(hash_, characters, min_length, max_length):

    start = datetime.now()
    start_time = time()

    for length in range(int(min_length), int(max_length) + 1):
        products = product(characters, repeat=length)
        for attempt in products:
            hashed = "".join(attempt).encode("utf-8")
            hashed = md5(hashed).hexdigest()


            if hashed != hash_:
                #print(f"{colors['R']}{''.join(attempt)}")
                next

            else:
                diff = int(time()-start_time)
                sys.stdout= open('bruteForceOutput.txt', 'a')
                print(f"{colors['G']}{''.join(attempt)}")
                print(colors["~"])
                print(" Statistics")
                print("~~~~~~~~~~~~~~~~~")
                print(f"Started:          {start}")
                print(f"Calculation time: {diff} seconds")
                print(f"Original hash:    {hash_}")
                print(f"Found string:     {''.join(attempt)}")
                print("~~~~~~~~~~~~~~~~~")
                return True

def main():
    bruteforce(hash_, charset, minlength, maxlength)

if __name__ == "__main__":
    main()
    exit()
