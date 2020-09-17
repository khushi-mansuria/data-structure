# Selection sort

def selection_sort(num):
for i in range(len(num)):
lowest_value_index=i
for j in range(i+1,len(num)):
if num[j]<num[lowest_value_index]:
lowest_value_index=j
num[i],num[lowest_value_index]=num[lowest_value_index],num[i]

# Insertion sort

def insertionSort(arr):
for i in range(1, len(arr)):
key = arr[i]
j = i-1
while j >=0 and key < arr[j] :
arr[j+1] = arr[j]
j -= 1
arr[j+1] = key
# main
arr = ['t','u','t','o','r','i','a','l']
insertionSort(arr)
print ("The sorted array is:")
for i in range(len(arr)):
print (arr[i])

# Bubble sort

def bubble_sort(num):
swap=True
while swap:
swap=False
for i in range(len(num)-1):
if num[i]>num[i+1]:
num[i],num[i+1]=num[i+1],num[i]
swap=True


list=[23,14,66,8,2]
bubble_sort(list)
print(list)
