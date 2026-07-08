my_list = []
swapped = True 
num = int(input("How many elemments do you want to sort  "))
for i in range(num):
    val = float(input("enter a list element = "))
    my_list.append(val)

while swapped :
    for i in range(len(my_list)-1) :
        swapped = False 
        if my_list[i] > my_list[i+1] :
            swapped = True
            my_list[i] , my_list[i+1] = my_list[i+1] , my_list[i]
            
print(my_list)

'''
###  What is the output of the following snippet? ###
'''
  """ QIZ """
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[0]

print(list_3)

################
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2

print(list_3)

########################

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[:]

print(list_3)

################

list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)

