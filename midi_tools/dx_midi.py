import mido
import time

# 1. Open the virtual port you created (e.g., 'loopMIDI Port')
# Use mido.get_output_names() to find the exact name
port_name = 'loopMIDI Port' 
outport = mido.open_output(port_name)

# 2. Load your MIDI file
mid = mido.MidiFile('')

# 3. Play the file to Dexed
for msg in mid.play():
    outport.send(msg)

outport.close()
