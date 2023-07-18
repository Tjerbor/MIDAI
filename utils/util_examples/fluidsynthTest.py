from midi2audio import FluidSynth
import os

fs = FluidSynth('C:\\Users\\Thiemo\\IdeaProjects\\Bildverarbeitung\\mg_symphony_hall_bank.SF2')
#fs.play_midi('D:\\Daten\\Dokumente\\FL Studio 20\\Midis\\Deep Haus Chords.mid')
fs.midi_to_audio('D:\\Daten\\Dokumente\\FL Studio 20\\Midis\\Cymatics Freebies - MIDI\\Cymatics - MIDI Chord Progressions Vol 3\\Cymatics - MIDI 21 - C#.mid','D:\\Daten\\Musik\\FL Studio\\out1.wav')
fs.midi_to_audio('D:\\Daten\\Dokumente\\FL Studio 20\\Midis\\Cymatics Freebies - MIDI\\Cymatics - MIDI Chord Progressions Vol 3\\Cymatics - MIDI 22 - C#.mid','D:\\Daten\\Musik\\FL Studio\\out2.wav')
os.system('"sox.exe -m "D:\\Daten\\Musik\\FL Studio\\out1.wav" "D:\\Daten\\Musik\\FL Studio\\out2.wav" "D:\\Daten\\Musik\\FL Studio\\outCombined.wav""')