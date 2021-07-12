# extend method
vowel=['a','e','i','o','u']
vowel.insert(3,'o')
print("updated list",vowel)

#pop() method

vowel=['a','e','i','o','u']
vowel.pop(2)
print("list elements",vowel)

#remove() method

list=['1','2','3','4','5']
for i in list:
  print(i)
  list.remove('2')
  print("after removing:")
  for i in list:
    print(i)
    
#reverse() method

systems=['windows','macos','linux']
print('original list','systems')
s2= systems.reverse()
print(s2)

#sort() method

list1=['5','4','2','1','3']
list1.sort()
print("sorted list",list1)
