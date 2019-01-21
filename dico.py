# encoding utf-8


import hashlib
import sys
import time
hashes = "PATH TO SHADOW FILE"
dict_file = "PATH TO DICTIONNARY"
crack = []
t0 = time.clock();
colors = {"R":"\033[91m",
           "G":"\033[92m",
           "~":"\033[00m"
         }


def main():
    with open(hashes) as fileobj:
        for line in fileobj:
            password = line.split(':')
            crack.append(password[1][3:])
    i = 0
    while i < len(crack):
        with open(dict_file) as dicobj:
            for line in dicobj:
                lines = line.strip()
                if hashlib.md5(lines.encode('utf-8')).hexdigest() == crack[i]:
                    sys.stdout= open('dicoOutput.txt', 'a')
                    print(f"{colors['G']}{''.join(lines)}")
                    print(colors["~"])
                    print("Statistics")
                    print("~~~~~~~~~~~~~~~~~")
                    print(f"Calculation time: {round(time.clock() - t0, 3)} seconds")
                    print(f"Original hash:    {crack[i]}")
                    print(f"Found string:     {''.join(lines)}")
                    print("~~~~~~~~~~~~~~~~~ \n")
            i = i + 1


if __name__ == '__main__':
    main()
