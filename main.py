import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import Workbook
url='https://thethao247.vn/livescores/anh/ngoai-hang-anh/standings/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extract data from the parsed HTML
    datas = soup.find('div', class_='table-standings')
    table= datas.find('table')
    all = table.find_all('tr')
    results = []
    for alls in all:
        col  = alls.find_all('td')
        # print(col )
        if col :
            stt = col[0].find('span').text.strip()
            name= col[0].find('strong').text.strip()
            tran = col[1].text.strip()
            win = col[2].text.strip()
            hSo = col[3].text.strip()
            diem = col[4].text.strip()
            result = {
                "Xếp Hạng": stt,
                "Name": name,
                "Số Trận": tran,
                "Thắng": win,
                "Hiệu Số": hSo,
                "Điểm": diem
            }
            # print(result)
            results.append(result)
            # print("\n")
    workbook = Workbook()
    worksheet = workbook.active

    # Add headers to the Excel sheet
    headers = ["Xếp Hạng", "Name", "Số Trận", "Thắng", "Hiệu Số", "Điểm"]
    worksheet.append(headers)

    # Add data rows to the Excel sheet
    for result in results:
        row = [result["Xếp Hạng"], result["Name"], result["Số Trận"], result["Thắng"], result["Hiệu Số"], result["Điểm"]]
        worksheet.append(row)

    # Save the Excel file
    excel_file_name = 'premier_league_standings.xlsx'
    workbook.save(excel_file_name)

    print(f"Data has been successfully exported to '{excel_file_name}'.")

else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")