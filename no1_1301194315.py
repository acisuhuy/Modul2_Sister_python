import array

# array
arr = [12, 15, 8, 1, 45, 13, 22, 48, 56, 89, 3, 45,
        19, 56, 78, 33, 99, 78, 45, 65, 110, 97, 92]
        
#funsgi insertion
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]

        j = i-1
        while j>= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
            arr[j+1] = key
        #return
    return array

#fungsi binarysearch
def binarysearch(arr, r, x):
    n = 0

    while n <= r:
        mid = n +(r-1) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
                n = mid + 1
        elif arr[mid] > x:
                r = mid -1
    return -1


#panggil fungsi Insertion
insertion_sort(arr)

#printinsertion sort
for i in range(len(arr)):
    print("% d" % arr[i])

x = 2
hasil =binarysearch(arr, len(arr)-1, x)

if hasil == -1:
    print("Elemen tidak ditemukan")
else:
    print("Berada di index ke -", str(hasil))