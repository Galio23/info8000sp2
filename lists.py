a_list = [0,13,95,34,56,12]
a_list= list(reversed(a_list))
print(a_list)

#a_list.reserved()

a_list.sort()

print(a_list)

a_list.append(7)

print(a_list)

a_list.extend([53,27])

print(a_list)

a_list.pop()
print(a_list)

a_list.remove(95)       #removes element "95"
print(a_list)
del a_list[3]
print(a_list)

a_list = a_list[0:3]        #removes all but the three first elements
print(a_list)

a_list.insert(2,3)
print(a_list)
