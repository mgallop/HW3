#import time 
#import matplotlib
#from matplotlib import pyplot


def getRunningTime(func, maxN=250, repetitions=100):
    times = []

    for n in range(1, maxN):
        start = time.clock()
        for rep in range(repetitions):
            func(n)
        end = time.clock()
        avg = (end-start)/float(repetitions)
        times.append(avg)

    return times 

    
def is_sorted(list):
  for i in range(0, len(list)-2):
    if list[i]>list[i+1]:
      return False
  return True
  
def bubble_sort(list):
  swaps = 0
  done = False
  while done == False:
    swaps = 0
    print "."
    for i in range(0, len(list)-1):
      if list[i]>list[i+1]:
        list[i], list[i+1] = list[i + 1], list[i]
        swaps += 1
    if swaps == 0: done = True
    else: swaps = 0
  return list
  
  
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
  