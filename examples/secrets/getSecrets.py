#!/usr/bin/env python
#Author: skondla@me.com
#purpose: get secret key
# -*- coding: utf-8 -*-

import secretAdmin
import sys


def getPasswords(*kwargs):
    mypassword = secretAdmin.getPassword(kwargs[0],kwargs[1])
    print (kwargs[1], mypassword)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print ("You must set argument!!!")
        print ("region,secretkey")
        sys.exit(0)

    getPasswords(sys.argv[1],sys.argv[2])
