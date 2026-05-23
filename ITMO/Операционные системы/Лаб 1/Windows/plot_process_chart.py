import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Чтение данных из CSV
df = pd.read_csv("process_monitor.csv")

# Преобразование столбца Time (формат HH:mm:ss) в datetime
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S')

# Вычисление относительного времени (секунды от первого момента времени)
t0 = df['Time'][0]
df['RelativeTime'] = (df['Time'] - t0).dt.total_seconds()

# Построение графика
plt.plot(df['RelativeTime'], df['Count'], marker='o')
plt.title("Количество процессов во времени")
plt.xlabel("Время (секунды с начала)")
plt.ylabel("Количество процессов")
plt.grid(True)
plt.tight_layout()
plt.show()
