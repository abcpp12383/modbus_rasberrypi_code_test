from pyModbusTCP.client import ModbusClient

# TCP auto connect on first modbus request
c = ModbusClient(host="192.168.1.51", port=502, unit_id=1, auto_open=True)

regs = c.read_holding_registers(0,5)

if regs:
    print(regs)
else:
    print("read error")
    
