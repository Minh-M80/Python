# bài 1
# def tinh_giai_thua(n):
#     giai_thua = 1
#     for i in range(2, n + 1):
#         giai_thua *= i
#     return giai_thua
# n = int(input("Nhập n (1 < n < 20): "))
# while n <= 1 or n >= 20:
#     n = int(input("Nhập n (1 < n < 20): "))
# for i in range(2, n + 1):
#     print(f"Giai thừa của {i} là: {tinh_giai_thua(i)}")

#bài 2
# def kiem_tra_so_nguyen_to(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# n = int(input("Nhập n (n < 100): "))
# while n>=100 or n<=0:
#     n = int(input("Nhập n (n < 100): "))
# print("Các số nguyên tố từ 2 đến", n, "là:")
# for i in range(2, n+1):
#     if kiem_tra_so_nguyen_to(i):
#         print(i)



# bài 3

# def tim_uoc_chung_lon_nhat(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# def tim_boi_chung_nho_nhat(a, b):
#     return a * b // tim_uoc_chung_lon_nhat(a, b)

# a = int(input("Nhập số nguyên dương a: "))
# b = int(input("Nhập số nguyên dương b: "))
# while a<=0 or b<=0:
#     a = int(input("Nhập số nguyên dương a: "))
#     b = int(input("Nhập số nguyên dương b: "))
# print("Ước số chung lớn nhất của", a, "và", b, "là:", tim_uoc_chung_lon_nhat(a, b))
# print("Bội số chung nhỏ nhất của", a, "và", b, "là:", tim_boi_chung_nho_nhat(a, b))


# bai 4

def fibonacci(n):
    if n < 0:
        return "Số Fibonacci không hợp lệ"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b
def fibonacci2(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci2(n-1)+fibonacci2(n-2)
n=int(input("Nhập số nguyên dương n:"))
while n<=0:
    n=int(input("Nhập số nguyên dương n"))
print(f"Số Fibonacci thứ {n} là:", fibonacci(n))