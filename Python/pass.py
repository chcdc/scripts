#!/usr/bin/python3.5
# Generate random password
#
# Carlos Carvalho
# 15/06/2017
import random, string, sys

password = []
lenght = int(sys.argv[1])
amount = int(sys.argv[2])

def generate(lenght):
    global password
    current_number = 1
    while current_number <= lenght:
        password.append(random.choice(string.digits + string.ascii_lowercase + string.digits + string.ascii_lowercase))
        try:
            if len(item) == len(set(item)):

        current_number += 1
    return (password)



#        if len(password) == len(set(password)):
        #    print("q")


generate(lenght)

print(password)