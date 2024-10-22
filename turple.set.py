# # Bài 1
# input_str = input("Nhập chuỗi số, phân tách bằng dấu phẩy: ")


# num_list = input_str.split(',')
# print(num_list)

# num_tuple = tuple(num_list)
# print(num_tuple)
# 
# print("Danh sách:", num_list)
# print("Tuple:", num_tuple)

# Bài 2
# num_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# print("Nửa đầu:", num_tuple[:len(num_tuple)//2])
# print("Nửa cuối:", num_tuple[len(num_tuple)//2:])

# Bài 3
# num_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# even_tuple = tuple(x for x in num_tuple if x % 2 == 0)


# print("Tuple chứa các số chẵn:", even_tuple)


#set
# Bài 1
# input_str = input("Nhập chuỗi các từ, phân tách bởi khoảng trắng: ")


# words = input_str.split()
# print(words)
# unique_words = sorted(set(words))


# print("Các từ sau khi loại bỏ trùng lặp và sắp xếp:", ' '.join(unique_words))
#join() để nối lại danh sách thành một chuỗi kết quả.

# # Bài 2
# input_str = input("Nhập một xâu ký tự: ")


# unique_chars = "".join(sorted(set(input_str), key=input_str.index))


# print("Xâu ký tự sau khi loại bỏ các ký tự trùng lặp:", unique_chars)


# Bài 3
# def longest_unique_substring(s):
#     max_len = 0
#     max_substr = ""
#     start = 0
#     used_chars = {}

#     for i, char in enumerate(s):
#         if char in used_chars and used_chars[char] >= start:
#             start = used_chars[char] + 1
#         used_chars[char] = i
#         current_len = i - start + 1
#         if current_len > max_len:
#             max_len = current_len
#             max_substr = s[start:i + 1]

#     return max_substr

# input_str = input("Nhập một xâu ký tự: ")
# result = longest_unique_substring(input_str)

# print("Xâu con dài nhất không chứa các ký tự trùng lặp:", result)


# def longest_unique_substrings(s):
#     max_len = 0
#     max_substrs = []
#     start = 0
#     used_chars = {}

#     for i, char in enumerate(s):
#         print("i","char",i,char)
#         if char in used_chars and used_chars[char] >= start:
#             start = used_chars[char] + 1
#         used_chars[char] = i
#         current_len = i - start + 1

#         # Nếu tìm thấy xâu con dài hơn
#         if current_len > max_len:
#             max_len = current_len
#             max_substrs = [s[start:i + 1]]  # Làm mới danh sách với xâu mới
#         # Nếu tìm thấy xâu con có độ dài bằng với xâu dài nhất hiện tại
#         elif current_len == max_len:
#             max_substrs.append(s[start:i + 1])  # Thêm vào danh sách

#     return max_substrs

# input_str = input("Nhập một xâu ký tự: ")
# result = longest_unique_substrings(input_str)

# print("Các xâu con dài nhất không chứa các ký tự trùng lặp:", result)
def longest_unique_substrings(s):
    char_set = set()
    left = 0
    max_len = 0
    substrings = []
    
    for right in range(len(s)):
        # Nếu ký tự đã tồn tại trong tập hợp, xóa ký tự phía bên trái cho đến khi không trùng lặp
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Thêm ký tự hiện tại vào tập hợp
        char_set.add(s[right])
        
        current_len = right - left + 1
        
        # Cập nhật xâu con dài nhất
        if current_len > max_len:
            max_len = current_len
            substrings = [s[left:right + 1]]  # Cập nhật lại danh sách với xâu mới dài nhất
        elif current_len == max_len:
            substrings.append(s[left:right + 1])  # Thêm xâu con có cùng độ dài

    return substrings

# Ví dụ sử dụng:
s = "abcabcbbdefgh"
longest_substrings = longest_unique_substrings(s)

if longest_substrings:
    print("Xâu con dài nhất không chứa ký tự trùng lặp là:")
    for substring in longest_substrings:
        print(substring)
else:
    print("Không có xâu con nào thỏa mãn.")
