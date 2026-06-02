import mido 

out = mido.open_output('USB MIDI Interface') 
out.send(mido.Message('note_on', note=60, velocity=100, channel=1))

