from skyfield.api import load
import matplotlib.pyplot as plt
import numpy as np

# 1. 加载 TLE 文件（CelesTrak 提供的 Starlink TLE）
# stations_url = "https://celestrak.org/NORAD/elements/starlink.txt"
# stations_url = 'https://celestrak.org/NORAD/elements/stations.txt'
starlink = 'starlink-reentry.txt'
satellites = load.tle_file(starlink)

print("共载入卫星数量:", len(satellites))

# 2. 选择一颗 Starlink 卫星，例如第一颗
satellite = satellites[0]
print("选择卫星:", satellite)

# 3. 设定时间范围
ts = load.timescale()
hours = range(0, 23, 2)   # 每 2 小时
time_list = [ts.utc(2025,9,d,h,0,0) for d in range(26,30) for h in hours]

altitude = []
for times in time_list:
    print('times:', times)
    geocentric = satellite.at(times) # 4. 计算卫星的地心坐标
    subpoint = geocentric.subpoint() # 5. 提取高度（地心半径 - 地球半径
    altitudes_km = subpoint.elevation.km
    print('altitude:', altitudes_km)
    altitude.append(altitudes_km)

altitude = np.array(altitude)

# 6. 绘制高度轨迹
plt.figure(figsize=(10,5))
plt.plot(altitude)
plt.xlabel("Time (hour)")
plt.ylabel("Altitude (km)")
plt.title(f"Satellite altitude: {satellite.name}")
plt.grid(True)
plt.show()
