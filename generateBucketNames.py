#!/usr/bin/env python

import sys

if len(sys.argv) != 3:    
    print "Usage: python generateBucketNames.py wordlistfile domainname"
    exit(1);

with open(sys.argv[1]) as f:
    for line in f:
    	print line.strip()+"."+sys.argv[2].strip()