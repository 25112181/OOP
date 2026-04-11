# Câu 1: Đổi  42 phút 42 giây sang giây
minutes = 42
seconds = 42
total_seconds = minutes * 60 + seconds
print("Total seconds: ", total_seconds)
# Câu 2: Đổi 10km sang mile
kilometers = 10
mile = kilometers / 1.60934
print("Miles: ", mile)
# Câu 3: Tính average pace và speed (10km trong 42 phút 42 giây)
time_hours = total_seconds / 3600
speed = kilometers / time_hours
pace = total_seconds / kilometers
print("Average speed (km/h): ", speed)
print("Average pace (seconds/km): ", pace)