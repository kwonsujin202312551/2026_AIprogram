#5-1
even_list = list(range(2, 11, 2))
print(even_list)

nations = ['Korea', 'China', 'India', 'Nepal']
print(nations)

friends = ['길동', '철수', '은지', '지은', '영민']
print(friends)

string = list('XYZ')
print(string)

#5-2
prime_list=[2,3,5,7]
print("prime_list의 첫 원소 :", prime_list[0])
print("prime_list의 마지막 원소 :", prime_list[3])
print("prime_list의 마지막 원소 :", prime_list[-1])

nations=['KOREA','China','Russia','Malaysia']
print("nations의 첫 원소 : ", nations[0])
print("nations의 마지막 원소 : ", nations[-1])
print("nations의 마지막 원소 : ",nations[len(nations)-1])

#5-3
prime_list=[2,3,5,7]
print("소수목록 : ",prime_list)
prime_list.append(11)
print("추가 후 소수목록 : ",prime_list)

print("삭제 전 소수목록 : ",prime_list)
prime_list.remove(3)
print("삭제 후 소수목록 : ",prime_list)

nations=['KOREA','China','Russia','Malaysia']
print("국가 목록 : ",nations)
nations.append('Nepal')
print("추가 후 국가 목록 : ",nations)

if('Japan' in nations):
    print("Japan는(은) 국가목록에 있습니다.")
else:
        print("Japan는(은) 국가목록에 없습니다.")
if('Russia' in nations):
    print("Russia는(은) 국가 목록에 있습니다")
else:
        print("Russia는(은) 국가 목록에 없습니다")

#5-4
prime_list=[2.3,5,7]
print("1에서 10까지의 소수 :",prime_list)
print(" 최솟값: " , min(prime_list))
print(" 최댓값: " , max(prime_list))
print(" 합계 : " , sum(prime_list))
print(" 평균 : " , sum(prime_list)/len(prime_list))

nations=['KOREA','China','Russia','Malaysia']
print("사전에 가장 먼저 나오는 나라 :", min(nations))
print("사전에 가장 뒤에 나오는 나라 :",max(nations))        
        
#5-5
a = [1, 2, 3]
b = [10, 20, 30]

a.append(b)
print(a)

a = [1, 2, 3]
b = [10, 20, 30]

a.extend(b)
print(a)

nlist = list(range(1, 11))
print(nlist)

nlist = list(range(1, 11))

nlist.insert(0, 0)

print(nlist)

nlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nlist.reverse()

print(nlist)

nlist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

last = nlist.pop()

print("마지막 원소 =", last)
print("nlist =", nlist)

#5-6
n = int(input("반복할 정수를 입력하시오 : "))

result = [1, 2, 3] * n

print(result)

#5-7
n_list = list(range(15))
print(n_list)

n_list = list(range(15))

s_list1 = n_list[0:5]
s_list2 = n_list[5:11]
s_list3 = n_list[11:15]
s_list4 = n_list[2:11:2]
s_list5 = n_list[10:5:-1]
s_list6 = n_list[10:1:-2]

print(s_list1)
print(s_list2)
print(s_list3)
print(s_list4)
print(s_list5)
print(s_list6)
#5-6
n = int(input("반복할 정수를 입력하시오 : "))

result = [1, 2, 3] * n

print(result)

