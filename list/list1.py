list=[1,2,3,4,5,6,7,8]
list.append(23)
print(list)

# modified list without change original list
new=[9,1,3,8,5,]
org=new[::] # copy of list
new.sort()
print(new)
print("below original org")
print(org)