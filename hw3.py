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