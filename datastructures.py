#1.Assigning elements to a different lists

print('\n')
list1=[1,2,3]
list2=['apple','banana','cherry']
print('original lists')
print(list1)
print(list2)
list1.append(4)
list2.append('dragon fruit')
print('list after appending one element')
print(list1)
print(list2)
list1.extend(list2)
print('after clubbing list1 and list2')
print(list1)

#2.Accessing elements from a tuple

print('\n')
print('original tuple')
t1=('a','b','c','d',1,2,3)
print(t1)
print('accessing elements using index')
print('1st element:',t1[0],'4th element:',t1[3],'last element:',t1[6])

#3.Deleting different dictionary elements

print('\n')
print('dictionary:')
d1={1:'My',2:'Captain',3:'AI',4:'Workshop'}
print(d1)
print('deleting 3rd element using key')
del d1[3]
print(d1)
print('deleting element using pop')
pop_ele=d1.pop(1)
print(d1)
print('deleted element is:',pop_ele)
print('deleting an element using popitem')
pop_ele1=d1.popitem()
print(d1)
print('deleted key value pair is:',pop_ele1)


