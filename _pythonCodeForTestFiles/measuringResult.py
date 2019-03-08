# This file measure the time of sorting experimental data using the different sorting algorithms

from inputData import arraySetBinaryDigits, arraySetRevSorted, arraySetRandom, arraySetFiftyUnsorted, arraySetTenUnSorted
import time
import sys
import datetime

from heapSort import heapSort
from mergeSort import mergeSort
from hoarePartition import quickSortHoare
from lomutoPartition import quickSortLomuto
from quickSortOpenSource import quickSortOpenSource

recursion = 1000000
sys.setrecursionlimit(recursion)    #this function increase the recursion limit.

array = arraySetBinaryDigits        #change the variable to switch to different test
#array = arraySetRevSorted           #comment out to use
#array = arraySetRandom               #comment out to use
#array = arraySetFiftyUnsorted          #comment out to use
#array = arraySetTenUnSorted            #comment out to use

now = datetime.datetime.now()           #print the time and date for the record
print now

number_of_array = len(array)        #set the range of the array
for i in range (0, number_of_array):
    start = time.time()
    sorted(array[i])
    #mergeSort(array[i])
    #quickSortHoare(array[i])
    #quickSortLomuto(array[i])
    #quickSortOpenSource(array[i])
    end = time.time()
    print (end-start),