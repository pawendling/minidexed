#
# open -n -a "Dexed"  
# 
#
import mido

# ==========================================
# 8-BUS MIDI SPLITTER
# ==========================================

out1 = mido.open_output('IAC Driver Bus 1')
out2 = mido.open_output('IAC Driver Bus 2')
out3 = mido.open_output('IAC Driver Bus 3')
out4 = mido.open_output('IAC Driver Bus 4')
out5 = mido.open_output('IAC Driver Bus 5')
out6 = mido.open_output('IAC Driver Bus 6')
out7 = mido.open_output('IAC Driver Bus 7')
out8 = mido.open_output('IAC Driver Bus 8')

# mid = mido.MidiFile('/Users/pawendling/Downloads/ABBA_The_Winner_Takes_It_All.mid')
mid = mido.MidiFile('/Users/pawendling/Downloads/Aha - Take on Me.mid')

# MIDI channels internally:
# Ch1=0 ... Ch16=15

# ------------------------------------------
# One musical role per bus
# ------------------------------------------

bus1 = {1, 3, 5, 7, 10, 12, 14}   # Piano channels
bus2 = {2}                        # Synth Bass
bus3 = {9}                        # Drums
bus4 = {11, 15}                   # Guitars
bus5 = {0, 8}                     # Strings
bus6 = {6}                        # Brass
bus7 = {4}                        # Lead Sawtooth
bus8 = {13}                       # Lead Calliope

for msg in mid.play():

    if hasattr(msg, 'channel'):

        if msg.channel in bus1:
            out1.send(msg)

        if msg.channel in bus2:
            out2.send(msg)

        if msg.channel in bus3:
            out3.send(msg)

        if msg.channel in bus4:
            out4.send(msg)

        if msg.channel in bus5:
            out5.send(msg)

        if msg.channel in bus6:
            out6.send(msg)

        if msg.channel in bus7:
            out7.send(msg)

        if msg.channel in bus8:
            out8.send(msg)

    else:
        # Send timing/system/meta to all buses
        out1.send(msg)
        out2.send(msg)
        out3.send(msg)
        out4.send(msg)
        out5.send(msg)
        out6.send(msg)
        out7.send(msg)
        out8.send(msg)
