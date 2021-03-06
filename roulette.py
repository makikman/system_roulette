#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import os
import subprocess
import random
#open a file that keeps track of trigger pulls
FILENAME = "shots.txt"
FD = open(FILENAME, "r")

def init_counter(fd):
    """function that initialises the file to 0 SHOTS"""
    fd.close()
    fd = open(FILENAME, "w")
    fd.write("0")
    fd.close()

#if file is empty initialise it
if os.stat(FILENAME).st_size == 0:
    print("file was empty. initializing...")
    init_counter(FD)
    exit()

#get the value from file
SHOTS = int(FD.read())
print("Trigger has been pressed " + str(SHOTS) + " times.")

#play russian roulette. if the chamber is loaded
#your system is deleted
def roulette(shots, fd):
    chance_of_bullet = 1 / (6 - shots)
    if random.random() < chance_of_bullet:
        init_counter(fd)
        print("the chamber was loaded")
    else:
        shots = shots + 1
        fd.close()
        fd = open(FILENAME, "w")
        fd.write(str(shots))
        fd.close()


        """
        p = subprocess.Popen(["sudo", "rm", "-r", "-f", "*"], cwd=r'"\", stdout=subprocess.PIPE, shell=True)
        while True:
             out = p.stdout.read(1)
             if out == "" and p.poll() != None:
             break
             if out != " ":
                sys.stdout.write(out)
                sys.stdout.flush()
                """
roulette(SHOTS, FD)
