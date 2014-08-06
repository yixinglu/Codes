#!/usr/bin/env python

def fact(n):
  if n == 1:
    return 1
  return n * fact(n - 1)

print fact(1)
print fact(5)
print fact(100)
# print fact(1000)


from recipe_474088_1 import tail_call_optimized

def fact(n):
  return fact_iter(1, 1, n)

@tail_call_optimized
def fact_iter(product, count, max):
  if count > max:
    return product
  return fact_iter(product * count, count + 1, max)

print fact(1000)

