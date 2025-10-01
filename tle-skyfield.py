from skyfield.api import load
import matplotlib.pyplot as plt
import numpy as np

# 1. 加载 TLE 文件（CelesTrak 提供的 Starlink TLE）
# stations_url = "https://celestrak.org/NORAD/elements/starlink.txt"
# stations_url = 'https://celestrak.org/NORAD/elements/stations.txt'
stations_url = 'https://celestrak.org/NORAD/elements/starlink-reentry.txt'
satellites = load.tle_file(stations_url)

print("共载入卫星数量:", len(satellites))

# 2. 选择一颗 Starlink 卫星，例如第一颗
satellite = satellites[0]
print("选择卫星:", satellite)

# 3. 设定时间范围（未来 424 小时，每 10 分钟）
ts = load.timescale()
# t0 = ts.now()
t0 = ts.utc(2025,9,26,0,0,0)
# minutes = np.arange(0, 24*60, 10)   # 每 10 分钟
# seconds = minutes * 60.0 # 转换为秒
t1 = ts.utc(2025,9,26,12,0,0)
t2 = ts.utc(2025,9,27,0,0,0)
t3 = ts.utc(2025,9,27,12,0,0)
t4 = ts.utc(2025,9,28,0,0,0)
t5 = ts.utc(2025,9,28,12,0,0)
t6 = ts.utc(2025,9,29,0,0,0)
times_list = [t0, t1, t2, t3, t4, t5, t6]
altitude = []
for times in times_list:
    print('times:', times)
    geocentric = satellite.at(times) # 4. 计算卫星的地心坐标
    subpoint = geocentric.subpoint() # 5. 提取高度（地心半径 - 地球半径
    altitudes_km = subpoint.elevation.km
    print('altitude:', altitudes_km)
    altitude.append(altitudes_km)

altitude = np.array(altitude)
# 6. 绘制高度轨迹
plt.figure(figsize=(10,5))
# plt.plot(minutes/60, altitude)
plt.plot(altitude, 'ro-')
plt.xlabel("Time (hour)")
plt.ylabel("Altitude (km)")
plt.title(f"Satellite altitude: {satellite.name}")
plt.grid(True)
plt.show()
