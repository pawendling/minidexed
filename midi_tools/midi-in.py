import mido

# List available input ports just to be sure
print("Available inputs:", mido.get_input_names())

try:
    # Open the input port for your interface
    with mido.open_input('USB MIDI Interface') as inport:
        print("\n--- Listening for MIDI messages on 'USB MIDI Interface' ---")
        print("Play some keys on your Clavinova... (Press Ctrl+C to stop)")
        
        # This loop stays open and prints every message as it arrives
        for msg in inport:
            print(f"Received: {msg}")
            
except IOError:
    print("Error: Could not find 'USB MIDI Interface'. Is it plugged in?")
except KeyboardInterrupt:
    print("\nStopping listener...")

