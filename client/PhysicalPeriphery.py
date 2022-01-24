"""
    .
    Tu znajdą się metody do interakcji z fizycznymi peryferiami
"""
SIMULATION_MODE = True

SIMULATION_EXTERNAL_TEMPERATURE = 10.0
SIMULATION_EXTERNAL_TEMPERATURE_CHANGE = 1.0
SIMULATION_EXTERNAL_TEMPERATURE_MAX = 22.0
SIMULATION_EXTERNAL_TEMPERATURE_MIN = 10.0
SIMULATION_EXTERNAL_HUMIDITY = 0.5
SIMULATION_EXTERNAL_HUMIDITY_CHANGE = 0.01
SIMULATION_EXTERNAL_LIGHTING = 400.0
SIMULATION_EXTERNAL_LIGHTING_CHANGE = 100.0
SIMULATION_EXTERNAL_WIND = 10.0
SIMULATION_EXTERNAL_WIND_CHANGE = 1.0

SIMULATION_INTERNAL_TEMPERATURE = 18.0
SIMULATION_INTERNAL_TEMPERATURE_CHANGE = 0.1
SIMULATION_INTERNAL_HUMIDITY = 0.5
SIMULATION_INTERNAL_HUMIDITY_CHANGE = 0.01
SIMULATION_INTERNAL_LIGHTING = 1000.0
SIMULATION_INTERNAL_LIGHTING_CHANGE = 10.0

SIMULATION_DAY = True

if not SIMULATION_MODE:
    import config as cfg
    import w1thermsensor
    import board
    import busio
    import adafruit_bme280.advanced as adafruit_bme280


def bme280():
   i2c = busio.I2C(board.SCL, board.SDA)
   bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, 0x76)

   bme280.sea_level_pressure = 1013.25
   bme280.standby_period = adafruit_bme280.STANDBY_TC_500
   bme280.iir_filter = adafruit_bme280.IIR_FILTER_X16
   bme280.overscan_pressure = adafruit_bme280.OVERSCAN_X16
   bme280.overscan_humidity = adafruit_bme280.OVERSCAN_X1
   bme280.overscan_temperature = adafruit_bme280.OVERSCAN_X2

#    print("\nBME280:")
#    print(f"Temperature: {bme280.temperature:0.1f} ’+chr(176)+’C")
#    print(f"Humidity: {bme280.humidity:0.1f} %")
#    print(f"Pressure: {bme280.pressure:0.1f} hPa")
#    print(f"Altitude: {bme280.altitude:0.2f} meters")

   return (bme280.temperature, bme280.humidity)

def ds18b20():
   sensor = w1thermsensor.W1ThermSensor()
   temp = sensor.get_temperature()
   return temp

def resolve_simulation_day():
    global SIMULATION_DAY
    if SIMULATION_EXTERNAL_TEMPERATURE == SIMULATION_EXTERNAL_TEMPERATURE_MAX:
        SIMULATION_DAY = False
    if SIMULATION_EXTERNAL_TEMPERATURE == SIMULATION_EXTERNAL_TEMPERATURE_MIN:
        SIMULATION_DAY = True

def print_data_from_external_sensors(temp, hum, light, wind, simulated):
    if simulated:
        print("Retrieved simulated data from external sensors: temp: " + str(temp) + ", hum: " + str(hum) + ", light: " + str(light) +", wind: " + str(wind))
    else:
        print("Retrieved data from external sensors: temp: " + str(temp) + ", hum: " + str(hum) + ", light: " + str(light) +", wind: " + str(wind))
    

def print_data_from_internal_sensors(temp, hum, light, simulated):
    if simulated:
        print("Retrieved simulated data from internal sensors: temp: " + str(temp) + ", hum: " + str(hum) + ", light: " + str(light))
    else:
        print("Retrieved data from internal sensors: temp: " + str(temp) + ", hum: " + str(hum) + ", light: " + str(light))


