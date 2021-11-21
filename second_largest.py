# Finding the second largest value from a list
total = int(input("Enter number of items: "))
a = list()
print("Input items serially: ", end='')
for i in range(total):
    a.append(int(input()))

print(a)
#### This code has a bug ; when the __first 2 input__ is the greatest number it returns largest number; ###
### Fix This SHIT ###
max1 = a[0]
max2 = a[0]
for item in a:
    if (item > max1):
        max2 = max1
        max1 = item

print('Second largest item: ' +str(max2))

'''
max1 = 0
max2 = 0
## Finding MAX from list
for item in a:
    if (item>max1):
        max1 = item
    elif(item>max2 and item<max1):
        max2 = item
'''