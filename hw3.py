import random
#import time 
#import matplotlib
#from matplotlib import pyplot


def getRunningTimeList(func, maxN=250, repetitions=100):
    times = []

    for n in range(1, maxN):
      start = time.clock()
      for rep in range(repetitions):
        random_array = range(1, n)
        random.shuffle(random_array)
        func(random_array)
      end = time.clock()
      avg = (end-start)/float(repetitions)
      times.append(avg)

    return times 

    
def is_sorted(list):
  for i in range(0, len(list)-2):
    if list[i]>list[i+1]:
      return False
  return True
  
def merge(left, right):
  result = []
  while len(left) > 0 or len(right) > 0:
    if len(left) > 0 and len(right) > 0:
      if left[0] <= right[0]:
        result.append(left[0])
        del left[0]
      else:
        result.append(right[0])
        del right[0]
    elif len(left) > 0:
      result.append(left[0])
      del left[0]
    else:
      result.append(right[0])
      del right[0]
  return result
  
def merge_sort(list):
  l = len(list)
  if l <= 1:
    return list
  m = l / 2
  right, left = list[0:m], list[m: l]
  left = merge_sort(left)
  right = merge_sort(right)
  return merge(left, right)
  
def comb_sort(list, shrink = 1.24733095):
  gap = len(list)
  done = False
  while done == False:
    print "."
    swaps = 0
    gap = max(int(gap/shrink), 1)
    for i in range(0, len(list)-gap):
      if list[i]>list[i+gap]:
        list[i], list[i+gap] = list[i+gap], list[i]
        swaps += 1
    if swaps == 0 and gap ==1: done = True
  return list
  