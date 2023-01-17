import os, sys
try:
    __import__("pub2").menu()
except Exception as e:
    exit(str(e))
