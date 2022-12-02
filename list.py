'''
list is ordered sequence of different types of elements.
denoted by []
list is mutable , meant value can be chnaged
del(L[index])- to delete particular index of a list
L.pop(), remove elements at the end of the list with L.pop(), retrunrs the removed elements
L.remove(element)- remove specific elements from the list
List can be converted into string using procedure list
s = 'abc'
G= list(s)
can use s.split(), to split a string on a character parameter 
split on spaces if called without parameter
''.join(L)
'_'join(L)
L.sort()- will mutate the lists to a new one, and sorted()-
just a sorted version but don't mutate the list.
L.reverse() - mutate the list
'''
L = [1,2,3]
L.append(5)
L1 = [1,2,3]
L1.extend([5,6])
L2 = [3,5,6]
L3 = L1 + L2
#print(L3)
del(L3[2])
s = 'manu'
surya = list(s)
sorted(surya)
surya.sort()


