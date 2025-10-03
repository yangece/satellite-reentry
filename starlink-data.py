import requests
import csv

# 你的 Space-Track 账户信息
USERNAME = "yangzhao.ge@outlook.com"
PASSWORD = "UAlbany2006"

# 登录 URL
LOGIN_URL = "https://www.space-track.org/ajaxauth/login"

# 查询 Starlink 数据
QUERY_URL = (
    "https://www.space-track.org/basicspacedata/query/"
    "class/decay/OBJECT_NAME/~~STARLINK/"
    "orderby/DECAY_EPOCH desc/format/json"
)

def fetch_starlink_reentry(username, password):
    # 建立 Session
    session = requests.Session()

    # 登录
    login_data = {"identity": username, "password": password}
    resp = session.post(LOGIN_URL, data=login_data)
    resp.raise_for_status()

    # 请求数据
    r = session.get(QUERY_URL)
    r.raise_for_status()
    data = r.json()

    return data

def save_to_csv(data, filename="starlink_reentry.csv"):
    # 提取 NORAD ID，卫星名称，坠落时间及RCS尺寸
    rows = [(item["NORAD_CAT_ID"], item["OBJECT_NAME"], item["DECAY_EPOCH"], item["RCS_SIZE"]) for item in data]

    # 写入 CSV
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["NORAD_CAT_ID", "OBJECT_NAME", "DECAY_EPOCH", "RCS_SIZE"])
        writer.writerows(rows)

    print(f"已保存 {len(rows)} 条记录到 {filename}")

if __name__ == "__main__":
    data = fetch_starlink_reentry(USERNAME, PASSWORD)
    # 提取星链数据
    starlink_data = [item for item in data if "starlink" in item["OBJECT_NAME"].lower()]
    # 提取历史数据
    starlink_hist = [item for item in starlink_data if item["MSG_TYPE"] == "Historical"]
    save_to_csv(starlink_hist)