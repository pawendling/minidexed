#
# open -n -a "Dexed"
#

import mido


# General MIDI Level 1 instrument names (Program numbers 0-127)
GM_INSTRUMENTS = {
    0: "Acoustic Grand Piano",
    1: "Bright Acoustic Piano",
    2: "Electric Grand Piano",
    3: "Honky-tonk Piano",
    4: "Electric Piano 1",
    5: "Electric Piano 2",
    6: "Harpsichord",
    7: "Clavinet",
    8: "Celesta",
    9: "Glockenspiel",
    10: "Music Box",
    11: "Vibraphone",
    12: "Marimba",
    13: "Xylophone",
    14: "Tubular Bells",
    15: "Dulcimer",
    16: "Drawbar Organ",
    17: "Percussive Organ",
    18: "Rock Organ",
    19: "Church Organ",
    20: "Reed Organ",
    21: "Accordion",
    22: "Harmonica",
    23: "Tango Accordion",
    24: "Acoustic Guitar (nylon)",
    25: "Acoustic Guitar (steel)",
    26: "Electric Guitar (jazz)",
    27: "Electric Guitar (clean)",
    28: "Electric Guitar (muted)",
    29: "Overdriven Guitar",
    30: "Distortion Guitar",
    31: "Guitar Harmonics",
    32: "Acoustic Bass",
    33: "Electric Bass (finger)",
    34: "Electric Bass (pick)",
    35: "Fretless Bass",
    36: "Slap Bass 1",
    37: "Slap Bass 2",
    38: "Synth Bass 1",
    39: "Synth Bass 2",
    40: "Violin",
    41: "Viola",
    42: "Cello",
    43: "Contrabass",
    44: "Tremolo Strings",
    45: "Pizzicato Strings",
    46: "Orchestral Harp",
    47: "Timpani",
    48: "String Ensemble 1",
    49: "String Ensemble 2",
    50: "Synth Strings 1",
    51: "Synth Strings 2",
    52: "Choir Aahs",
    53: "Voice Oohs",
    54: "Synth Choir",
    55: "Orchestra Hit",
    56: "Trumpet",
    57: "Trombone",
    58: "Tuba",
    59: "Muted Trumpet",
    60: "French Horn",
    61: "Brass Section",
    62: "Synth Brass 1",
    63: "Synth Brass 2",
    64: "Soprano Sax",
    65: "Alto Sax",
    66: "Tenor Sax",
    67: "Baritone Sax",
    68: "Oboe",
    69: "English Horn",
    70: "Bassoon",
    71: "Clarinet",
    72: "Piccolo",
    73: "Flute",
    74: "Recorder",
    75: "Pan Flute",
    76: "Blown Bottle",
    77: "Shakuhachi",
    78: "Whistle",
    79: "Ocarina",
    80: "Lead 1 (square)",
    81: "Lead 2 (sawtooth)",
    82: "Lead 3 (calliope)",
    83: "Lead 4 (chiff)",
    84: "Lead 5 (charang)",
    85: "Lead 6 (voice)",
    86: "Lead 7 (fifths)",
    87: "Lead 8 (bass+lead)",
    88: "Pad 1 (new age)",
    89: "Pad 2 (warm)",
    90: "Pad 3 (polysynth)",
    91: "Pad 4 (choir)",
    92: "Pad 5 (bowed)",
    93: "Pad 6 (metallic)",
    94: "Pad 7 (halo)",
    95: "Pad 8 (sweep)",
    96: "FX 1 (rain)",
    97: "FX 2 (soundtrack)",
    98: "FX 3 (crystal)",
    99: "FX 4 (atmosphere)",
    100: "FX 5 (brightness)",
    101: "FX 6 (goblins)",
    102: "FX 7 (echoes)",
    103: "FX 8 (sci-fi)",
    104: "Sitar",
    105: "Banjo",
    106: "Shamisen",
    107: "Koto",
    108: "Kalimba",
    109: "Bag Pipe",
    110: "Fiddle",
    111: "Shanai",
    112: "Tinkle Bell",
    113: "Agogo",
    114: "Steel Drums",
    115: "Woodblock",
    116: "Taiko Drum",
    117: "Melodic Tom",
    118: "Synth Drum",
    119: "Reverse Cymbal",
    120: "Guitar Fret Noise",
    121: "Breath Noise",
    122: "Seashore",
    123: "Bird Tweet",
    124: "Telephone Ring",
    125: "Helicopter",
    126: "Applause",
    127: "Gunshot"
}

