from pymodbus.client.sync import ModbusTcpClient

modbus_IP = "192.163.1.51"
modbus_port = 502

client = ModbusTcpClient(modbus_IP, port= modbus_port)

try:
    if client.connect():
        result = client.read_holding_registers(address=0, count=5, unit= 1)


        if result.isError():
            print("讀取失敗", result)
        else:
            print("讀取結果:", result.registers)

    else:
        print("無法連線到modbus設備")

finally:
    client.close()
