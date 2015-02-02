import random

a = [5,1,8,6,7,10,9,4,2,3,99,20]

def quick_sort(a):
    if len(a) < 2:
        return a
    pivot = random.randint(0,len(a)-1)
    left = list()
    middle = list()
    right = list()
    piv_elem = a[pivot]
    for i in xrange(len(a)):
        if a[i] < piv_elem:
            left.append(a[i])
        elif a[i] > piv_elem:
            right.append(a[i])
        else:
            middle.append(a[i])
    return quick_sort(left) + middle + quick_sort(right)

def quick_sort_in_place(a):
    if len(a) < 2:
        return a
    pivot = random.randint(0,len(a)-1)
    a[0], a[pivot] = a[pivot], a[0]
    repeats = 1
    i = 1
    j = 1
    while j < len(a):
        if a[j] < a[0]:
            a[i], a[j] = a[j], a[i]
            i += 1
        elif a[j] == a[0]:
            a = [a.pop(j)] + a
            repeats += 1
            i += 1
        j += 1
    return quick_sort_in_place(a[repeats:i]) + a[:repeats] + quick_sort_in_place(a[i:])


def quick_sort_first_element(a, left, right):
    count = 0
    if right - left < 2:
        return 0
    else:
        i = partition(a, left, right)
        count = right - left - 1
        left_count = quick_sort_first_element(a, left, i)
        right_count = quick_sort_first_element(a, i+1, right)
        return count + left_count + right_count

def partition(a, left, right):
    pivot = a[left]
    i = left + 1
    for j in range(i,right):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[left], a[i-1] = a[i-1], a[left]
    return i - 1

def quick_sort_last_element(a, left, right):
    count = 0
    if right - left < 2:
        return 0
    else:
        a[left], a[right-1] = a[right-1], a[left]
        i = partition(a, left, right)
        count = right - left - 1
        left_count = quick_sort_last_element(a, left, i)
        right_count = quick_sort_last_element(a, i+1, right)
        return count + left_count + right_count

def quick_sort_middle_element(a, left, right):
    count = 0
    if right - left < 2:
        return 0
    else:
        median = make_median(a, left, right)
        a[left], a[median] = a[median], a[left]
        i = partition(a, left, right)
        count = right - left - 1
        left_count = quick_sort_middle_element(a, left, i)
        right_count = quick_sort_middle_element(a, i+1, right)
        return count + left_count + right_count

def make_median(a, left, right):
    first = a[left]
    middle = a[(left+right-1)/2]
    last = a[right-1]
    if right - left == 2:
        return left
    if (first < middle and first > last) or (first > middle and first < last):
        return left
    elif (middle < first and middle > last) or (middle > first and middle < last):
        return (left+right-1)/2
    else:
        return right - 1

def is_sorted(a):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return 'Not Sorted'
        return 'Is Sorted'

'''
print quick_sort_middle_element(a,0,len(a))


a = list()
with open('QuickSort.txt') as f:
    for line in f.readlines():
        a.append(int(line))

print quick_sort_first_element(a,0,len(a))

print is_sorted(a)

a = list()
with open('QuickSort.txt') as f:
    for line in f.readlines():
        a.append(int(line))

print quick_sort_last_element(a,0,len(a))

print is_sorted(a)

a = list()
with open('QuickSort.txt') as f:
    for line in f.readlines():
        a.append(int(line))

print quick_sort_middle_element(a,0,len(a))

print is_sorted(a)'''