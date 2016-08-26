########################sorting algorithms########################
#bubble sort
def bubble_sort(items):
        """ Implementation of bubble sort """   #doc string, not a comment, string literal as the first statement in a function, becom __doc__
        for i in range(len(items)):
                for j in range(len(items)-1-i):
                        if items[j] &gt; items[j+1]:
                                items[j], items[j+1] = items[j+1], items[j]     # Swap!
 
 #insertion sort
 def insertion_sort(items):
        """ Implementation of insertion sort """   #doc string, not a comment, string literal as the first statement in a function, becom __doc__
        for i in range(1, len(items)):
                j = i
                while j &gt; 0 and items[j] &lt; items[j-1]:
                        items[j], items[j-1] = items[j-1], items[j]
                        j -= 1
 
#merge sort
def merge_sort(items):
        """ Implementation of mergesort """   #doc string, not a comment, string literal as the first statement in a function, becom __doc__
        if len(items) &gt; 1:
 
                mid = len(items) / 2        # Determine the midpoint and split
                left = items[0:mid]
                right = items[mid:]
 
                merge_sort(left)            # Sort left list in-place
                merge_sort(right)           # Sort right list in-place
 
                l, r = 0, 0
                for i in range(len(items)):     # Merging the left and right list
 
                        lval = left[l] if l &lt; len(left) else None
                        rval = right[r] if r &lt; len(right) else None
 
                        if (lval and rval and lval &lt; rval) or rval is None:
                                items[i] = lval
                                l += 1
                        elif (lval and rval and lval &gt;= rval) or lval is None:
                                items[i] = rval
                                r += 1
                        else:
                                raise Exception('Could not merge, sub arrays sizes do not match the main array')
 
 #merge sort2
 def merge(items, sections, temporary_storage):
    (start_1, end_1), (start_2, end_2) = sections
    i_1 = start_1
    i_2 = start_2
    i_t = 0

    while i_1 < end_1 or i_2 < end_2:
        if i_1 < end_1 and i_2 < end_2:
            if items[i_1] < items[i_2]:
                temporary_storage[i_t] = items[i_1]
                i_1 += 1
            else:  # the_list[i_2] >= items[i_1]
                temporary_storage[i_t] = items[i_2]
                i_2 += 1
            i_t += 1

        elif i_1 < end_1:
            for i in range(i_1, end_1):
                temporary_storage[i_t] = items[i_1]
                i_1 += 1
                i_t += 1

        else:  # i_2 < end_2
            for i in range(i_2, end_2):
                temporary_storage[i_t] = items[i_2]
                i_2 += 1
                i_t += 1

    for i in range(i_t):
        items[start_1 + i] = temporary_storage[i]


def merge_sort(items):
    n = len(items)
    temporary_storage = [None] * n
    size_of_subsections = 1

    while size_of_subsections < n:
        for i in range(0, n, size_of_subsections * 2):
            i1_start, i1_end = i, min(i + size_of_subsections, n)
            i2_start, i2_end = i1_end, min(i1_end + size_of_subsections, n)
            sections = (i1_start, i1_end), (i2_start, i2_end)
            merge(items, sections, temporary_storage)
        size_of_subsections *= 2

    return items

 #quick sort
 def quick_sort(items):
        """ Implementation of quick sort """   #doc string, not a comment, string literal as the first statement in a function, becom __doc__
        if len(items) &gt; 1:
                pivot_index = len(items) / 2
                smaller_items = []
                larger_items = []
 
                for i, val in enumerate(items):
                        if i != pivot_index:
                                if val &lt; items[pivot_index]:
                                        smaller_items.append(val)
                                else:
                                        larger_items.append(val)
 
                quick_sort(smaller_items)
                quick_sort(larger_items)
                items[:] = smaller_items + [items[pivot_index]] + larger_items
 
#quick sort2
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)


#heap sort
import heapq
 
def heap_sort(items):
        """ Implementation of heap sort """   #doc string, not a comment, string literal as the first statement in a function, becom __doc__
        heapq.heapify(items)
        items[:] = [heapq.heappop(items) for i in range(len(items))]
 
#selection sort
def selection_sort(items):
    """Sorts a list of items into ascending order using the
       selection sort algoright.
       """               #doc string, not a comment, string literal as the first statement in a function, becom __doc__
    for step in range(len(items)):
        # Find the location of the smallest element in
        # items[step:].
        location_of_smallest = step
        for location in range(step, len(items)):
            # determine location of smallest
            if items[location] < items[location_of_smallest]:
                location_of_smallest = location
        # Exchange items[step] with items[location_of_smallest]
        temporary_item = items[step]
        items[step] = items[location_of_smallest]
        items[location_of_smallest] = temporary_item

