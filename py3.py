# i=1
# while i<9:
#     a=i*i
#     print("bình phương số thứ ",i,'là',a)
#     i+=1

#bài 01
# for i in range(100):
#     if i%2!=0:
#         print("các số dương lẻ nhỏ hơn 100 :",i)


#bài 02
# n=int(input("nhập số nguyên n:"))
# sum=0
# for i in range(1,n+1):
#     sum+=float((-1)**i/(-i))
# print(sum)

#bài 03
 
# n=int(input("nhập số nguyên n:"))
# while n<=0 and n>=100:
#     n=int(input("nhập số nguyên n:"))


# for i in range(1,n):
#     if(i%3==0):
#         print(i)


#bài 04
# from math import sqrt
# a=int(input("Nhập số nguyên a"))
# while 0>=a:
#     a=int(input("Nhập số nguyên a"))

# t=int(sqrt(a))
# count=0
# for i in range(1,t+1):
#     if(a%i==0):
#         count+=1
#         if i!=a/i:
#             count+=1

# print("số lượng ước của nó là",count)

# for i in range(1,a+1):
#     if(a%i==0):
#         print(i)
        
	
#bài05
# a=int(input("nhập a"))
# b=int(input("nhập b"))

# while a<=0:
#     a=int(input("nhập a"))
# while b<=0:
#     b=int(input("nhập b"))

# for i in range(1,min(a,b)+1):
#     if(a%i==0 and b%i==0):
#         print(i)

#bai06

# from math import sqrt
# a=int(input("nhập a"))
# while a<=0:
#     a=int(input("nhập a"))
# t=int(sqrt(a))
# for i in range(2,t+1):
#     if(a==2 or a==3):
#         print("a là số nt")
#     if(a%i==0):
#         print("a k là số nt")
#         break
#     else:
#         print("a là số nt")

#bài 07
# a = int(input("Nhập vào số nguyên dương a: "))
# if a <= 0:
#     print("Vui lòng nhập vào một số nguyên dương.")
# else:
#     divisors_sum = 0
#     for i in range(1, a):
#         if a % i == 0:
#             divisors_sum += i

#     if divisors_sum == a:
#         print(f"{a} là số hoàn hảo.")
#     else:
#         print(f"{a} không phải là số hoàn hảo.")

#bài 08
# A = float(input("Nhập vào giá trị A: "))
# sum_val = 0
# n = 1

# while sum_val <= A:
#     sum_val += 1/n
#     n += 1

# print(f"Số nguyên dương n nhỏ nhất sao cho tổng lớn hơn {A} là: {n-1}")
#bài 09
# a = int(input("Nhập vào số nguyên dương a: "))
# count=0
# while a<=0:
#     a=int(input("nhập a"))
# while(a):
#     a//=10
#     count+=1
# print("số chữ số của a là ",count)

a = int(input("Nhập vào số nguyên dương a: "))
print("Số chữ số của a là:",len(str(a)))
#

#bài 10
# a=int(input("nhập a"))
# x,y=1,1
# while y<=a:
#     z=x+y
#     x=y
#     y=z
# print(f"số trong dãy số fibonacci lớn nhất nhưng không vượt quá {a}:",x)

