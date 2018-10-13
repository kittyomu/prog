import sys
import math

r = sys.argv
argc = len(r)

a = float(r[1])

if argc != 2:
  print ("error 入力する数値は一つです")
  quit()

print (a*a*math.pi)