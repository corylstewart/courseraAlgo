def unimod_top(a):
    if len(a) == 1: #if one element array return element
        return a[0]
    elif len(a) == 0: #if array is empty return none
        return None
    elif len(a) == 2: #if array has two elements return the higher of the two
        if a[0] < a[1]:
            return a[1]
        else:
            return a[0]
    middle = len(a)/2 #select the middle element
    '''if the middle is the largest of its neighbors it is the max so return it
    if the list is still ascending recurse on the right half
    if the list is stilll descending recurse on the left half'''
    if a[middle-1] < a[middle] and a[middle] > a[middle+1]:
        return a[middle]
    elif a[middle-1] < a[middle] and a[middle] < a[middle+1]:
        return unimod_top(a[middle:])
    else:
        return unimod_top(a[:middle])
        
print unimod_top([1,10,9,8,7,6,5])
print unimod_top([1,2,3,4,5,10,8,6,4,2,1,0])
print unimod_top([])
print unimod_top([10])
print unimod_top([10,1])
print unimod_top([1,10])

a = list()
for i in xrange(1000):
    a.append(i)
for i in range(998,0,-3):
    a.append(i)
print unimod_top(a)
