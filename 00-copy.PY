import time
from pymodbus.client.sync import ModbusTcpClient

# Modbus 設備的 IP 和 Port
MODBUS_IP = "192.168.1.51"
MODBUS_PORT = 502

# 建立 ModbusClient 實例
client = ModbusTcpClient(MODBUS_IP, port=MODBUS_PORT)


   

# main read loop
while True:
        try:
        # 開啟連線
            if client.connect():
                # 進行 Modbus 讀取操作，例如讀取保持寄存器的值
                # 請根據實際情況修改寄存器地址和數量
                result = client.read_holding_registers(address=0, count=5, unit=1)

                # 檢查是否成功讀取
                if result.isError():
                    print("讀取失敗:", result)
                else:
                    print("讀取結果:", result.registers)

            else:
                print("無法連線到 Modbus 設備")

        finally:
        # 關閉連線
            client.close()
    # sleep 2s before next polling
        time.sleep(1)