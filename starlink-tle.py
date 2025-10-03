import requests

def download_starlink_tle(filename="starlink_tle.txt"):
    """
    从 CelesTrak 下载所有 Starlink 卫星的 TLE 数据并保存到本地文件
    """
    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=tle"
    
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"Starlink TLE 数据已保存到 {filename}")
    else:
        print("下载失败，状态码:", response.status_code)

if __name__ == "__main__":
    download_starlink_tle("starlink_tle.txt")