def get_midi_instruments(file_path):
    # Load MIDI file
    mid = mido.MidiFile(file_path)

    # Default all channels to Program 0
    channel_instruments = {i: 0 for i in range(16)}

    # Channel 10 (index 9) = drums
    channel_instruments[9] = "Percussion/Drums"

    for track in mid.tracks:
        for msg in track:
            if msg.type == 'program_change':
                channel_instruments[msg.channel] = msg.program

    print(f"{'Channel':<8} | {'Program':<8} | Instrument")
    print("-" * 50)

    for channel, program in channel_instruments.items():
        if channel == 9:
            print(f"{channel+1:<8} | {'--':<8} | Percussion/Drums")
        else:
            name = GM_INSTRUMENTS.get(program, "Unknown")
            print(f"{channel+1:<8} | {program:<8} | {name}")

# =====================================================
# 8-BUS MIDI SPLITTER WITH CTRL-C MIDI PANIC RESET
# =====================================================

MIDI_FILE = '/Users/pawendling/Downloads/Aha - Take on Me.mid'
# MIDI_FILE = '/Users/pawendling/Downloads/ABBA_The_Winner_Takes_It_All.mid'


def open_outputs():
    return [
        mido.open_output('IAC Driver Bus 1'),
        mido.open_output('IAC Driver Bus 2'),
        mido.open_output('IAC Driver Bus 3'),
        mido.open_output('IAC Driver Bus 4'),
        mido.open_output('IAC Driver Bus 5'),
        mido.open_output('IAC Driver Bus 6'),
        mido.open_output('IAC Driver Bus 7'),
        mido.open_output('IAC Driver Bus 8'),
    ]


def midi_panic(outputs):
    """
    Send MIDI reset / all notes off / sustain off
    Clears stuck notes if Ctrl-C is pressed.
    """
    print("\nSending MIDI panic reset...")

    for out in outputs:
        for ch in range(16):
            out.send(mido.Message('control_change', channel=ch, control=64, value=0))   # Sustain Off
            out.send(mido.Message('control_change', channel=ch, control=123, value=0))  # All Notes Off
            out.send(mido.Message('control_change', channel=ch, control=121, value=0))  # Reset Controllers


def play_file(filename):
    outputs = open_outputs()

    out1, out2, out3, out4, out5, out6, out7, out8 = outputs

    mid = mido.MidiFile(filename)

    # MIDI channels internally start at zero:
    # Ch1=0 ... Ch16=15

    bus1 = {1, 3, 5, 7, 10, 12, 14}   # Piano
    bus2 = {2}                        # Bass
    bus3 = {9}                        # Drums
    bus4 = {11, 15}                   # Guitars
    bus5 = {0, 8}                     # Strings
    bus6 = {6}                        # Brass
    bus7 = {4}                        # Lead 1
    bus8 = {13}                       # Lead 2

    try:
        for msg in mid.play():

            if msg.type == 'program_change':
                continue  # ignore patch changes completely

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
                for out in outputs:
                    out.send(msg)

    except KeyboardInterrupt:
        print("\nInterrupted by user (Ctrl-C).")
        midi_panic(outputs)

    finally:
        midi_panic(outputs)

        for out in outputs:
            out.close()


def main():
    get_midi_instruments(MIDI_FILE)
    play_file(MIDI_FILE)


if __name__ == "__main__":
    main()
