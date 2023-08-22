list1 = [12,-7,5,64,-14]
list2 = [12,4,-95,3]

output1= [num for num in list1 if num > 0]
output2= [num for num in list2 if num > 0]

print(','.join(map(str, output1)))
print(','.join(map(str, output2)))
