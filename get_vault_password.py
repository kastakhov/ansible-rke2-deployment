#!/usr/bin/env python3
from os import environ
from sys import exit

if 'ANSIBLE_VAULT_PASSWORD' in environ:
    print(environ['ANSIBLE_VAULT_PASSWORD'])
    exit(0)
else:
    exit(1)
