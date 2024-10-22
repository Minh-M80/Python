# 1.nhập dãy số nguyên ngăn cách bởi dấu phẩy
# 2.hiện thị số dương nhỏ nhất trong danh sách
# 3.hiện thị dãy âm liên tiếp dài nhất
# 4.hiện thị tổng và tbc danh sách

def trans_lst(s):
    return list(map(int,s.split(",")))

#2
def duong_min(lst):
    min_num=[char for char in lst if char>0]
    if min_num:
        return min(min_num)
    else:
        return "Danh sách không có số dương"
def longest_negative_subarrays(lst):
    max_len = 0
    current_len = 0
    start_idx = -1
    subarrays = []
    
    for i, num in enumerate(lst):
        if num < 0:
            if current_len == 0:
                start_idx = i  # Đánh dấu vị trí bắt đầu của dãy âm hiện tại
            current_len += 1
        else:
            if current_len > 0:
                # Khi gặp số không âm, kiểm tra và cập nhật danh sách dãy âm dài nhất
                if current_len > max_len:
                    max_len = current_len
                    subarrays = [lst[start_idx:start_idx + current_len]]  # Cập nhật dãy dài nhất
                elif current_len == max_len:
                    subarrays.append(lst[start_idx:start_idx + current_len])  # Thêm dãy có cùng độ dài
            current_len = 0  # Đặt lại độ dài
    
    # Xử lý dãy âm cuối cùng nếu mảng kết thúc bằng số âm
    if current_len > 0:
        if current_len > max_len:
            max_len = current_len
            subarrays = [lst[start_idx:start_idx + current_len]]
        elif current_len == max_len:
            subarrays.append(lst[start_idx:start_idx + current_len])
    
    return subarrays

# Ví dụ sử dụng:
# arr = [1, -2, -3, 4, -1, -2, -5, -7, 0, -1, -3, -6, -7]
# longest_subarrays = longest_negative_subarrays(arr)

# if longest_subarrays:
#     print("Dãy âm liên tiếp dài nhất là:")
#     for subarray in longest_subarrays:
#         print(subarray)
# else:
#     print("Không có dãy âm nào trong mảng.")
