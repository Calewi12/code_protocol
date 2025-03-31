# import modules
from machine import UART
from machine import Pin
import time
import uasyncio as asyncio


MAX_MESSAGE_LEN=64
team = [b'a',b'b',b'c',b'd']
id = b'a'
broadcast = 'X'

# initialize a new UART class
uart = UART(2, 9600,tx=17,rx=16)
# run the init method with more details including baudrate and parity
uart.init(9600, bits=8, parity=None, stop=1) 
# define pin 2 as an output with name led. (Pin 2 is connected to the ESP32-WROOM dev board's onboard blue LED)
led = Pin(2,Pin.OUT)


def send_message(message):
    print('ESP: send message')
    # send_queue.append(message)

def handle_message(message):
    my_string = message.decode('utf-8')
    print('ESP: handling my message',message)
    


async def process_rx():
    while True:
        c = uart.read(1)
        if c:
            print("ESP received raw byte:", c)
    await asyncio.sleep_ms(10)    

async def heartbeat():

    while True:
        print('ESP: sending')
        uart.write(b'AZabHello!YB')
        await asyncio.sleep(10)    



async def main():
    while True:
        await asyncio.sleep(1)

asyncio.create_task(process_rx())
asyncio.create_task(heartbeat())

try:
    asyncio.run(main())
finally:
    asyncio.new_event_loop()
