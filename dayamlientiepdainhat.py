def longest_negative_subarrays(arr):
    max_len = 0
    current_len = 0
    start_idx = -1
    subarrays = []
    
    for i, num in enumerate(arr):
        if num < 0:
            if current_len == 0:
                start_idx = i  # Đánh dấu vị trí bắt đầu của dãy âm hiện tại
            current_len += 1
        else:
            if current_len > 0:
                # Kiểm tra xem dãy con hiện tại có phải là dài nhất hay không
                if current_len > max_len:
                    max_len = current_len
                    subarrays = [arr[start_idx:start_idx + current_len]]  # Cập nhật danh sách mới
                elif current_len == max_len:
                    subarrays.append(arr[start_idx:start_idx + current_len])  # Thêm dãy vào danh sách
            current_len = 0  # Đặt lại độ dài
    
    # Xử lý trường hợp dãy kết thúc bằng số âm
    if current_len > 0:
        if current_len > max_len:
            max_len = current_len
            subarrays = [arr[start_idx:start_idx + current_len]]
        elif current_len == max_len:
            subarrays.append(arr[start_idx:start_idx + current_len])

    return subarrays

# Ví dụ sử dụng:
arr = [1, -2, -3, 4, -1, -2, -5, -7, 0, -1, -3, -4,-5]
longest_subarrays = longest_negative_subarrays(arr)

if longest_subarrays:
    print("Các dãy âm liên tiếp dài nhất là:")
    for subarray in longest_subarrays:
        print(subarray)
else:
    print("Không có dãy âm nào trong mảng.")
