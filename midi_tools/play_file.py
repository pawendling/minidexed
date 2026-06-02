import mido

# ==========================================
# MIDI SPLITTER
# Bus 1 = accompaniment / rhythm section
# Bus 2 = leads / pads / melody
# ==========================================

out1 = mido.open_output('IAC Driver Bus 1')
out2 = mido.open_output('IAC Driver Bus 2')

#mid = mido.MidiFile('/Users/pawendling/Downloads/ABBA_The_Winner_Takes_It_All.mid')
mid = mido.MidiFile('/Users/pawendling/Downloads/Aha - Take on Me.mid')

# MIDI channels in file are zero-based internally:
# Ch1 = 0, Ch2 = 1 ... Ch16 = 15

# Send to BUS 1:
# Piano, bass, drums, guitars
bus1_channels = {
    1,   # Ch2 Piano
    2,   # Ch3 Synth Bass
    3,   # Ch4 Piano
    5,   # Ch6 Piano
    7,   # Ch8 Piano
    9,   # Ch10 Drums
    10,  # Ch11 Piano
    11,  # Ch12 Guitar
    12,  # Ch13 Piano
    14,  # Ch15 Piano
    15   # Ch16 Nylon Guitar
}

# Send to BUS 2:
# Strings, brass, leads
bus2_channels = {
    0,   # Ch1 Strings
    4,   # Ch5 Saw Lead
    6,   # Ch7 Brass
    8,   # Ch9 Strings
    13   # Ch14 Calliope Lead
}

for msg in mid.play():

    if hasattr(msg, 'channel'):

        if msg.channel in bus1_channels:
            out1.send(msg)

        if msg.channel in bus2_channels:
            out2.send(msg)

    else:
        # timing/meta/system messages to both
        out1.send(msg)
        out2.send(msg)
