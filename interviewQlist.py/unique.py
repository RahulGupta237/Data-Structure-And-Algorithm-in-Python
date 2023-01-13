#Question 5 - isqunieuq
def isUnique(list):
  a=[]
  for i in list:
    if i in a:
        print(i)
        return False
    else:
        a.append(i)
  return True
mylist=[5,2,3,1]
print(isUnique(mylist))