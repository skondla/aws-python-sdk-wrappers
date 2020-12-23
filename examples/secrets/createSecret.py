#!/usr/bin/env python
#Author: skondla@me.com
#purpose: Create secret to store password
# -*- coding: utf-8 -*-

import secretAdmin
import sys

def createSecret(*args):
    secretAdmin.createSecret(args[0],args[1],args[2])

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print ("You must set argument!!!")
        print ("region,key,value")
        sys.exit(0)

    createSecret(sys.argv[1],sys.argv[2],sys.argv[3])

