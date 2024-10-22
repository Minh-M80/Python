

n=int(input("Nhập số phần tử của dãy là:"))
while n<=0 or n>=100:
    n=int(input("Nhập số phần tử của dãy là:"))
a=[]
for i in range(n):
    t=int((input(f"Nhập phần tử thứ {i}:")))
    a.append(int(t))
def tbc(n,a):
    tbc=sum(a)
    return tbc/n
def tbcPositive(n,a):
    tbcPositive=0
    cnt=0
    for i in range(n):
        if a[i]>0:
            tbcPositive+=a[i]
            cnt+=1
    return tbcPositive/cnt    
def ArrangeIncrease(n,a):
    a=a.sort()
    return a
def findFirstNegative(n,a):
    for i in range(n):
        if(a[i]<0):
            print("Vị trí phần tử âm đầu tiên trong mảng:",i)
def Max(n,a):
    max_value=max(a)
    index=a.index(max)
    print("max và vị trí của nó là:",max_value,index)










