from pymodbus.client.sync import ModbusTcpClient
import csv
import time
from datetime import datetime

# Modbus 設備的 IP 和 Port
MODBUS_IP = "192.168.1.51"
MODBUS_PORT = 502

# 建立 ModbusClient 實例
client = ModbusTcpClient(MODBUS_IP, port=MODBUS_PORT)

# CSV 文件的列標題
csv_header = ['Timestamp', 'Register_0', 'Register_1', 'Register_2', 'Register_3', 'Register_4']

# CSV 文件的文件名
csv_filename = 'modbus_data.csv'

try:
    # 開啟CSV文件並寫入列標題
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(csv_header)

    # 循環讀取 Modbus 寄存器並記錄數據
    while True:
        # 開啟連線
        if client.connect():
            # 進行 Modbus 讀取操作，例如讀取保持寄存器的值
            # 請根據實際情況修改寄存器地址和數量
            result = client.read_holding_registers(address=0, count=5, unit=1)

            # 檢查是否成功讀取
            if result.isError():
                print("讀取失敗:", result)
            else:
                # 獲取當前時間戳
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # 輸出讀取結果和時間戳
                print("讀取結果:", result.registers, "時間:", timestamp)

                # 將數據寫入CSV文件
                with open(csv_filename, 'a', newline='', encoding='utf-8') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow([timestamp] + list(result.registers))

                # 等待一秒
                time.sleep(1)

        else:
            print("無法連線到 Modbus 設備")

finally:
    # 關閉連線
    client.close()
