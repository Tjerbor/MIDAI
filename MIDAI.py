# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def dodo():
    s = """https://github.com/gavin-peterkin/music_composition
https://github.com/gavin-peterkin/music_composition/tree/master/src/scraping/midi
https://www.fourmilab.ch/webtools/midicsv/
https://github.com/timwedde/banana-split
https://github.com/TriYop/MIDI_Split
https://github.com/Rainbow-Dreamer/musicpy
https://github.com/ZaneH/piano-trainer
https://github.com/allthemusicllc/atm-cli
https://github.com/jjazzboss/JJazzLab-X
https://midifile.sapp.org/
https://timidity.sourceforge.net/
https://signal.vercel.app/
https://github.com/kosua20/MIDIVisualizer
https://github.com/FluidSynth/fluidsynth
https://github.com/1j01/midiflip
https://github.com/JamesOwers/midi_degradation_toolkit
https://github.com/Cornerback24/Python-Midi-Analysis
https://github.com/DamiPayne/AI-Music-Composer
https://github.com/Wally869/MidiSplitter
https://github.com/AlexPoulsen/vgmusic_midi_scraper
https://github.com/AlexPoulsen/ninsheetmusic_scraper
https://github.com/PatricioGuinle/CoffeMIDI
https://github.com/Kermalis/MIDIProgramSplitter
https://github.com/leegee/audio-glitch
https://github.com/sandershihacker/midi-classification-tutorial
https://cymatics.fm/blogs/production/soundfonts
https://sox.sourceforge.net/"""

    ss = s.splitlines()
    for x in range(len(ss)):
        print('- [' +ss[x]+']('+ss[x]+')')


if __name__ == '__main__':
    dodo()
