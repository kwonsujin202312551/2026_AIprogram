set1 = {0, 1, 2, 2, 4, 5, 5}
print(set1)

set1 = {0, 5, 2, 2, 4, 1}
print(set1)

#합집합
setA = {1, 2, 3, 4}
setB = {2, 4, 6, 7}
setC = setA.union(setB)
print(setC)

setA = {1, 2, 3, 4}
setB = {2, 4, 6, 7}
setC = setA | setB
print(setC)

setA = {1, 2, 3, 4}
setB = {2, 4, 6, 7}
setC = setB | setA
print(setC)

setA = {1, 2, 3, 4}
setB = {2, 4, 6, 7}
setC = setB.union(setA)
print(setC)

#교집합
setA = {1, 2, 3, 4}
setB = {2, 4, 6, 7}
setC = setA & setB
print(setC)

setA = {1, 2, 3, 4}
setB = {2, 4, 6, 7}
setC = setA.intersection(setB)
print(setC)

setA = {1, 2, 3, 4}
setB = {2, 4, 6, 7}
setC = setB & setA
print(setC)

setA = {1, 2, 3, 4}
setB = {2, 4, 6, 7}
setC = setB.intersection(setA)
print(setC)

#차집합
setA = {1, 2, 3, 4}
setB = {2, 4, 6, 7}
setC = setA - setB
print(setC)

setA = {1, 2, 3, 4}
setB = {2, 4, 6, 7}
setC = setA.difference(setB)
print(setC)

setA = {1, 2, 3, 4}
setB = {2, 4, 6, 7}
setC = setB - setA
print(setC)

setA = {1, 2, 3, 4}
setB = {2, 4, 6, 7}
setC = setB.difference(setA)
print(setC)
