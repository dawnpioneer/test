import requests
from bs4 import BeautifulSoup
import csv

# 設定網站連結
url = "http://www.ither.com.tw/ither/index_search.asp"

# 定義 headers，模擬瀏覽器請求
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}

# 發送 GET 請求取得網頁內容
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("成功獲取網頁內容！")

    # 使用 Beautiful Soup 解析 HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # 找到包含 MUS 下載連結的所有元素
    mus_links = soup.find_all("a", href=lambda href: href and "MUS" in href)

    # 儲存解析出的檔案名稱和下載連結
    data = []

    # 迴圈遍歷所有找到的下載連結
    for link in mus_links:
        # 取得檔案名稱
        file_name = link.text.strip()
        file_name = file_name.replace("〔", "").replace("〕", "")  # 移除多餘的字元

        # 取得下載連結
        download_link = link.get("href")

        # 將檔案名稱和下載連結儲存到 data 中
        data.append((file_name, download_link))

    # 將 data 儲存為 CSV 檔案
    with open("download_links.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["檔案名稱", "下載連結"])  # 寫入 CSV 標題行
        writer.writerows(data)  # 寫入資料到 CSV 檔案

    print("下載連結已儲存至 download_links.csv 檔案了唷！")
else:
    print("無法獲取網頁內容！")
