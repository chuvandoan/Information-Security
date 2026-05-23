import matplotlib.pyplot as plt

# Đọc dữ liệu từ file
timestamps = []
process_counts = []

with open("process_log.txt", "r") as f:
    for line in f:
        ts, count = line.strip().split()
        timestamps.append(int(ts))
        process_counts.append(int(count))

# Chuyển timestamp về dạng thời gian tương đối (giây từ thời điểm đầu tiên)
t0 = timestamps[0]
relative_time = [t - t0 for t in timestamps]

# Vẽ đồ thị
plt.plot(relative_time, process_counts, marker='o')
plt.title("Количество процессов во времени")
plt.xlabel("Время (секунды)")
plt.ylabel("Количество процессов")
plt.grid(True)
plt.tight_layout()
plt.show()
