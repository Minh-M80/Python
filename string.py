# Bài 1: In ra tất cả các ký tự trong xâu và đảo ngược xâu
# def bai1():
#     s = input("Nhập xâu ký tự: ")
#     print("Các ký tự trong xâu:", ", ".join(s))
#     print("Xâu đảo ngược:", s[::-1])

# bai1()
# Bài 2: Tìm số lần xuất hiện của xâu con s1 trong s
# def bai2():
#     s = input("Nhập xâu ký tự: ")
#     s1 = input("Nhập xâu con: ")
#     count = s.count(s1)
#     print(f"Số lần xuất hiện của '{s1}' trong '{s}' là: {count}")

# bai2()
# Bài 3: Đếm chữ hoa, chữ thường trong xâu
# def bai3():

#     s = input("Nhập xâu ký tự: ")
#     upper_count = sum(1 for c in s if c.isupper())
#     lower_count = sum(1 for c in s if c.islower())
#     print(f"Số chữ hoa: {upper_count}")
#     print(f"Số chữ thường: {lower_count}")

# bai3()
# Bài 4: Sắp xếp các ký tự trong xâu theo thứ tự tăng dần
# def bai4():
#     s = input("Nhập xâu ký tự: ")
#     sorted_s = ''.join(sorted(s))
#     print("Xâu sau khi sắp xếp:", sorted_s)

# bai4()
# Bài 5: Tìm tất cả các xâu con của xâu ký tự
# def bai5():
#     s = input("Nhập xâu ký tự: ")
#     substrings = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
#     print("Tất cả các xâu con:", substrings)

# bai5()
# Bài 6: Kiểm tra xem xâu có kết thúc bằng một chuỗi con cho trước hay không
def bai6():
    s = input("Nhập xâu ký tự: ")
    sub_str = input("Nhập chuỗi con: ")
    if s.endswith(sub_str):
        print(f"'{s}' kết thúc bằng '{sub_str}'")
    else:
        print(f"'{s}' không kết thúc bằng '{sub_str}'")

# bai6()
# Bài 7: Ký tự xuất hiện ít lần nhất
from collections import Counter

def bai7():
    s = input("Nhập xâu ký tự: ")
    frequency = Counter(s)
    print(frequency)
    min_frequency = min(frequency.values())
    print(frequency.values())#lấy value
    print(frequency.items())#lấy cặp key-value 
    min_chars = [char for char, count in frequency.items() if count == min_frequency]
    
    print(f"Các ký tự xuất hiện ít lần nhất: {', '.join(min_chars)} với {min_frequency} lần")

# bai7()

# Bài 8: Kiểm tra xem xâu có bắt đầu bằng một chuỗi con cho trước hay không
# def bai8():
#     s = input("Nhập xâu ký tự: ")
#     sub_str = input("Nhập chuỗi con: ")
#     if s.startswith(sub_str):
#         print(f"'{s}' bắt đầu bằng '{sub_str}'")
#     else:
#         print(f"'{s}' không bắt đầu bằng '{sub_str}'")

# bai8()
# Bài 9: Ký tự xuất hiện ít lần nhất
# from collections import Counter
# def bai9():
#     s = input("Nhập xâu ký tự: ")
#     frequency = Counter(s)
#     print(frequency)
#     max_frequency = max(frequency.values())
#     print(frequency.values())
#     print(frequency.items())
#     max_chars = [char for char, count in frequency.items() if count == max_frequency]
    
#     print(f"Các ký tự xuất hiện ít lần nhất: {', '.join(max_chars)} với {max_frequency} lần")

# bai9()

# Bài 10: In ra tất cả các xâu con liên tiếp
# def bai10():
#     s = input("Nhập xâu ký tự: ")
#     substrings = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
#     print("Tất cả các xâu con liên tiếp:", substrings)

# bai10()
# Bài 11: Ký tự xuất hiện nhiều lần nhất
# from collections import Counter
# def bai9():
#     s = input("Nhập xâu ký tự: ")
#     frequency = Counter(s)
#     print(frequency)
#     max_frequency = max(frequency.values())
#     print(frequency.values())
#     print(frequency.items())
#     max_chars = [char for char, count in frequency.items() if count == max_frequency]
    
#     print(f"Các ký tự xuất hiện ít lần nhất: {', '.join(max_chars)} với {max_frequency} lần")

# bai9()