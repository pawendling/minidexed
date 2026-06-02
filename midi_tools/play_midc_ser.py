import mido
import serial
import time

# 1. Open the raw macOS serial port. 
# Standard MIDI uses 31250 baud. Change to 115200 if using a custom Arduino/DIY interface.
#ser = serial.Serial('/dev/cu.usbserial-0001', baudrate=31250, timeout=1)
#ser = serial.Serial('/dev/cu.usbserial-1420', baudrate=31250, timeout=0.1, write_timeout=1, inter_byte_timeout=0.01)
ser = serial.Serial('/dev/cu.usbserial-0001', baudrate=31250, timeout=0.1, write_timeout=1, inter_byte_timeout=0.01)

# 2. Construct your Mido message exactly as you did before
msg = mido.Message('note_on', note=60, velocity=100, channel=0) # Note: Channel 0 in Mido is 0 internally

try:
    # 3. Convert the Mido message to raw bytes and send them over the serial connection
    ser.write(msg.bytes())
    print(f"Sent: {msg} as bytes {msg.bytes()}")
    
    # Keep the note playing for 1 second
    time.sleep(1)
    
    # 4. Send a note_off message to stop the sound
    off_msg = mido.Message('note_off', note=60, velocity=0, channel=0)
    ser.write(off_msg.bytes())
    print(f"Sent: {off_msg}")

finally:
    # Always close the port when done to prevent the device from locking up
    ser.close()

