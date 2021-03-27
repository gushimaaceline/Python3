countries=["Kenya","Uganda","Rwanda","South Sudan"]
print(countries[2])
'Rwanda'
countries[1:3]
['Uganda', 'Rwanda']
new_countries=["Burundi","Tanzania"]
countries.extend(new_countries)
print(countries)
['Kenya', 'Uganda', 'Rwanda', 'South Sudan', 'Burundi', 'Tanzania']
countries.reverse()
print(countries)
['Tanzania', 'Burundi', 'South Sudan', 'Rwanda', 'Uganda', 'Kenya']
list=[[1,2,3],[4,5,6],[],[7,8,9]]
b=[element for sublist in list for element in sublist]
print(b)
[1, 2, 3, 4, 5, 6, 7, 8, 9]


list=[[1,2,3],[4,5,6],[],[7,8,9]]
b=[]
for sublist in list:
    for element in sublist:
            b.append(element)

print(b)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
b
[1, 2, 3, 4, 5, 6, 7, 8, 9]
c=[any%2 for any in b]
print(c)
[1, 0, 1, 0, 1, 0, 1, 0, 1]
