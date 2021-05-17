#!/usr/bin/env python3
import os

print("Enter level number:")
level = input()
os.system("ssh bandit" + level + "@bandit.labs.overthewire.org -p 2220")
