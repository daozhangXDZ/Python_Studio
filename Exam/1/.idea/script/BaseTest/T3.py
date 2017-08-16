#!/usr/bin/python
import sys;
numbers=2;
guss=int(input ("\n\nPress the enter key to exit."));
if  guss==numbers:
    print(guss);
elif guss>numbers:
    print(guss  +   1);
else:
    print(guss  -   1);