def get_external_sensors_data() -> tuple[float, float, float, float]:
    """
    temperatura, wilgotnosc, wiatr, swiatlo
    """
    global SIMULATION_EXTERNAL_TEMPERATURE
    global SIMULATION_EXTERNAL_HUMIDITY
    global SIMULATION_EXTERNAL_LIGHTING
    global SIMULATION_EXTERNAL_WIND
    
    if SIMULATION_MODE:
        resolve_simulation_day()
        if SIMULATION_DAY:
            SIMULATION_EXTERNAL_TEMPERATURE += SIMULATION_EXTERNAL_TEMPERATURE_CHANGE
            SIMULATION_EXTERNAL_HUMIDITY += SIMULATION_EXTERNAL_HUMIDITY_CHANGE
            SIMULATION_EXTERNAL_LIGHTING += SIMULATION_EXTERNAL_LIGHTING_CHANGE
            SIMULATION_EXTERNAL_WIND += SIMULATION_EXTERNAL_WIND_CHANGE
        else:
            SIMULATION_EXTERNAL_TEMPERATURE -= SIMULATION_EXTERNAL_TEMPERATURE_CHANGE
            SIMULATION_EXTERNAL_HUMIDITY -= SIMULATION_EXTERNAL_HUMIDITY_CHANGE
            SIMULATION_EXTERNAL_LIGHTING -= SIMULATION_EXTERNAL_LIGHTING_CHANGE
            SIMULATION_EXTERNAL_WIND -= SIMULATION_EXTERNAL_WIND_CHANGE
        print_data_from_external_sensors(SIMULATION_EXTERNAL_TEMPERATURE, SIMULATION_EXTERNAL_HUMIDITY, SIMULATION_EXTERNAL_WIND, SIMULATION_EXTERNAL_LIGHTING, True)
        return SIMULATION_EXTERNAL_TEMPERATURE, SIMULATION_EXTERNAL_HUMIDITY, SIMULATION_EXTERNAL_WIND, SIMULATION_EXTERNAL_LIGHTING
    else:
        temp, hum = bme280()
        print_data_from_external_sensors(temp, hum, 0.0, 0.0, False)
        return temp, hum, 0.0, 0.0

def get_internal_sensors_data() -> tuple[float, float, float]:
    """
    temperatura, wilgotnosc, swiatlo,
    """
    global SIMULATION_INTERNAL_TEMPERATURE
    global SIMULATION_INTERNAL_HUMIDITY
    global SIMULATION_INTERNAL_LIGHTING
    
    if SIMULATION_MODE:
        resolve_simulation_day()
        if SIMULATION_DAY:
            SIMULATION_INTERNAL_TEMPERATURE += SIMULATION_INTERNAL_TEMPERATURE_CHANGE
            SIMULATION_INTERNAL_HUMIDITY += SIMULATION_INTERNAL_HUMIDITY_CHANGE
            SIMULATION_INTERNAL_LIGHTING += SIMULATION_INTERNAL_LIGHTING_CHANGE
        else:
            SIMULATION_INTERNAL_TEMPERATURE -= SIMULATION_INTERNAL_TEMPERATURE_CHANGE
            SIMULATION_INTERNAL_HUMIDITY -= SIMULATION_INTERNAL_HUMIDITY_CHANGE
            SIMULATION_INTERNAL_LIGHTING -= SIMULATION_INTERNAL_LIGHTING_CHANGE
        print_data_from_internal_sensors(SIMULATION_EXTERNAL_TEMPERATURE, SIMULATION_EXTERNAL_HUMIDITY, SIMULATION_EXTERNAL_LIGHTING, True)
        return SIMULATION_INTERNAL_TEMPERATURE,SIMULATION_INTERNAL_HUMIDITY,SIMULATION_INTERNAL_LIGHTING
    else:
        temp = ds18b20()
        print_data_from_internal_sensors(temp, 0.0, 0.0, False)
        return temp, 0.0, 0.0


def set_light(wlaczone: bool):
    """
    Jeśli true to włączamy światla ...
    """
    if SIMULATION_MODE:
        if wlaczone:
            print('Wlaczam swiatla')
        else:
            print('Wylaczam swiatla')


def set_windows(otwarte: bool):
    """
    Jeśli true to otwieramy okna ...
    """
    if SIMULATION_MODE:
        if otwarte:
            print('Otwieram okna')
        else:
            print('Zamykam okna')
