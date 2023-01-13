def removeDuplicates(myList):
    new_list=[]
 
    for i in myList:
 
        if i not in new_list:
 
            new_list.append(i)
 
    return new_list

myist=[11,22,11,22,33,45]
print(removeDuplicates(myist))