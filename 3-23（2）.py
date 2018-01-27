#1-100求和
#sum = 0
#for i in range(101):
 #   sum = sum+  i
#print(sum)
#100以内3,5倍数的和
'''
sum = 0
for i in range(101):
     if i%3 == 0 and i%5 == 0:
         sum += i
print(sum)
'''
#Collatz猜想
a = input("plz input a number:")
i = int(a)
print(i)
while True:
    if i%2 == 0:
        i = i/2
        if i != 1:
            print(i)
    elif i == 1:
        print(i)
        break
    else:
        i = i*3+1
        print(i)


