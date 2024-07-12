import time
import smbus2

i2cbus = smbus2.SMBus(1)


def getDataFromDHT20(adress):
    time.sleep(0.5)
    data = i2cbus.read_i2c_block_data(adress, 0x71, 1)
    if (data[0] | 0x08) == 0:
        print('Initialization error')
    i2cbus.write_i2c_block_data(adress, 0xac, [0x33, 0x00])
    time.sleep(0.1)
    data = i2cbus.read_i2c_block_data(adress, 0x71, 7)
    return data


def getTemperature(address):
    data = getDataFromDHT20(address)
    tempRaw = ((data[3] & 0xf) << 16) + (data[4] << 8) + data[5]
    temperature = 200 * float(tempRaw) / 2 ** 20 - 50
    return temperature


def getHumidity(address):
    data = getDataFromDHT20(address)
    humRaw = ((data[3] & 0xf0) >> 4) + (data[1] << 12) + (data[2] << 4)
    humidity = 100 * float(humRaw) / 2 ** 20
    return humidity
