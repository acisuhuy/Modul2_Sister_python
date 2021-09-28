arr=[1,1,1,1,2,2,2,4,4,4,5,6,9,8,7,4,1,2,3,6,5,4,7,8,5,1,2,36,45,2,3,4,5,8,9,4,1,2,8,7,932,1,74,8,5,3,85,7,4,1,25,8,693,21,47,8,5,63,32,24,7,8]

#nomer1
print('Jumlah angka 1 pada list: ', arr.count(1))
#nomer2
arr.insert(-123, 3)
print('Jumlah angka -123 pada list 3:', *arr)
#nomer3
print('Jumlah angka 932 Pada list: ',arr.index(932))
#nomer4
print('List jika dibalik', *arr[::-1])
#nomer5
print('Element terakhir pada list: ', arr[-1])
#nomer6
arr.append(-456)
print('List menambagkan -456', *arr)
#nomer7
print('setengah bagian terdepan dari list: ', *arr[:len(arr)// 2])