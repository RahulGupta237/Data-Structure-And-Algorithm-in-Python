numdays=int(input("enter a number of days"))
total=0
list_tempday=[]
for i in range(numdays):
    temprature=int(input(f"enter a day {i+1} high temprature  "))
    list_tempday.append(temprature)
    total+=1

print(f"Average temprature {total/numdays}")
for i in list_tempday:
    if i > total/numdays:
        print(f"THis day {i} above than average high temprature")
    else:
        print("no any day low  than average high temprature")

