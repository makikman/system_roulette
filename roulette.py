#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import os
import subprocess
import random
#open a file that keeps track of trigger pulls
filename = "shots.txt"
fd = open(filename, "r")

#function that initialises the file to 0 shots
def init_counter(fd):
    fd.close()
    fd = open(filename, "w")
    fd.write("0")
    fd.close()

#if file is empty initialise it
if os.stat(filename).st_size == 0:
    print("file was empty. initializing...")
    init_counter(fd)
    exit()

#get the value from file
shots = int(fd.read())
print("Trigger has been pressed " + str(shots) + " times.")

#play russian roulette. if the chamber is loaded
#your system is deleted
chance_of_bullet = 1 / (6 - shots)
if random.random() < chance_of_bullet:
     init_counter(fd)
     print("the chamber was loaded")
    #p = subprocess.Popen(["sudo", "rm", "-r", "-f", "*"], cwd=r'"\", stdout=subprocess.PIPE, shell=True)
    #while True:
#        out = p.stdout.read(1)
#        if out == "" and p.poll() != None:
#            break
#        if out != " ":
#            sys.stdout.write(out)
#            sys.stdout.flush()

#if the chamber was not loaded
#keep track of shots so the chance increases
#shots are stored in file
else:
    shots = shots + 1
    fd.close()
    fd = open(filename, "w")
    fd.write(str(shots))
    fd.close()
