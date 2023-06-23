# Programa para determinar la función W de Lambert

from math import exp
import sys

def lambert(x):
  l = 0
  r = (l * exp(l) - x) / ((1 + l) * exp(l))
  while abs(r) > 10 ** -8:
    l -= r
    r =  (l * exp(l) - x) / ((1 + l) * exp(l))
  return l

a = float(sys.argv[1])
if a < -exp(-1):
  print("Error: no se puede calcular la función W de Lambert")
else:
  w = round(lambert(a), 8)
  print(w)