########################searching algorithms########################
#linear search
def linear_search(items, desired_item):
    for position, item in enumerate(items):
        if item == desired_item:
            return position

    raise ValueError("%s was not found in the list." % desired_item)

#binary search
def binary_search(items, desired_item, start=0, end=None):
    if end == None:
        end = len(items)

    if start == end:
        raise ValueError("%s was not found in the list." % desired_item)

    pos = (end - start) // 2 + start

    if desired_item == items[pos]:
        return pos
    elif desired_item > items[pos]:
        return binary_search(items, desired_item, start=(pos + 1), end=end)
    else: # desired_item < items[pos]:
        return binary_search(items, desired_item, start=start, end=pos)

#binary search2
def binarySearch(alist, item):
	    first = 0
	    last = len(alist)-1
	    found = False
	
	    while first<=last and not found:
	        midpoint = (first + last)//2
	        if alist[midpoint] == item:
	            found = True
	        else:
	            if item < alist[midpoint]:
	                last = midpoint-1
	            else:
	                first = midpoint+1
	
	    return found
	
	testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
	print(binarySearch(testlist, 3))
	print(binarySearch(testlist, 13))

#binary search3
def binarySearch(alist, item):
	    if len(alist) == 0:
	        return False
	    else:
	        midpoint = len(alist)//2
	        if alist[midpoint]==item:
	          return True
	        else:
	          if item<alist[midpoint]:
	            return binarySearch(alist[:midpoint],item)
	          else:
	            return binarySearch(alist[midpoint+1:],item)
	
	testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
	print(binarySearch(testlist, 3))
	print(binarySearch(testlist, 13))

#sequential search, looks for boolean value, if found = false
def sequentialSearch(alist, item):
	    pos = 0
	    found = False
	
	    while pos < len(alist) and not found:
	        if alist[pos] == item:
	            found = True
	        else:
	            pos = pos+1
	
	    return found
	
	testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
	print(sequentialSearch(testlist, 3))
	print(sequentialSearch(testlist, 13))

#ordered sequential search
def orderedSequentialSearch(alist, item):
	    pos = 0
	    found = False
	    stop = False
	    while pos < len(alist) and not found and not stop:
	        if alist[pos] == item:
	            found = True
	        else:
             if alist[pos] > item:
	                stop = True
	            else:
	                pos = pos+1
	
	    return found
	
	testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
	print(orderedSequentialSearch(testlist, 3))
	print(orderedSequentialSearch(testlist, 13))


########################hashing algorithms and functions########################
#hashing
def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])

    return sum%tablesize

#hashing, use two lists to create hashtable class, 
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size #hold the key items and parallel list
        self.data = [None] * self.size  #hold the data values

#put assumes empty hash slot unless present in self.slots
def put(self,key,data):
  hashvalue = self.hashfunction(key,len(self.slots))

  if self.slots[hashvalue] == None:
    self.slots[hashvalue] = key
    self.data[hashvalue] = data
  else:
    if self.slots[hashvalue] == key:
      self.data[hashvalue] = data  #replace
    else:
      nextslot = self.rehash(hashvalue,len(self.slots))
      while self.slots[nextslot] != None and \
                      self.slots[nextslot] != key:
        nextslot = self.rehash(nextslot,len(self.slots))

      if self.slots[nextslot] == None:
        self.slots[nextslot]=key
        self.data[nextslot]=data
      else:
        self.data[nextslot] = data #replace

def hashfunction(self,key,size):
     return key%size

def rehash(self,oldhash,size):
    return (oldhash+1)%size        

#get computes init hash value
def get(self,key):
  startslot = self.hashfunction(key,len(self.slots))

  data = None
  stop = False
  found = False
  position = startslot
  while self.slots[position] != None and  \
                       not found and not stop:
     if self.slots[position] == key:
       found = True
       data = self.data[position]
     else:
       position=self.rehash(position,len(self.slots))
       if position == startslot:
           stop = True
  return data

def __getitem__(self,key):
    return self.get(key)

def __setitem__(self,key,data):
    self.put(key,data)


################checking anagrams (two strings are equal but not in same order)################
#check to see if each character in the first string occurs in the second
def anagramSolution1(s1,s2):
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK

print(anagramSolution1('abcd','dcba'))

#sort each string alphabetically (a-z) then check to see if the strings equal
def anagramSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

print(anagramSolution2('abcde','edcba'))

#count the number of times each char occurs, use a list of 26 chars, checks if counter lists are equal
def anagramSolution4(s1,s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK

print(anagramSolution4('apple','pleap'))


######################## Dijstra's Algorithm ########################
#determine shortest path via iterative algorithm on nodes
from pythonds.graphs import PriorityQueue, Graph, Vertex
def dijkstra(aGraph,start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                    + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance( newDist )
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert,newDist)




