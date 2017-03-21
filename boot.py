from machine import UART
import os
uart = UART(0, 115200)
os.dupterm(uart)
