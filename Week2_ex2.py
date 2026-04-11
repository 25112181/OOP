import math

# Câu 1: Thể tích hình cầu bán kính 5
r = 5
volume = (4/3) * math.pi * r**3
print("Volume of the sphere: ", volume)


# Câu 2: Tổng chi phí 60 cuốn sách
cover_price = 24.85
discount = 0.4
shipping_cost = 3
shipping_cost_per_book = 0.75
number_of_books = 60
total_cost = (cover_price * (1 - discount) * number_of_books) + shipping_cost + (shipping_cost_per_book * number_of_books)
print("Total cost: ", total_cost)

# Câu 3: Thời gian về nhà sau khi chạy
start_time = 7 * 60 + 15 # 7:15 in minutes
easy_pace = 8 + 15/60 # 8 minutes 15 seconds per mile in hours
tempo_pace = 7 + 12/60 # 7 minutes 12 seconds per mile in hours

total_running_time = 2 * easy_pace + 3 * tempo_pace + easy_pace
finish_time = start_time + total_running_time

hours = int(finish_time // 60)
minutes = int(finish_time % 60)

print("Finish time: ", hours, ":", minutes)