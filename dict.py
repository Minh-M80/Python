#bài 1
# N = int(input("Nhập vào một số nguyên N: "))
# mydict = {i : i * i for i in range(1, N + 1)}
# print(mydict)

print({1,2,3,4,4})
#bài 2

# myclass = {}
# n = int(input("Nhập số lượng học sinh: "))
# for i in range(n):
#     name = input("Nhập tên học sinh: ")
    
#     while True:
#         score = int(input("Nhập điểm của học sinh (0-10): "))
#         if 0 <= score <= 10:
#             break
#         else:
#             print("Điểm không hợp lệ! Vui lòng nhập lại.")
    
#     myclass[name] = score
# score_count = {i: 0 for i in range(11)}
# print("score_count",score_count)
# for score in myclass.values():
#     score_count[score] += 1
# print("\nThống kê số học sinh đạt từng điểm:")
# for score, count in score_count.items():
#     print(f"Điểm {score}: {count} học sinh")


# bài 3

# phonebook = {}
# def add_contact():
#     while True:
#         name = input("Nhập họ tên: ")
#         phone = input("Nhập số điện thoại: ")
#         phonebook[name] = phone
        
#         another = input("Bạn có muốn thêm người khác không? (y/n): ").lower()
#         if another != 'y':
#             break

# def display_phonebook():
#     print("\nDanh bạ điện thoại:")
#     for name in sorted(phonebook.keys()):
#         print(f"{name}: {phonebook[name]}")
#     print(f"Tổng số người trong danh bạ: {len(phonebook)}")

# def search_by_name(search_term):
#     print(f"\nTìm kiếm theo tên chứa: '{search_term}'")
#     found = False
#     for name, phone in phonebook.items():
#         if search_term.lower() in name.lower():
#             print(f"{name}: {phone}")
#             found = True
#     if not found:
#         print("Không tìm thấy người nào.")

# def search_by_phone(search_term):
#     print(f"\nTìm kiếm theo số điện thoại chứa: '{search_term}'")
#     found = False
#     for name, phone in phonebook.items():
#         if search_term in phone:
#             print(f"{name}: {phone}")
#             found = True
#     if not found:
#         print("Không tìm thấy người nào.")

# add_contact()
# display_phonebook()

# name_search = input("\nNhập xâu ký tự để tìm kiếm theo tên: ")
# search_by_name(name_search)

# phone_search = input("\nNhập chuỗi số để tìm kiếm theo số điện thoại: ")
# search_by_phone(phone_search)
