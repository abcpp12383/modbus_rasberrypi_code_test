import modbus_tk.modbus_tcp as mt
import modbus_tk.defines as md
import json
# 遠端連線到伺服器端
master = mt.TcpMaster("192.168.1.51", port=502)
master.set_timeout(1.0)

# @slave=1 就是modbus ID 數值從 1 to 247.  0為廣播所有的站號
# @function_code=READ_HOLDING_REGISTERS：功能碼
#[控制碼01]READ_COILS
#[控制碼02]READ_DISCRETE_INPUTS
#[控制碼03]READ_HOLDING_REGISTERS 讀取輸入寄存器
#[控制碼04]READ_INPUT_REGISTERS 讀取輸入寄存器
#[控制碼05]WRITE_SINGLE_COIL 
#[控制碼06]WRITE_SINGLE_REGISTER
#[控制碼15]WRITE_MULTIPLE_COILS
#[控制碼16]WRITE_MULTIPLE_REGISTERS

# @starting_address=1：開始地址，如果說明文件是給16進位的地址如64 需要改為10進位成100
# @quantity_of_x=3：回傳地址的的數量
# @output_value：一個整數或可迭代的值：1/[1,1,1,0,0,1]/xrange(12)
# @data_format
# @expected_length
Hold_value = master.execute(slave=1, 
                            function_code=md.READ_INPUT_REGISTERS, 
                            starting_address=108, 
                            quantity_of_x=8, 
                            output_value=7)

print(json.dumps(Hold_value))  # 取到的暫存器的值格式為元組(456, 288)